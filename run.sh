#!/bin/bash

# MarkdownGPT RAG API Startup Script

echo "🚀 Starting MkdocsGPT RAG API..."

# Check if .env file exists
if [ ! -f .env ]; then
    echo "❌ Error: .env file not found"
    echo "Please create .env file with GOOGLE_API_KEY"
    exit 1
fi

# Check if db directory exists
if [ ! -d db ]; then
    echo "⚠️  Warning: db directory not found"
    echo "Make sure to run Embedding.ipynb first to create the database"
fi

# Check if UserGuide directory exists
if [ ! -d UserGuide ]; then
    echo "❌ Error: UserGuide directory not found"
    echo "Please create UserGuide directory with Markdown files"
    exit 1
fi

# Install dependencies
echo "📦 Installing dependencies..."
pip install -r requirements.txt

# Run the application
echo "✅ Dependencies installed. Starting server..."
uvicorn app:app --host 0.0.0.0 --port 8000 --reload

echo "🎉 API is running at http://localhost:8000"
echo "📖 API docs available at http://localhost:8000/docs"
