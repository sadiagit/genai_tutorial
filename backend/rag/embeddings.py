import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

def embed_texts(texts: list[str]) -> list[list[float]]:
    genai.configure(api_key=os.environ["GEMINI_API_KEY"])
    response = genai.embed_content(
        model="gemini-embedding-001",
        content=texts
    )
    return response["embedding"]
