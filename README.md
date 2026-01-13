# RoboQuery: Retrieval-Augmented Generation (RAG) System

## Introduction

RoboQuery is a RAG-powered Internal Knowledge Assistant which aims to answer employees' questions regarding internal company policies.

RoboQuery provides answers strictly based on internal company documents stored in Google Drive.

## Process Overview
The pipeline is as follows:
1. Documents are loaded from Google Drive
2. Text is split into chunks and converted into vector embeddings
3. Embeddings are stored in ChromaDB (persistent vector database)
4. User question is semantically compared to chunks to identify relevant documents
5. LLM answers questions only using retrieved context

## Stack
**Core AI / NLP**
- LangChain
- HuggingFace embeddings (all-MiniLM-L6-v2)
- Groq (LLaMA 3.3 70B)

**Vector Database**
- ChromaDB

**Document Ingestion**
- GoogleDriveLoader (LangChain Community)
- Google Drive API
- Google Auth / OAuth

**Frontend**
- StreamLit

**Utilities**
- python-dotenv

## Demo

https://github.com/user-attachments/assets/3dc040f3-b0a8-481b-aa0b-5d5cbe1665f0

## Why Retrieval-Augmented Generation (RAG)?

RAG is a technique that optimises LLM performance by connecting it to an external knowledge base, allowing it to semantically search for specific information within the database before generating a context-aware answer.

This technique is widely used in powering Internal Knowledge Assistants like RoboQuery. It enhances AI usage safety and hallucination reduction.

## Future Improvements
- Metadata filtering (eg. by department / policy type)
- Semantic caching for similar user queries (skip RAG pipeline and provide cached response)

## Acknowledgements & References
This project was built by learning from many amazing resources. Endless gratitude to:

**Youtube Tutorials**
- [codebasics - Gen AI Project Using Llama3.1 | End to End Gen AI Project](https://youtu.be/CO4E_9V6li0?si=j_aedxsSdcKpD6sn)
- [Greg Kamradt - LangChain101: Connect Google Drive Files To OpenAI](https://youtu.be/IqqHqDcXLww?si=9jTLoqbw38jG9fSB)

**Open Source Projects**
- [umbertogriffo - rag-chatbot](https://github.com/umbertogriffo/rag-chatbot.git)

**Documentation**
- [LangChain](https://docs.langchain.com/)