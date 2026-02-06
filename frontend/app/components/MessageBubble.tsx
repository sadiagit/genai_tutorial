// components/MessageBubble.tsx
"use client"

import { Message } from "@/types/chat"

export default function MessageBubble({ message }: { message: Message }) {
  const isUser = message.role === "user"

  return (
    <div className={`flex ${isUser ? "justify-end" : "justify-start"}`}>
      <div
        className={`rounded-lg px-4 py-2 max-w-[80%]
        ${isUser ? "bg-red-800 text-white" : "bg-gray-200 text-black"}`}
      >
        <p className="whitespace-pre-wrap">{message.content}</p>

        {message.sources && message.sources.length > 0 && (
          <div className="mt-2 text-xs text-gray-600">
            <p className="font-semibold">Sources:</p>
            <ul className="list-disc ml-4">
              {message.sources.map((s, i) => (
                <li key={i}>{typeof s === 'object' ? s.source : s}</li>
              ))}
            </ul>
          </div>
        )}
      </div>
    </div>
  )
}
