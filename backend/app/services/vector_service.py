from sentence_transformers import SentenceTransformer
import chromadb

model = SentenceTransformer("all-MiniLM-L6-v2")

client = chromadb.PersistentClient(path="chroma_db")

collection = client.get_or_create_collection(
    name="nexus_documents"
)

def store_chunks(chunks):

    for i, chunk in enumerate(chunks):

        embedding = model.encode(chunk).tolist()

        collection.add(
            ids=[str(i)],
            embeddings=[embedding],
            documents=[chunk]
        )

    print("Chunks stored successfully")