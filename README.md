# 🤖 LLM-Based RAG Chatbot using LangChain

This project is an end-to-end **Retrieval-Augmented Generation (RAG)** chatbot powered by **LangChain**, **OpenAI**, and a beautiful **Tailwind CSS** chat interface. It allows users to upload a PDF and chat with its contents in natural language.

---

## 📸 Preview

![image](https://github.com/user-attachments/assets/ddb320aa-63ea-4f55-8aaa-e3dc3d670d7c)

---

## 🚀 Features

- 📄 Upload any PDF and start chatting with it
- 🔍 Uses vector search + OpenAI embeddings
- 🧠 Supports conversation memory
- ⚡ FastAPI backend for document processing
- 💬 Tailwind CSS chat-style frontend
- 📦 Easy to deploy or extend

---

## 🛠️ Tech Stack

| Layer        | Technology                     |
|--------------|--------------------------------|
| LLM          | OpenAI GPT-3.5 Turbo           |
| Embeddings   | OpenAI Embeddings              |
| Framework    | LangChain (RAG, memory, chain) |
| Backend API  | FastAPI                        |
| Frontend     | HTML, Tailwind CSS             |
| Vector Store | DocArrayInMemorySearch         |

---

## 🧪 How It Works

1. User uploads a PDF file
2. Backend parses & splits it into chunks
3. Embeddings are created and stored in memory
4. User enters a question
5. Bot retrieves top relevant chunks and responds using OpenAI's LLM

---

## 🖥️ Local Setup

### 1. Clone the Repo

```bash
git clone https://github.com/Gokul5001/LLM-Based-RAG-BOT-using-Langchain.git
cd LLM-Based-RAG-BOT-using-Langchain


### 2. Install Python Dependencies

```bash
pip install -r requirements.txt
```

Or manually:

```bash
pip install fastapi uvicorn langchain openai python-dotenv pypdf
```

### 3. Create `.env` file

```bash
echo "OPENAI_API_KEY=sk-xxxx" > .env
```

### 4. Run the Python Backend

```bash
uvicorn chatbot_engine:app --reload --host 0.0.0.0 --port 8001
```

### 5. Start the Frontend

```bash
node server.js
# Make sure you have express server running if using Node.js
```

Then open your browser:
👉 [http://localhost:3000](http://localhost:3000)

---

## 📁 Project Structure

```
.
├── chatbot_engine.py        # FastAPI + LangChain backend
├── public/
│   ├── index.html           # Chat UI using Tailwind CSS
│   ├── style.css (optional)
│   └── ...
├── .env                     # API Key
├── .gitignore
└── requirements.txt
```

---

## 📌 To-Do / Enhancements

* [ ] Add persistent vector store (e.g., FAISS, Chroma)
* [ ] Support other file types (e.g., DOCX, TXT)
* [ ] User authentication
* [ ] Chatbot avatars & timestamps
* [ ] Deploy on Render or Hugging Face Spaces

---

## 💡 Inspiration

This project is inspired by the LangChain community's best practices for building RAG-based AI systems.

---

## 👨‍💻 Author

**Gokul K**
📬 [LinkedIn](https://www.linkedin.com/in/gokul5001)
📁 GitHub: [@Gokul5001](https://github.com/Gokul5001)

---

## 🪪 License

MIT License — feel free to use and modify!

```
