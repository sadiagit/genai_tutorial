// components/ChatInput.tsx
"use client"

import { useState } from "react"

export default function ChatInput({
  onSend
}: {
  onSend: (text: string) => void
}) {
  const [text, setText] = useState("")

  function submit() {
    if (!text.trim()) return
    onSend(text)
    setText("")
  }

  return (
    <div className="flex gap-2">
      <input
        className="flex-1 border rounded px-3 py-2"
        placeholder="Ask about your documents…"
        value={text}
        onChange={e => setText(e.target.value)}
        onKeyDown={e => e.key === "Enter" && submit()}
      />
      <button
        onClick={submit}
        className="bg-blue-600 text-white px-4 rounded"
      >
        Send
      </button>
    </div>
  )
}
