
from code.llm_model import genrate_answer
from code.load_documents import load_documents
from code.text_spliter import split_documents
from code.vectore_store import create_vector_store
from code.retriever import create_retriever
import streamlit as st
import time
import psutil

st.title("Sanskrit RAG System")

st.write("Welcome to the Sanskrit RAG System! Ask any question related to Sanskrit, and I'll do my best to provide you with an answer based on the documents I've been trained on.")

@st.cache_resource
def initialize_system():

    documents = load_documents('Data')

    chunks = split_documents(documents)

    vector_db = create_vector_store(chunks)

    retriever = create_retriever(vector_db)

    return retriever

retriever = initialize_system()

query = st.text_input("Enter your question")


if st.button('Ask'):
    if query:
        start_time = time.time()
        relevant_docs = retriever.invoke(query)

        context = ""

        for i in relevant_docs:
            context += i.page_content + "\n"

        prompt = f"""

You are a Sanskrit question-answering assistant.

Answer ONLY from the provided context.

If the answer is not present in the context, say:
"Answer not found in context."

Context:
{context}

Question:
{query}

Answer:
"""


        # Generate answer
        answer = genrate_answer(prompt)
        end_time = time.time()
        latency = end_time - start_time


        st.write(f"Response Time: {latency:.2f} seconds")

        cpu_usage = psutil.cpu_percent()

        st.write(f"CPU Usage: {cpu_usage}%")



        # Show answer
        st.subheader("Answer")

        st.write(answer)   
