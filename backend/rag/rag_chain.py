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

model = genai.GenerativeModel("models/gemini-2.5-flash-lite", tools=tools)
SYSTEM_PROMPT = """You are Genia, a helpful assistant.

If the question is about todos:
- Call todo_tool before answering

You may use:
- Retrieved context
- Tool responses

Trust tool responses over context.
If unsure after tools, say you don't know.
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
    prompt = f"""
{SYSTEM_PROMPT}
You have access to a todo_tool that can:
- add tasks
- list tasks
- complete tasks
- delete tasks

Context:
{context}

Question: {question}
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
