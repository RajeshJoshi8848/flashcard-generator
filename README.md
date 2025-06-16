# 📚 Flashcard Generator using LLMs

A smart and offline-capable flashcard generator built with Python, Streamlit, and open-source large language models (LLMs) running locally via Ollama.

## 🚀 Demo

▶️ [Watch the Demo Video](https://drive.google.com/file/d/1FW42fsWfDKKGLj3mzh0EsH86P6PZ38Ej/view?usp=sharing )

---

## 📌 Features

- 🧠 Generates 10–15 question-answer flashcards from educational content
- 📄 Supports both **PDF upload** and **plain text** input
- 💻 Runs completely **offline** using local LLMs via [Ollama](https://ollama.com)
- ⚡ Optimized for performance on laptops with 8 GB RAM
- 💾 Download flashcards in `.txt`, `.json`, or `.csv` format
- 🛡️ No API keys or external requests required

---

## 🧰 Tech Stack

| Layer        | Technology            |
|--------------|------------------------|
| Frontend     | Streamlit              |
| AI Model     | Mistral / Gemma (Ollama) |
| PDF Parsing  | PyMuPDF (`fitz`)       |
| Local Server | Ollama                 |
| Language     | Python 3.11+           |
| Version Ctrl | Git + GitHub           |

---

## 🛠️ How It Works

1. User uploads a PDF or pastes educational text.
2. Text is extracted and sent as a prompt to a local LLM.
3. The model (e.g. `mistral` or `gemma:2b`) generates flashcards.
4. Flashcards are displayed and can be downloaded.

---

## 📷 Screenshots

| Upload & Preview         | Flashcards Output             |
|--------------------------|-------------------------------|
| ![Upload](![image](https://github.com/user-attachments/assets/18b9000f-b4f5-43b7-be51-4d7864e7b51e)
) | ![Output](![image](https://github.com/user-attachments/assets/9395efe2-da72-4093-ab81-3d6766f6ab5c)
) |

