from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

model = SentenceTransformer('all-MiniLM-L6-v2')

def embed_chunks(chunks):
    return model.encode(chunks, convert_to_numpy=True)

def build_faiss_index(embeddings):
    dim = embeddings.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(embeddings)
    return index

def search_index(query, chunks, model, index, k=3):
    q_embed = model.encode([query], convert_to_numpy=True)
    _, indices = index.search(q_embed, k)
    return [chunks[i] for i in indices[0]]
