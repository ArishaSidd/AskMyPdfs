# 📚 Chat with PDFs using Local LLM (Ollama)

Interact with your PDF documents using natural language! This Streamlit app lets you upload multiple PDFs, extract their text, chunk and embed it, and chat with them using a locally hosted LLM like Mistral via [Ollama](https://ollama.com).

---

## 🚀 Features

- 📄 Upload and process multiple PDFs
- 🧠 Local language model integration using Ollama (e.g., `mistral`)
- 🔍 Smart text chunking and vector search using FAISS
- 💬 Conversational memory for contextual replies
- 🧱 Simple, clean UI built with Streamlit

---

## 🖼️ Demo

https://github.com/user-attachments/assets/0f509b04-7197-4924-9365-e7a7d16dd037

---

## 🧰 Tech Stack
- Frontend: Streamlit + HTML templates
- LLM: Local model (mistral) via Ollama
- Embeddings: sentence-transformers/all-MiniLM-L6-v2
- Vector Store: FAISS
- Document Parsing: PyPDF2
- Chain Framework: LangChain

---
## 🛠️ Installation & Setup

Follow these steps to set up the project locally:

### ✅ 1. Clone the Repository

```
git clone https://github.com/yourusername/chat-with-pdfs.git
cd chat-with-pdfs
```
### ✅ 2. Create and Activate Virtual Environment
```
# For Windows
python -m venv venv
venv\Scripts\activate

# For macOS/Linux
python3 -m venv venv
source venv/bin/activate
```
### ✅ 3. Install Python Dependencies
```
pip install -r requirements.txt
```
### ✅ 5. Run the Streamlit App
```
streamlit run app.py
```

## 📁 Project Structure

```bash
.
├── app.py                # Main Streamlit app
├── htmlTemplates.py      # Custom HTML templates for chat bubbles
├── requirements.txt      # Python dependencies
└── README.md             # This file

---


