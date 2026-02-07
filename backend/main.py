from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import os
import shutil
from db.db import get_db_connection
from rag.loader import load_pdf, load_markdown
from rag.chunker import chunk_text
from rag.embeddings import embed_texts
from rag.vectorstore import add_chunks
from rag.rag_chain import answer_question
from db.create_todo_table import init_db
from sse.routes import router as sse_router

# Initialize the database if not already done
init_db()

app = FastAPI()

#register the SSE router
app.include_router(sse_router)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins (restrict in production)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    with open(file_path, "wb") as f:
        shutil.copyfileobj(file.file, f)

    if file.filename.endswith(".pdf"):
        text = load_pdf(file_path)
    elif file.filename.endswith(".md"):
        text = load_markdown(file_path)
    else:
        return {"error": "Unsupported file type"}

    chunks = chunk_text(text)
    embeddings = embed_texts(chunks)

    metadata = [{"source": file.filename} for _ in chunks]
    add_chunks(chunks, embeddings, metadata)

    return {"status": "indexed", "chunks": len(chunks)}

@app.post("/chat")
async def ask_question(payload: dict):
    question = payload.get("question")
    result = answer_question(question)
    return result

@app.get("/todos")
def get_todos(user_id: str):
    conn = get_db_connection()
    rows = conn.execute(
        "SELECT id, text, completed FROM todos WHERE user_id = ?",
        (user_id,)
    ).fetchall()

    return [dict(row) for row in rows]

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)