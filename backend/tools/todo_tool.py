from db.db import get_db_connection
from google.generativeai.types import FunctionDeclaration, Tool

todo_function = FunctionDeclaration(
    name="todo_tool",
    description="Manage the user's todo list",
    parameters={
        "type": "object",
        "properties": {
            "action": {
                "type": "string",
                "enum": ["add", "list", "complete", "delete"]
            },
            "task": {
                "type": "string"
            },
            "task_id": {
                "type": "integer"
            }
        },
        "required": ["action"]
    }
)

def handle_todo_tool(user_id: str, args: dict):
    db = get_db_connection()
    action = args["action"]

    if action == "add":
        text = args["task"]
        db.execute(
            "INSERT INTO todos (user_id, text) VALUES (?, ?)",
            (user_id, text)
        )
        db.commit()
        return {"status": "added"}

    if action == "list":
            rows = db.execute(
                "SELECT id, text, completed FROM todos WHERE user_id = ?",
                (user_id,)
            ).fetchall()
            return {"tasks": [{"id": row[0], "text": row[1], "completed": row[2]} for row in rows]}

    if action == "complete":
        db.execute(
            "UPDATE todos SET completed = 1 WHERE id = ? AND user_id = ?",
            (args["task_id"], user_id)
        )
        db.commit()
        return {"status": "completed"}
    if action == "delete":
        db.execute(
            "DELETE FROM todos WHERE id = ? AND user_id = ?",
            (args["task_id"], user_id)
        )
        db.commit()
        return {"status": "deleted"}

tools = [Tool(function_declarations=[todo_function])]
