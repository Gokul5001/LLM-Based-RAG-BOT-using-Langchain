# chatbot_engine.py
from fastapi import FastAPI, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from langchain.chains import ConversationalRetrievalChain
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.memory import ConversationBufferMemory
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import DocArrayInMemorySearch
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.chat_models import ChatOpenAI


import uvicorn
import os
from dotenv import load_dotenv

load_dotenv()
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
qa_chain = None

@app.post("/upload-pdf/")
async def upload_pdf(file: UploadFile):
    content = await file.read()
    with open("uploaded.pdf", "wb") as f:
        f.write(content)

    loader = PyPDFLoader("uploaded.pdf")
    documents = loader.load()
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=150)
    docs = splitter.split_documents(documents)

    embeddings = OpenAIEmbeddings()
    vectordb = DocArrayInMemorySearch.from_documents(docs, embeddings)

    retriever = vectordb.as_retriever(search_kwargs={"k": 3})
    global qa_chain
    qa_chain = ConversationalRetrievalChain.from_llm(
        ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0),
        retriever=retriever,
        memory=memory
    )
    return {"message": "PDF loaded successfully."}


@app.post("/ask/")
async def ask_question(payload: dict):
    global qa_chain
    question = payload.get("question")
    if qa_chain:
        result = qa_chain({"question": question})
        return {"answer": result['answer']}
    return {"answer": "Please upload a PDF first."}


if __name__ == "__main__":
    uvicorn.run("chatbot_engine:app", host="0.0.0.0", port=8001, reload=True)
