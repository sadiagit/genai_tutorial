from pathlib import Path
import chromadb


BASE_DIR = Path(__file__).resolve().parent
chroma_client = chromadb.PersistentClient(path=str(BASE_DIR / "data/chroma"))

collection = chroma_client.get_or_create_collection(
    name="genia_docs"
)

def add_chunks(chunks: list[str], embeddings: list[list[float]], metadata: list[dict]):
    ids = [f"chunk_{i}" for i in range(len(chunks))]
    collection.add(
        documents=chunks,
        embeddings=embeddings,
        metadatas=metadata,
        ids=ids
    )

def query_chunks(query_embedding: list[float], k=5):
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=k
    )
    return results
