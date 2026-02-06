# GenAI Tutorial: Full-Stack RAG Chat Application

A comprehensive tutorial project demonstrating a complete **Retrieval-Augmented Generation (RAG)** system with a modern full-stack architecture. This project combines a Python FastAPI backend with a Next.js frontend to create an intelligent chatbot that can answer questions from uploaded documents.

## 📋 Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Backend Setup](#backend-setup)
  - [Frontend Setup](#frontend-setup)
- [Running the Application](#running-the-application)
- [API Endpoints](#api-endpoints)
- [Project Components](#project-components)
  - [Backend Architecture](#backend-architecture)
  - [Frontend Architecture](#frontend-architecture)
- [Key Concepts](#key-concepts)
  - [RAG Pipeline](#rag-pipeline)
  - [Chunking & Tokenization](#chunking--tokenization)
  - [Embeddings & Vector Store](#embeddings--vector-store)
  - [Chat Interface](#chat-interface)
- [Database](#database)
- [Configuration](#configuration)
- [Common Issues & Fixes](#common-issues--fixes)
- [Contributing](#contributing)
- [License](#license)

---

## 🎯 Project Overview

This project is an **educational tutorial** that teaches you how to build a production-ready RAG (Retrieval-Augmented Generation) application. It demonstrates:

- ✅ Document upload and processing (PDF & Markdown)
- ✅ Text chunking and tokenization using `tiktoken`
- ✅ Embedding generation with Google Gemini
- ✅ Vector database storage using Chroma
- ✅ Semantic search and retrieval
- ✅ LLM-based question answering with context
- ✅ Full-stack implementation with modern frameworks
- ✅ Todo management with database integration
- ✅ File handling and processing workflows

---

## ✨ Features

### Backend Features
- **FastAPI Server** - High-performance async Python web framework
- **Document Processing** - Support for PDF and Markdown files
- **Text Chunking** - Intelligent text splitting using token-based chunking
- **Vector Embeddings** - Google Gemini embedding generation
- **Vector Database** - Chroma for semantic search
- **RAG Pipeline** - Retrieval-augmented generation for accurate answers
- **Todo Management** - Database-backed todo operations
- **CORS Support** - Cross-origin request handling
- **File Upload** - Secure file handling and processing

### Frontend Features
- **Modern Chat UI** - Clean, responsive design with Tailwind CSS
- **Real-time Chat** - Message display and input handling
- **File Upload** - Document upload with drag-and-drop
- **Chat History** - Message persistence and display
- **Todo Management** - Interactive todo list component
- **Type Safety** - Full TypeScript support
- **Responsive Design** - Works on desktop and mobile devices

---

## 🛠️ Tech Stack

### Backend
- **Python 3.x** - Primary backend language
- **FastAPI** - Modern web framework
- **Uvicorn** - ASGI server
- **PyPDF** - PDF parsing and text extraction
- **Chromadb** - Vector database
- **Google Gemini API** - Embeddings and LLM
- **Tiktoken** - OpenAI tokenizer for accurate chunking
- **SQLite** - Data persistence

### Frontend
- **Next.js 16.x** - React metaframework
- **React 19.x** - UI library
- **TypeScript** - Type safety
- **Tailwind CSS** - Styling
- **ESLint** - Code linting

---

## 📁 Project Structure

```
genai_tutorial/
├── backend/
│   ├── __init__.py
│   ├── main.py                 # FastAPI application entry point
│   ├── requirements.txt         # Python dependencies
│   ├── db/
│   │   ├── __init__.py
│   │   ├── db.py               # Database connection utilities
│   │   └── create_todo_table.py # Todo table initialization
│   ├── rag/
│   │   ├── __init__.py
│   │   ├── loader.py           # Document loading (PDF, Markdown)
│   │   ├── chunker.py          # Text chunking logic
│   │   ├── embeddings.py       # Embedding generation
│   │   ├── vectorstore.py      # Vector database operations
│   │   ├── rag_chain.py        # RAG orchestration
│   │   └── data/
│   │       └── chroma/         # Vector store data
│   ├── tools/
│   │   └── todo_tool.py        # Todo management operations
│   └── uploads/                # Uploaded document storage
│
├── frontend/
│   ├── app/
│   │   ├── layout.tsx          # Root layout component
│   │   ├── page.tsx            # Main page component
│   │   ├── globals.css         # Global styles
│   │   └── components/
│   │       ├── ChatWindow.tsx  # Chat display component
│   │       ├── ChatInput.tsx   # Message input component
│   │       ├── FileUploader.tsx# Document upload component
│   │       ├── MessageBubble.tsx # Message display
│   │       └── TodoComponent.tsx # Todo list component
│   ├── types/
│   │   └── chat.ts             # TypeScript type definitions
│   ├── public/                 # Static assets
│   ├── package.json
│   ├── tsconfig.json
│   ├── next.config.ts
│   ├── tailwind.config.ts
│   └── postcss.config.mjs
│
├── README.md                   # This file
├── prep.md                     # Development notes
└── issues_summary.md           # Known issues and fixes
```

---

## 🏛️ Architecture Diagrams

### System Architecture Overview
![alt text](designs\system-arch.png)


### RAG Pipeline Flowchart
![alt text](designs\rag-pipeline.png)



### Component Interaction Diagram



### Data Flow Diagram



### Tech Stack Architecture
![alt text](designs\tech-stack.png)



---

## 🚀 Getting Started

### Prerequisites

- **Python 3.8+** for the backend
- **Node.js 18+** for the frontend
- **npm or yarn** package manager
- **Google Gemini API Key** for embeddings and LLM
- **Git** for version control

### Backend Setup

1. **Navigate to the backend directory:**
   ```bash
   cd backend
   ```

2. **Create a Python virtual environment:**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment:**
   - **Windows:**
     ```bash
     venv\Scripts\activate
     ```
   - **macOS/Linux:**
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

5. **Set environment variables:**
   - Create a `.env` file or set system environment variables
   ```bash
   set GEMINI_API_KEY=your_actual_gemini_api_key
   ```

6. **Initialize the database:**
   ```bash
   python -c "from db.create_todo_table import init_db; init_db()"
   ```

### Frontend Setup

1. **Navigate to the frontend directory:**
   ```bash
   cd frontend
   ```

2. **Install dependencies:**
   ```bash
   npm install
   # or
   yarn install
   ```

3. **Configure API endpoint** (if needed):
   - Update API calls in components to point to your backend URL
   - Default assumes backend runs on `http://localhost:8000`

---

## ▶️ Running the Application

### Starting the Backend Server

1. **From the backend directory with virtual environment activated:**
   ```bash
   uvicorn main:app --reload
   ```
   - The server will start on `http://localhost:8000`
   - The `--reload` flag enables auto-restart on code changes
   - API documentation available at `http://localhost:8000/docs`

### Starting the Frontend Development Server

1. **From the frontend directory:**
   ```bash
   npm run dev
   # or
   yarn dev
   ```
   - The application will open at `http://localhost:3000`
   - The frontend automatically connects to the backend

### Production Build

**Frontend:**
```bash
npm run build
npm start
```

**Backend:**
```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

---

## 📡 API Endpoints

### Document Upload and Indexing

**`POST /upload`**
- **Description:** Upload a document (PDF or Markdown) for indexing
- **Parameters:**
  - `file` (form-data): The document file
- **Returns:**
  - Status: "indexed"
  - Number of chunks created
- **Example:**
  ```bash
  curl -X POST "http://localhost:8000/upload" \
    -F "file=@document.pdf"
  ```

### Chat/Question Answering

**`POST /chat`** (or similar endpoint)
- **Description:** Submit a question and receive RAG-based answers
- **Parameters:**
  - `question` (string): The user's question
- **Returns:**
  - Response from LLM based on retrieved documents

### Todo Management

**`POST /todos`**
- **Description:** Create a new todo item

**`GET /todos`**
- **Description:** Retrieve all todo items

**`PUT /todos/{id}`**
- **Description:** Update a todo item

**`DELETE /todos/{id}`**
- **Description:** Delete a todo item

---

## 🏗️ Project Components

### Backend Architecture

#### Document Loading (`rag/loader.py`)
Handles document parsing:
- **PDF Files:** Extracts text using PyPDF
- **Markdown Files:** Reads raw text content
- Error handling for unsupported formats

#### Text Chunking (`rag/chunker.py`)
Intelligently splits documents using token counting:
- Default chunk size: ~800 tokens
- Overlap: ~200 tokens to maintain context
- Uses `tiktoken` for accurate token counting
- Ensures chunks align with LLM token limits

#### Embeddings (`rag/embeddings.py`)
Generates vector representations:
- Uses Google Gemini's text-embedding-004 model
- Requires GEMINI_API_KEY environment variable
- Returns embeddings as float vectors

#### Vector Store (`rag/vectorstore.py`)
Manages vector database operations:
- Uses Chroma for local vector storage
- Stores chunks with metadata
- Enables semantic similarity search
- Supports persistent storage

#### RAG Chain (`rag/rag_chain.py`)
Orchestrates the complete RAG pipeline:
1. Embeds user question
2. Retrieves relevant document chunks
3. Creates prompt with retrieved context
4. Calls LLM to generate answer
5. Returns grounded response

#### Database (`db/db.py` & `db/create_todo_table.py`)
- SQLite database for todo management
- Table schema for todo items
- CRUD operations support

### Frontend Architecture

#### Layout (`app/layout.tsx`)
- Root component wrapping all pages
- Global styles and metadata
- Provider setup

#### Main Page (`app/page.tsx`)
- Orchestrates main application UI
- Combines chat window, input, and file upload
- State management for messages

#### Components

**ChatWindow.tsx**
- Displays conversation history
- Shows loading states
- Renders message bubbles

**ChatInput.tsx**
- Text input for user messages
- Send button with validation
- Keyboard event handling

**FileUploader.tsx**
- Document upload interface
- Progress indication
- File type validation

**MessageBubble.tsx**
- Individual message rendering
- User vs. AI message styling
- Message formatting

**TodoComponent.tsx**
- Todo list display
- Add/delete todo operations
- UI for todo management

#### Types (`types/chat.ts`)
TypeScript definitions for type safety across the application

---

## 💡 Key Concepts

### RAG Pipeline

**What is RAG?**
Retrieval-Augmented Generation (RAG) improves LLM responses by:
1. Retrieving relevant information from your documents
2. Augmenting the LLM prompt with this information
3. Generating more accurate, grounded answers

**Why RAG?**
- **Accuracy:** Grounds responses in actual documents
- **Freshness:** Uses your data, not just model training data
- **Citations:** Answers reference source documents
- **Control:** You control what documents are available

### Chunking & Tokenization

**Why Chunking?**
- LLMs have context limits (token limits)
- Embedding models work better on smaller passages
- Allows for efficient storage and retrieval
- Enables precise context management

**Token-Based Chunking:**
```python
def chunk_text(text: str, chunk_size=800, overlap=200):
    # Use tiktoken to count tokens accurately
    tokens = encode(text)
    # Split on token boundaries, not character boundaries
    # Ensures chunks fit within token limits
    return chunks
```

### Embeddings & Vector Store

**How Embeddings Work:**
- Convert text to high-dimensional vectors
- Similar content = similar vectors
- Enables semantic search (not just keyword matching)
- Enables measuring text similarity

**Vector Database (Chroma):**
- Stores text chunks and their embeddings
- Provides semantic search capability
- Supports similarity queries
- Enables fast retrieval

**Flow:**
```
Document → Chunks → Embeddings → Chroma → Retrieval on Query
```

### Chat Interface

**User Interaction Flow:**
1. User types question in chat input
2. Frontend sends question to backend
3. Backend embeds question
4. Backend retrieves relevant chunks
5. Backend generates answer using LLM
6. Answer sent back to frontend
7. Frontend displays answer in chat window

---

## 💾 Database

### Todo Table Schema

The application uses SQLite with a `todos` table:

```sql
CREATE TABLE IF NOT EXISTS todos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT,
    completed BOOLEAN DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
```

**Database Location:** `backend/db/todos.db`

**Operations:**
- Create new todos
- Read/retrieve todos
- Update todo status
- Delete completed todos

---

## ⚙️ Configuration

### Environment Variables

Create a `.env` file in the backend directory:

```bash
# Google Gemini API
GEMINI_API_KEY=your_actual_api_key

# Database (optional)
DATABASE_URL=sqlite:///./todos.db

# Server Configuration
BACKEND_HOST=0.0.0.0
BACKEND_PORT=8000

# Frontend Configuration (in frontend .env)
NEXT_PUBLIC_API_URL=http://localhost:8000
```

### Backend Configuration

**CORS Settings:**
```python
# In main.py - currently allows all origins
# FOR PRODUCTION: Restrict to specific origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://yourdomain.com"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

**Upload Settings:**
```python
UPLOAD_DIR = "uploads"  # Directory for uploaded files
CHUNK_SIZE = 800        # Tokens per chunk
CHUNK_OVERLAP = 200     # Token overlap between chunks
```

---

## 🐛 Common Issues & Fixes

### Issue 1: ModuleNotFoundError - "No module named 'rag'"

**Cause:**
- Missing `__init__.py` files
- Incorrect import paths

**Solution:**
- Ensure all directories have `__init__.py` files
- Use correct import paths: `from backend.rag.loader import ...`

### Issue 2: GEMINI_API_KEY not found

**Cause:**
- Environment variable not set
- Missing in `.env` file

**Solution:**
```bash
# Windows (Command Prompt)
set GEMINI_API_KEY=your_key

# Windows (PowerShell)
$env:GEMINI_API_KEY="your_key"

# Linux/macOS
export GEMINI_API_KEY=your_key
```

### Issue 3: Internal Server Error (500) on Upload

**Cause:**
- Missing or incorrect API key
- Wrong response key in embedding parsing

**Solution:**
- Verify GEMINI_API_KEY is set correctly
- Check `embeddings.py` uses correct response key: `response["embedding"]`

### Issue 4: CORS Errors in Frontend

**Cause:**
- Backend not accepting requests from frontend URL
- CORS middleware misconfigured

**Solution:**
- In development: Keep `allow_origins=["*"]`
- In production: Specify exact frontend URL

### Issue 5: Upload Directory Permission Errors

**Cause:**
- Missing upload directory
- Insufficient permissions

**Solution:**
```python
# Automatic in code:
os.makedirs(UPLOAD_DIR, exist_ok=True)

# Or manually:
mkdir uploads
```

---

## 📚 Learning Path

Follow this recommended order to learn the concepts:

1. **Start with Backend Basics**
   - Understand `main.py` and FastAPI setup
   - Learn about file upload handling

2. **Learn Document Processing**
   - Study `rag/loader.py` for document parsing
   - Understand `rag/chunker.py` for text splitting

3. **Understand Embeddings**
   - Learn how `rag/embeddings.py` generates vectors
   - Understand embedding similarity

4. **Vector Database**
   - Study `rag/vectorstore.py`
   - Learn how semantic search works

5. **RAG Pipeline**
   - Understand complete flow in `rag/rag_chain.py`
   - Learn context augmentation

6. **Frontend Integration**
   - Build the UI components
   - Connect to backend APIs

7. **Database & Persistence**
   - Learn todo management
   - Understand data persistence

---

## 🚢 Deployment

### Backend Deployment Options

**Heroku:**
```bash
heroku login
heroku create your-app-name
git push heroku main
```

**Docker:**
```dockerfile
FROM python:3.11
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["uvicorn", "main:app", "--host", "0.0.0.0"]
```

### Frontend Deployment Options

**Vercel (Recommended for Next.js):**
- Connect GitHub repository
- Auto-deploys on push
- Environment variables in Vercel dashboard

**Netlify:**
```bash
npm run build
netlify deploy --prod --dir=.next
```

---

## 📖 Additional Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Next.js Documentation](https://nextjs.org/docs)
- [Chroma Vector DB](https://www.trychroma.com/)
- [Google Gemini API](https://ai.google.dev/)
- [RAG Tutorial](https://docs.llamaindex.ai/en/stable/)
- [Token Counting with tiktoken](https://github.com/openai/tiktoken)

---

## 🤝 Contributing

Contributions are welcome! Here's how to contribute:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/amazing-feature`)
3. **Commit** your changes (`git commit -m 'Add amazing feature'`)
4. **Push** to the branch (`git push origin feature/amazing-feature`)
5. **Open** a Pull Request

---

## 📝 License

This project is provided as an educational tutorial. Feel free to use, modify, and learn from it.

---

## ❓ FAQ

**Q: Can I use a different LLM provider?**
A: Yes! Modify `rag/embeddings.py` and `rag/rag_chain.py` to use your preferred provider (OpenAI, Anthropic, etc.)

**Q: What's the maximum file size I can upload?**
A: Currently unlimited by code, but adjust based on your server capacity

**Q: How do I improve RAG accuracy?**
A: Experiment with chunk size, overlap, retrieval k-value, and prompt engineering

**Q: Can I use this in production?**
A: Yes, but add proper authentication, rate limiting, input validation, and error handling

---

## 📞 Support

For issues and questions:
- Check the `issues_summary.md` file for known problems and fixes
- Review code comments for implementation details
- Refer to official documentation for each dependency

---

**Happy Learning! 🎓**

This tutorial is designed to teach you production-ready RAG architecture. Experiment, modify, and build upon it!
