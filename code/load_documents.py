from langchain_community.document_loaders.pdf import PyPDFLoader
import os

def load_documents(folder_path):
    documents=[]
    for file in os.listdir(folder_path):
        if file.endswith('.pdf'):
            file_path = os.path.join(folder_path,file)
            loader = PyPDFLoader(file_path)
            pdf_docs = loader.load()
            documents.extend(pdf_docs)
    return documents


    
        
     


