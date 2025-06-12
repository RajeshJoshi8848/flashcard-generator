# app.py

import streamlit as st
from utils.pdf_reader import extract_text_from_pdf
from utils.llm import generate_flashcards
import json
import pandas as pd

st.set_page_config(page_title="Flashcard Generator", layout="wide")

st.title("📚 LLM-Powered Flashcard Generator")

# Input mode: file or text
input_mode = st.radio("Choose input type:", ("Upload PDF", "Paste Text"))

text_data = ""

if input_mode == "Upload PDF":
    uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])
    if uploaded_file is not None:
        text_data = extract_text_from_pdf(uploaded_file)
        st.success("✅ PDF content extracted!")

elif input_mode == "Paste Text":
    text_data = st.text_area("Paste your educational content here", height=300)

# Show extracted or pasted content
if text_data:
    st.subheader("Extracted Text Preview")
    st.write(text_data[:1000])  # preview first 1000 characters

    if st.button("Generate Flashcards"):
        with st.spinner("Generating flashcards..."):
            flashcards = generate_flashcards(text_data)

        st.subheader("🧠 Generated Flashcards")

        # ✏️ Let user edit the flashcards before export
        edited_flashcards = st.text_area("✏️ Review & Edit Flashcards", flashcards, height=400)

        # 📥 Download as .txt
        st.download_button("📥 Download as .txt", edited_flashcards, file_name="flashcards.txt")

        # Process Q&A for .json and .csv
        questions = [line.strip() for line in edited_flashcards.split('\n') if line.startswith("Q")]
        answers = [line.strip() for line in edited_flashcards.split('\n') if line.startswith("A")]
        flashcard_list = [{"Q": q, "A": a} for q, a in zip(questions, answers)]

        # 📥 Download as .json
        st.download_button("📥 Download as .json", json.dumps(flashcard_list, indent=2), file_name="flashcards.json")

        # 📥 Download as .csv
        df = pd.DataFrame(flashcard_list)
        csv = df.to_csv(index=False)
        st.download_button("📥 Download as .csv", csv, file_name="flashcards.csv")
