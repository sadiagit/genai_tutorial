from pyexpat.errors import messages
import google.generativeai as genai
import os
from dotenv import load_dotenv
from db.db import get_db_connection
from tools.todo_tool import handle_todo_tool
from .vectorstore import query_chunks
from .embeddings import embed_texts
from tools.todo_tool import tools

load_dotenv()
genai.configure(api_key=os.environ["GEMINI_API_KEY"])
for m in genai.list_models():
  if 'generateContent' in m.supported_generation_methods:
    print(m.name)

model = genai.GenerativeModel("models/gemini-flash-latest", tools=tools)
SYSTEM_PROMPT = """You are Genia, a helpful assistant.
You have access to retrieved context from documents and a todo_tool for managing todo tasks.

IMPORTANT INSTRUCTIONS:
1. ALWAYS prioritize answering questions using the retrieved context from documents first.
2. ONLY use the todo_tool if the question is explicitly about managing, creating, or modifying todo tasks (e.g., "add a task", "mark as done", "list my tasks").
3. Do NOT call todo_tool for general knowledge questions, even if they seem vaguely related.
4. If you call todo_tool, use its response to answer the user's question if relevant.
5. If retrieved context is available and relevant, use it to provide accurate answers.
6. If no relevant context or tool applies, tell the user you don't have that information.

Examples of when to use todo_tool:
- "Add a task to fix the prompt tomorrow"
- "Show me my tasks"
- "Mark task 1 as complete"

Examples of when NOT to use todo_tool:
- "What is the junior girls uniform?" (answer from document context)
- "What are the uniform standards?" (answer from document context)
- Any factual question answerable from retrieved documents

"""
def extract_text(response):
    if not response or not response.candidates:
        return ""

    parts = response.candidates[0].content.parts
    texts = [p.text for p in parts if hasattr(p, "text") and p.text]
    return "\n".join(texts)


def answer_question(question: str):
    query_embedding = embed_texts([question])[0]
    results = query_chunks(query_embedding)

    docs = results["documents"][0]
    metas = results["metadatas"][0]

    context_blocks = []
    for i, doc in enumerate(docs):
        source = metas[i].get("source", "unknown")
        context_blocks.append(f"[{i+1}] ({source}) {doc}")

    context = "\n\n".join(context_blocks)
    prompt = f"""{SYSTEM_PROMPT}

Available Tools:
- todo_tool: Manage your tasks
  * "add" - Add a new task. Provide the task description.
  * "list" - Show all your tasks. No parameters needed.
  * "complete" - Mark a task as done. Provide the task description to find and complete it (e.g., "Mark fix the prompt tomorrow as complete" → task="fix the prompt tomorrow")
  * "delete" - Delete a task. Provide the task description to find and delete it (e.g., "delete the prompt fix task" → task="prompt fix")

IMPORTANT: The tool will automatically find tasks by description matching. You don't need task IDs!

Retrieved Context from Documents:
{context}

User Question: {question}

Instructions: 
1. First, determine if this question requires the todo_tool or if it should be answered from the retrieved context.
2. If the question is about managing tasks, use the todo_tool with the appropriate action and parameters.
   - For "complete" or "delete": extract and pass the task description from the user's request
   - The tool will find the matching task automatically
3. If the question is about factual information, answer using the retrieved context above.
4. Provide a clear, helpful answer to the user.
"""
    messages =[{
        "role": "user",
        "parts": [{
            
            "text": f"{prompt}"
        }]
    }]

    

    response = model.generate_content(messages)
    part = response.candidates[0].content.parts

    tool_part =  next((p for p in part if hasattr(p, "function_call")), None)

    if tool_part:
        call = tool_part.function_call

        if call.name == "todo_tool":
            result = handle_todo_tool(
                1,
                dict(call.args)
            )
            
            # Build a simple tool response and include it in a new prompt
            # instead of appending to an undefined `messages` variable.
            messages.append({
                "role": "tool",
                "parts": [{
                    "function_response": {
                        "name": "todo_tool",
                        "response": result
                    }
                }]
            })
            messages.append({
    "role": "user",
    "parts": [{
        "text": "Summarize the tool result for the user."
    }]
})


            final = model.generate_content(messages)
        else:
            final = response
    else:
        final = response

    return {
        "answer": final.text,
        "sources": metas
    }
