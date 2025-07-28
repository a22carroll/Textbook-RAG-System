# Textbook-RAG-System

# Textbook-RAG-System

A command-line Retrieval-Augmented Generation (RAG) system built in Python that allows users to upload a textbook-style PDF, extract and chunk its contents, embed and index those chunks using FAISS, and ask natural language questions about the content.

## Features

- PDF text extraction with `PyMuPDF`
- Text chunking for semantic processing
- Embedding of chunks using local or remote models
- Fast retrieval via FAISS vector index
- Context-aware answer generation using a language model

## Stack

- **PDF Parsing**: `PyMuPDF` (`fitz`)
- **Chunking & Embedding**: Custom logic + transformer-based embedding model
- **Vector Store**: `FAISS`
- **Answer Generation**: Hugging Face model or OpenAI (customizable)



