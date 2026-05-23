# No external imports are required in this module at the moment.

from langchain_chroma import Chroma

from langchain_community.embeddings import HuggingFaceEmbeddings
    

embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
)

def create_vector_store(chunks):
    vector_db = Chroma.from_documents(
        documents=chunks,
        embedding=embedding_model,
        persist_directory="vector_db"
    )
    return vector_db