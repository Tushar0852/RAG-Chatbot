from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.chains import create_history_aware_retriever, create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from typing import List
from langchain_core.documents import Document
import os
from chroma_utils import vectorstore
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retriever setup
retriever = vectorstore.as_retriever(search_kwargs={"k": 2})
output_parser = StrOutputParser()

# Prompts
contextualize_q_system_prompt = (
    "Given a chat history and the latest user question "
    "which might reference context in the chat history, "
    "formulate a standalone question which can be understood "
    "without the chat history. Do NOT answer the question, "
    "just reformulate it if needed and otherwise return it as is."
)

contextualize_q_prompt = ChatPromptTemplate.from_messages([
    ("system", contextualize_q_system_prompt),
    MessagesPlaceholder("chat_history"),
    ("human", "{input}"),
])

qa_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful AI assistant. Use the following context to answer the user's question."),
    ("system", "Context: {context}"),
    MessagesPlaceholder(variable_name="chat_history"),
    ("human", "{input}")
])

# RAG Chain function
def get_rag_chain(model="gemini-2.5-flash"):
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        raise ValueError("GOOGLE_API_KEY not found. Please set it in your .env file.")

    # Gemini LLM with API key
    llm = ChatGoogleGenerativeAI(
        model=model,
        api_key=api_key,   # ✅ Corrected here
        temperature=0
    )

    # History-aware retriever
    history_aware_retriever = create_history_aware_retriever(
        llm,
        retriever,
        contextualize_q_prompt
    )

    # QA chain
    question_answer_chain = create_stuff_documents_chain(llm, qa_prompt)

    # Full RAG pipeline
    rag_chain = create_retrieval_chain(history_aware_retriever, question_answer_chain)

    return rag_chain
