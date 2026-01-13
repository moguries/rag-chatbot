from langchain_community.document_loaders import GoogleDriveLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
# from langchain_community.embeddings import HuggingFaceEmbeddings (deprecated)
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

FOLDER_ID = "1M86nx_y-v-uWc9c-EylmuxJTaoZ8bcca"
DB_PATH = "chroma_db"
EMBEDDING_MODEL = "all-MiniLM-L6-v2"

loader = GoogleDriveLoader(folder_id=FOLDER_ID)
documents = loader.load()
print(f"Loaded {len(documents)} documents from Google Drive")

splitter = RecursiveCharacterTextSplitter(
        chunk_size=300,
        chunk_overlap=50,
        separators=[
        "\n\n",
        "\n",
        ". ",
        " ",
        ""
        ]
    )
chunks = splitter.split_documents(documents)
print(f"Split documents into {len(chunks)} chunks")

# convert chunks to vectors (embeddings)
# vectors preserve semantic meaning: similar meaning = closer vectors (cosine similarity)
embeddings = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL)

# store in vector DB (vector -> text chunk -> metadata) so internal docs are queryable by semantics
vectorstore = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings,
    persist_directory=DB_PATH
)

print("Documents ingested successfully into Chroma")