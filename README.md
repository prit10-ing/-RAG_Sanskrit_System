# Sanskrit RAG System

A Retrieval-Augmented Generation (RAG) system for Sanskrit documents using LangChain, ChromaDB, HuggingFace embeddings, and HuggingFace chat models.

The system allows users to ask questions from Sanskrit PDF documents and generates context-aware answers using semantic retrieval and LLM-based generation.

---

# Features

- Sanskrit PDF document ingestion
- Recursive text chunking
- Semantic similarity retrieval
- ChromaDB vector database
- HuggingFace multilingual embeddings
- HuggingFace chat model integration
- Streamlit-based UI
- CPU-based inference support

---

# Project Structure

project/

│── data/                     # Sanskrit PDF documents

│── code/

│   ├── __init__.py

│   ├── llm_model.py

│   ├── load_documents.py

│   ├── retriever.py

│   ├── text_spliter.py

│   ├── vectore_store.py

│── report/

│   ├── __init__.py


│── vector_db/ # Persistent vector database

├── rag_main.py

│── requirements.txt

│── .env

│── README.md

---

# Technologies Used

| Component | Technology |
|---|---|
| Framework | LangChain |
| PDF Loader | PyPDFLoader |
| Text Splitter | RecursiveCharacterTextSplitter |
| Embeddings | HuggingFaceEmbeddings |
| Vector Store | ChromaDB |
| Retriever | Similarity Search |
| LLM | ChatHuggingFace |
| UI | Streamlit |

---

# Installation

## Step 1 — Clone Repository

```bash
git clone <repository_url>

cd RAG_Sanskrit_PRITESH

-------------------------------------------------------------------------------

 Step 2 — Create Virtual Environment


Windows
python -m venv venv

venv\Scripts\activate


Linux / Mac
python3 -m venv venv

source venv/bin/activate



------------------------------------------------------------------------------
Step 3 — Install Requirements
pip install -r requirements.txt


Environment Variables
Create a .env file in the project root.

Example:

HUGGINGFACEHUB_API_TOKEN=your_huggingface_token

Get your HuggingFace token from:

https://huggingface.co/settings/tokens

Add Documents

Place Sanskrit PDF documents inside:

Data/

Example:

data/

│── story1.pdf


Run the Application

From the project root directory run:

streamlit run code/app.py


Example Queries : 

कालीदासः कः आसीत् ?

देवः कदा साहाय्यं करोति ?

Who was Kalidasa?

What is the moral of the story?


-------------------------------------------------------------------------------

System Workflow
PDF Documents
      ↓
PyPDFLoader
      ↓
RecursiveCharacterTextSplitter
      ↓
HuggingFace Embeddings
      ↓
ChromaDB
      ↓
Retriever
      ↓
ChatHuggingFace
      ↓
Generated Answer


----------------------------------------------------------------------------------
Performance :

CPU-based inference
Local vector database
Semantic retrieval using embeddings
Context-aware answer generation


---------------------------------------------------------------------
Future Improvements : 

Hybrid retrieval
Sanskrit OCR support
Better multilingual models
Chat history memory
Reranking mechanisms


Author
PRITESH