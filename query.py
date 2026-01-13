import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_chroma import Chroma
# from langchain_community.embeddings import HuggingFaceEmbeddings (deprecated)
from langchain_huggingface import HuggingFaceEmbeddings

EMBEDDING_MODEL = "all-MiniLM-L6-v2"
DB_PATH = "chroma_db"
LLM_MODEL = "llama-3.3-70b-versatile"
DISTANCE_THRESHOLD = 0.95
FAILED_RESPONSE = "This information is not present in any internal document."

load_dotenv()

llm = ChatGroq(
    temperature=0,
    api_key=os.getenv("LLM_API_KEY"),
    model=LLM_MODEL
)

prompt_template = PromptTemplate.from_template(
    """
    You are an internal company knowledge assistant.
    Answer questions ONLY using the provided context.
    Always cite the source document names.
    If the answer is not in the context, say {failed_response}.
    Do not cite any sources in that case.
    
    Context: {context}
    
    Question: {question}"""
)

embeddings = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL)

vectorstore = Chroma(
        persist_directory=DB_PATH,
        embedding_function=embeddings
    )

def answer_question(question: str):
    distances = vectorstore.similarity_search_with_score(question, k=3)

    # keep only documents whose distance is small enough (semantically similar to question)
    relevant_docs = [
        doc for doc, distance in distances
        if distance < DISTANCE_THRESHOLD
    ]

    if not relevant_docs:
        return FAILED_RESPONSE

    context = "\n\n".join(
        f"Source: {doc.metadata['source']}\n{doc.page_content}"
        for doc in relevant_docs
    )

    prompt = prompt_template.format(
        failed_response=FAILED_RESPONSE,
        context=context,
        question=question)
    
    response = llm.invoke(prompt)
    return response.content