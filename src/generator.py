from openai import OpenAI

client = OpenAI()

def generate_answer(query, context_chunks):
    context = "\n".join(context_chunks)
    prompt = f"Answer using this context:\n{context}\n\nQuestion: {query}"

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message["content"]
