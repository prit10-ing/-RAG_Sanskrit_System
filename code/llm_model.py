from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv


load_dotenv()

parser = StrOutputParser()

llm  = HuggingFaceEndpoint(
    repo_id="openai/gpt-oss-120b:groq",

    task="text-generation",

    max_new_tokens=400,

    temperature=0.3)


model = ChatHuggingFace(llm=llm)


def genrate_answer(promt):
    chain = model | parser
    result = chain.invoke(promt)
    return result