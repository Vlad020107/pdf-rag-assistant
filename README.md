# pdf-rag-assistant

A local RAG assistant that answers questions about PDF documents using Python, FAISS, Hugging Face embeddings, and Ollama.

## Overview

This project allows users to ask questions about the content of PDF documents.

The assistant reads a PDF file, splits its text into smaller fragments, converts the fragments into vector embeddings, and searches for the most relevant information. A local Ollama language model then generates a clear text answer based on the retrieved PDF context.

The project runs locally, so private documents do not need to be sent to external AI services.

## Features

- Load and process PDF documents
- Split document text into searchable fragments
- Create vector embeddings with Hugging Face Sentence Transformers
- Search relevant fragments using FAISS
- Generate answers with a local Ollama model
- Answer questions in Russian
- Run continuously in the terminal until the user enters `exit`

## Technologies

- Python 3.12
- LangChain
- FAISS
- PyPDF
- Hugging Face Sentence Transformers
- Ollama
- Qwen 2.5 3B

## Project Structure

```text
pdf-rag-assistant/
├── main.py                 # Main application file
├── Pr4.pdf                 # Example PDF placeholder
├── README.md               # Project documentation
├── LICENSE                 # Project license
└── .gitignore              # Ignored files and folders
```

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/Vlad020107/pdf-rag-assistant.git
cd pdf-rag-assistant
```

### 2. Create and activate a virtual environment

Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Install Python dependencies

```bash
pip install pypdf langchain langchain-community langchain-text-splitters langchain-huggingface langchain-ollama faiss-cpu sentence-transformers
```

### 4. Install Ollama

Download and install Ollama from:

```text
https://ollama.com/download
```

### 5. Download the language model

```bash
ollama pull qwen2.5:3b
```

## Usage

1. Put your PDF document in the project folder.

2. Update the PDF filename in `main.py` if needed:

```python
pdf_path = "Pr4.pdf"
```

3. Run the application:

```bash
python main.py
```

4. Enter a question in the terminal.

Example:

```text
Ask a question: What is Bash?
```

5. To close the application, type:

```text
exit
```

## How It Works

```text
PDF document
     ↓
Text extraction with PyPDF
     ↓
Text splitting into fragments
     ↓
Embeddings with Sentence Transformers
     ↓
Similarity search with FAISS
     ↓
Relevant PDF context
     ↓
Answer generation with Ollama
     ↓
Text response
```

## Privacy

The application is designed to work locally.

The example `Pr4.pdf` file is a placeholder. Replace it with your own document before running the assistant. Do not upload private, copyrighted, or confidential documents to a public repository.

## Future Improvements

- Support multiple PDF documents
- Add conversation memory
- Save the FAISS index to avoid rebuilding it on every launch
- Add PDF upload through a web interface
- Display document sources and page numbers with each answer
- Add support for DOCX and TXT files

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
