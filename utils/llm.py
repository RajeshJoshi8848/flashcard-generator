import requests

def generate_flashcards(text):
    prompt = f"""
You are a helpful AI that creates 10-15 flashcards in the format:
Q: [question]
A: [answer]

Focus on definitions, concepts, key facts, comparisons, or examples.

Text:
{text[:4000]}
"""

    # Send prompt to local Ollama Mistral model
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "mistral",
            "prompt": prompt,
            "stream": False
        }
    )

    return response.json().get("response", "⚠️ Failed to generate flashcards.")
