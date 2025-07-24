from utils import extract_text_from_pdf, chunk_text
from retriever import embed_chunks, build_faiss_index, search_index, model
from generator import generate_answer

text = extract_text_from_pdf("/home/a22carroll/python/projects/Textbook-RAG-System/Ifan Hughes, Thomas Hase - Measurements and their uncertainties-OUP (2010).pdf")
chunks = chunk_text(text)

embeddings = embed_chunks(chunks)
index = build_faiss_index(embeddings)

while True:
    query = input("Ask a question (or 'q' to quit): ")
    if query.lower() == 'q':
        break
    context = search_index(query, chunks, model, index)
    answer = generate_answer(query, context)
    print("\n📌", answer, "\n")
