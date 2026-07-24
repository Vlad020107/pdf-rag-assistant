# -*- coding: utf-8 -*-

from langchain_ollama import ChatOllama
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

pdf_path = "Pr4.pdf"

loader = PyPDFLoader(pdf_path)
pages = loader.load()

print("Загружено страниц:", len(pages))

splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=150
)
chunks = splitter.split_documents(pages)

print("Создано фрагментов:", len(chunks))

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2",
    encode_kwargs={"normalize_embeddings": True}
)

db = FAISS.from_documents(chunks, embeddings)

llm = ChatOllama(
    model="qwen2.5:3b",
    temperature=0
)

while True:
    query = input("\nYour query (или '0'): ").strip()

    if query.lower() == "0":
        print("Программа завершена.")
        break

    if not query:
        print("Введите вопрос.")
        continue

    results = db.similarity_search(query, k=3)

    context = "\n\n".join(
        f"[Страница {doc.metadata.get('page', 0) + 1}]\n{doc.page_content}"
        for doc in results
    )

    prompt = f"""
Ты помощник по учебным материалам.

Ответь на вопрос пользователя, используя только контекст из PDF.
Если в контексте нет ответа, честно скажи:
«В загруженных документах я не нашёл ответа».

Контекст:
{context}

Вопрос:
{query}

Дай понятный, краткий и практический ответ на русском языке.
"""

    answer = llm.invoke(prompt)

    print("\nОтвет:")
    print(answer.content)

