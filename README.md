# Smart Document Intelligence System

An AI-powered document question-answering system that helps users retrieve relevant information from multiple PDF documents using semantic search.

## Features
- Extracts text from PDF documents.
- Supports multiple PDF documents.
- Splits extracted text into manageable chunks.
- Generates semantic embeddings.
- Retrieves relevant passages using similarity search.
- Retrieves relevant passages from PDF documents and displays their source page references.
- Provides an interactive Streamlit interface.

## Technology Stack
- Python
- PyMuPDF
- Sentence Transformers
- Scikit-learn
- NumPy
- Streamlit

## Project Structure

Smart_Document_Intelligence/
├── documents/
├── outputs/
├── Smart_Document_Intelligence.ipynb
├── app.py
├── answer_engine.py
├── pdf_processor.py
├── search_engine.py
├── requirements.txt
└── README.md

## How It Works

1. PDF documents are loaded.
2. Text is extracted from the PDFs.
3. Text is divided into chunks.
4. Embeddings represent the meaning of each chunk.
5. Semantic search retrieves relevant passages.
6. The application displays retrieved content and source pages.

## Run the Application

Install dependencies:

pip install -r requirements.txt

Launch:

streamlit run app.py

## Project Objective

To build a practical document intelligence application that makes information retrieval from large PDF collections faster and easier.