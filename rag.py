from chromadb import PersistentClient
import chromadb.utils.embedding_functions as embedding_functions
import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

# Configure Gemini
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-2.0-flash")

# ChromaDB
chroma = PersistentClient(path="db/")
google_ef = embedding_functions.GoogleGenerativeAiEmbeddingFunction(
    api_key=api_key,
    model_name="models/text-embedding-004"
)

collection = chroma.get_collection(
    name="MKdocGPTv2",
    embedding_function=google_ef
)

def get_answer(prompt: str) -> str:
    results = collection.query(
        query_texts=[prompt],
        n_results=8
    )

    documents = results["documents"][0]
    context = "\n\n".join(documents)

    full_prompt = f"""
Use the following context to answer the question.

Context:
{context}

Question:
{prompt}
"""

    response = model.generate_content(full_prompt)
    return response.text.strip()
