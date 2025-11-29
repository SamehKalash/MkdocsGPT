# 🤖 mkdocsGPT - RAG Assistant

**mkdocsGPT** is a Retrieval-Augmented Generation (RAG) system that answers questions about your **MkDocs documentation**, grounded in your knowledge base.

It uses:
- 📖 **MkDocs documents** as the knowledge base
- 🧠 **Google's `text-embedding-005`** for semantic search
- 🌐 **ChromaDB** for vector storage
- 🤖 **Gemini 2** to generate accurate, context-grounded answers
- ⚙️ **FastAPI** as the backend for serving answers

![mkdocsGPT Demo]https://github.com/SamehKalash/MkdocsGPT/blob/main/mkdocsrag.gif)

---

## 🚀 Quick Start

### Prerequisites
- Python 3.10+
- Google API Key
- MKDocs documents in `UserGuide/`

### Installation & Setup

```bash
# Install dependencies
pip install -r requirements.txt

# Create .env file
echo "GOOGLE_API_KEY=your_api_key_here" > .env

# Embed documents (one-time)
jupyter notebook Embedding.ipynb

# Run the app
uvicorn app:app --reload
```

Then open **http://localhost:8000** in your browser.

---

## 📊 How It Works

### Phase 1: Embedding (`Embedding.ipynb`)
- Loads MkDocs files from `UserGuide/`
- Splits into chunks using `RecursiveCharacterTextSplitter`
- Embeds with `text-embedding-005`
- Stores in ChromaDB vector database

### Phase 2: Retrieval (`rag.py`)
- Embeds user question with same model
- Retrieves top-8 relevant chunks from ChromaDB
- Passes context to Gemini 2 for answer generation

### Phase 3: API & UI (`app.py` + `index.html`)
- FastAPI serves the backend
- Beautiful web UI for chat interface
- Real-time responses with animations

---

## 📡 API Reference

| Endpoint | Method | Purpose |
|----------|--------|---------|
| `/` | GET | Web UI |
| `/ask` | POST | Ask a question |
| `/docs` | GET | API Documentation |
| `/health` | GET | Health check |

**Example:**
```bash
curl -X POST http://localhost:8000/ask \
  -H "Content-Type: application/json" \
  -d '{"question": "How is it installed?"}'
```

---

## 🗂️ Project Structure

```
mkdirRAG/
├── app.py                 # FastAPI backend
├── rag.py                 # RAG logic
├── index.html             # Web UI
├── Embedding.ipynb        # Document embedding
├── requirements.txt       # Dependencies
├── .env                   # API keys
├── db/                    # ChromaDB vector store
└── UserGuide/             # MkDocs documents
```

---

## ⚙️ Configuration

**Embedding Model:** `models/text-embedding-005`  
**Generation Model:** `gemini-2.0-flash`  
**Vector DB:** ChromaDB  
**Query Results:** 8 documents  
**Collection:** `mkdocsGPT`

---

**Ready? Run `uvicorn app:app --reload` and visit http://localhost:8000! 🚀**
