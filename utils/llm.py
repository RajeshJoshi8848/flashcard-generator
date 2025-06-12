# utils/llm.py

from transformers import pipeline

# Load the Hugging Face FLAN-T5 model
generator = pipeline("text2text-generation", model="google/flan-t5-base")

def generate_flashcards(text, subject_type=None):
    prompt = f"""
You are a helpful AI that generates study flashcards from educational material.

Please generate 10–15 high-quality question-answer flashcards based on the content below.

✅ Focus on:
- Definitions, facts, or key terms
- Project details, concepts, and skills
- Achievements, education, or data points

📌 Format:
Q1: [question]
A1: [answer]
Q2: [question]
A2: [answer]
...

📄 Content:
{text[:2500]}
"""
    result = generator(prompt, max_length=512, do_sample=False)[0]['generated_text']
    return result
