'use client'
import { useState } from "react"
import { Message } from "@/types/chat"
import ChatWindow from "@/components/ChatWindow"
import ChatInput from "@/components/ChatInput"
import FileUploader from "./components/FileUploader"
import TodoComponent from "./components/TodoComponent"

export default function HomePage() {
  const [messages, setMessages] = useState<Message[]>([])
  const [loading, setLoading] = useState(false)

  const sendMessage = async (content: string) => {

    const newMessage: Message = { role: 'user', content }
    setMessages([...messages, newMessage])
    setLoading(true)

    const res = await fetch("http://localhost:8000/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ question: content })
    })

    const data = await res.json()

    const aiMsg: Message = {
      role: "assistant",
      content: data.answer,
      sources: data.sources
    }
    setMessages(prev => [...prev, aiMsg])
    setLoading(false)
  }
  
  return (
    <main className="flex min-h-screen flex-col items-center justify-center p-24">
      <h1 className="text-4xl font-bold">Genia</h1>
      <FileUploader />
      <ChatWindow messages={messages} loading={loading} />
      <ChatInput onSend={sendMessage} />
      <TodoComponent />

    </main>
  )
}