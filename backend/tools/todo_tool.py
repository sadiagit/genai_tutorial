import asyncio
import json
from db.db import get_db_connection
from google.generativeai.types import FunctionDeclaration, Tool
from difflib import SequenceMatcher
from sse.events import broadcaster

todo_function = FunctionDeclaration(
    name="todo_tool",
    description="Manage the user's todo list. For 'complete' and 'delete' actions, provide the task description to find the matching task (e.g., 'mark fix the prompt task as complete' → task_description='fix the prompt'). You can also provide task_id if the user explicitly mentions a task number.",
    parameters={
        "type": "object",
        "properties": {
            "action": {
                "type": "string",
                "enum": ["add", "list", "complete", "delete"],
                "description": "The action to perform on the todo list"
            },
            "task": {
                "type": "string",
                "description": "The task description. For 'add' action: the new task text. For 'complete'/'delete': provide the task description to find the matching task."
            },
            "task_id": {
                "type": "integer",
                "description": "Optional: The task ID. Only use if user explicitly mentions a task number (e.g., 'task 1', 'item 2'). If not provided, the tool will find the task by description matching."
            }
        },
        "required": ["action"]
    }
)


def find_task_by_description(user_id: str, description: str) -> dict:
    """
    Find a task by matching its description.
    Uses fuzzy matching to find the best match.
    Returns task ID and details if found, or error if no match.
    """
    db = get_db_connection()
    rows = db.execute(
        "SELECT id, text, completed FROM todos WHERE user_id = ? AND completed = 0",
        (user_id,)
    ).fetchall()
    
    if not rows:
        return {"error": "No active tasks found", "task_id": None}
    
    # Find best matching task using sequence matching
    best_match = None
    best_score = 0
    
    for row_id, row_text, row_completed in rows:
        score = SequenceMatcher(None, description.lower(), row_text.lower()).ratio()
        if score > best_score:
            best_score = score
            best_match = (row_id, row_text, score)
    
    # If match score is above 50%, consider it a match
    if best_match and best_score >= 0.5:
        return {"task_id": best_match[0], "task_text": best_match[1], "match_score": best_match[2]}
    
    return {"error": f"No task found matching '{description}'. Active tasks: {[row[1] for row in rows]}", "task_id": None}

def handle_todo_tool(user_id: str, args: dict):
    db = get_db_connection()
    action = args["action"]

    if action == "add":
        text = args.get("task", "")
        if not text:
            return {"error": "Task description is required for 'add' action"}
        db.execute(
            "INSERT INTO todos (user_id, text) VALUES (?, ?)",
            (user_id, text)
        )
        db.commit()
        
        # run broadcast in background
        asyncio.create_task(broadcaster.broadcast(json.dumps({
            "event": "todos_updated",
            "action": "add",
            "data": f"New task added: {text}"
        })))
        return {"status": "added", "task": text}

    if action == "list":
        rows = db.execute(
            "SELECT id, text, completed FROM todos WHERE user_id = ?",
            (user_id,)
        ).fetchall()
        tasks = [{"id": row[0], "text": row[1], "completed": row[2]} for row in rows]
        return {"tasks": tasks}

    if action == "complete":
        # Try to find task by ID first, then by description
        task_id = args.get("task_id")
        task_description = args.get("task")
        
        if not task_id and not task_description:
            return {"error": "Either task_id or task description is required for 'complete' action"}
        
        # If task_id is provided, use it directly
        if task_id:
            db.execute(
                "UPDATE todos SET completed = 1 WHERE id = ? AND user_id = ?",
                (task_id, user_id)
            )
            db.commit()
            asyncio.create_task(broadcaster.broadcast(json.dumps({
                "event": "todos_updated",
                "action": "complete",
                "task_id": task_id
            })))
            return {"status": "completed", "task_id": task_id}
        
        # Otherwise, find task by description
        match_result = find_task_by_description(user_id, task_description)
        if "error" in match_result:
            return match_result
        
        task_id = match_result["task_id"]
        db.execute(
            "UPDATE todos SET completed = 1 WHERE id = ? AND user_id = ?",
            (task_id, user_id)
        )
        db.commit()
        asyncio.create_task(broadcaster.broadcast(json.dumps({
            "event": "todos_updated",
            "action": "complete",
            "task_id": task_id,
            "task": match_result["task_text"]
        })))
        return {"status": "completed", "task_id": task_id, "task": match_result["task_text"]}
    
    if action == "delete":
        # Try to find task by ID first, then by description
        task_id = args.get("task_id")
        task_description = args.get("task")
        
        if not task_id and not task_description:
            return {"error": "Either task_id or task description is required for 'delete' action"}
        
        # If task_id is provided, use it directly
        if task_id:
            db.execute(
                "DELETE FROM todos WHERE id = ? AND user_id = ?",
                (task_id, user_id)
            )
            db.commit()
            asyncio.create_task(broadcaster.broadcast(json.dumps({
                "event": "todos_updated",
                "action": "delete",
                "task_id": task_id
            })))
            return {"status": "deleted", "task_id": task_id}
        
        # Otherwise, find task by description
        match_result = find_task_by_description(user_id, task_description)
        if "error" in match_result:
            return match_result
        
        task_id = match_result["task_id"]
        db.execute(
            "DELETE FROM todos WHERE id = ? AND user_id = ?",
            (task_id, user_id)
        )
        db.commit()
        asyncio.create_task(broadcaster.broadcast(json.dumps({
            "event": "todos_updated",
            "action": "delete",
            "task_id": task_id,
            "task": match_result["task_text"]
        })))
        return {"status": "deleted", "task_id": task_id, "task": match_result["task_text"]}

tools = [Tool(function_declarations=[todo_function])]
