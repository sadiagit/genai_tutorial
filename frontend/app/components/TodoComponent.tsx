import { useEffect, useState } from "react";

export default function TodoComponent() {
    const [todos, setTodos] = useState<Array<{id: number; text: string; completed: boolean}>>([]);
  
    async function fetchTodos() {
      const response = await fetch(`http://localhost:8000/todos?user_id=1`);
      const data = await response.json();
      setTodos(data);
    }
     useEffect(() => {
    fetchTodos();
  }, []);
    return (
    <div className="w-64 p-4 bg-gray-50 border-l border-gray-200 h-screen fixed right-0 top-0">
      <h2 className="text-lg font-bold mb-4">Todo List</h2>
      <ul className="space-y-2">
        {todos.map((todo) => (
          <li key={todo.id} className="flex justify-between items-center">
            <span className={todo.completed ? "line-through text-gray-400" : ""}>
              {todo.text}
            </span>
            <span>{todo.completed ? "✅" : "⬜"}</span>
          </li>
        ))}
      </ul>
    </div>
  );
}