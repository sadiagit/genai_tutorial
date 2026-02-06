"use client"

import MessageBubble from "./MessageBubble";

export default function ChatWindow({ messages, loading }: { messages: { role: "user" | "assistant" | "system"; content: string; sources?: string[] }[]; loading: boolean }) {
  return (
    <div className="w-full max-w-2xl h-96 border border-gray-300 rounded-lg p-4 overflow-y-auto mb-4">  
        {messages.map((msg, index) => (
            <MessageBubble key={index} message={msg}/>
        ))} 

        {loading && (
            <div className="animate-pulse">Genia is thinking...</div>
        )}
    </div>
  )
}