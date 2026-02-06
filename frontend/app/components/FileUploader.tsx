// components/FileUploader.tsx
"use client"

import { useState } from "react"

export default function FileUploader() {
  const [file, setFile] = useState<File | null>(null)
  const [loading, setLoading] = useState(false)

  async function upload() {
    if (!file) return

    const formData = new FormData()
    formData.append("file", file)

    setLoading(true)

    await fetch("http://localhost:8000/upload", {
      method: "POST",
      body: formData
    })

    setLoading(false)
    setFile(null)
    alert("File indexed successfully")
  }

  return (
    <div className="border rounded p-3 mb-4">
      <input
        type="file"
        accept=".pdf,.txt,.md"
        onChange={e => setFile(e.target.files?.[0] || null)}
      />

      <button
        onClick={upload}
        disabled={!file || loading}
        className="ml-2 bg-green-600 text-white px-3 py-1 rounded"
      >
        {loading ? "Uploading…" : "Upload"}
      </button>
    </div>
  )
}
