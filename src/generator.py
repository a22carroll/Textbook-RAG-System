import openai
import os
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_answer(query, context_chunks):
    context = "\n".join(context_chunks)
    prompt = f"Answer using this context:\n{context}\n\nQuestion: {query}"

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message["content"]
