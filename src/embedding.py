from langchain_text_splitters import RecursiveCharacterTextSplitter
from sentence_transformers import SentenceTransformer
import numpy as np
from src.data_loader import load_all_documents


class EmbeddingPipeline:
    def __init__(self, model_name: str = "all-MiniLM-L6-v2", chunk_size: int = 1000, chunk_overlap: int = 200):
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        self.model = SentenceTransformer(model_name)
        print(f"[INFO] Loaded embedding model: {model_name}")

    def chunk_documents(self, documents):
        """Split documents into smaller chunks for better RAG performance"""
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=self.chunk_size,
            chunk_overlap=self.chunk_overlap,
            length_function=len,
            separators=["\n\n", "\n", " ", ""]
        )
        chunks = text_splitter.split_documents(documents)
        print(f"[INFO] Split {len(documents)} documents into {len(chunks)} chunks")
        return chunks

    def embed_chunks(self, chunks):
        """Generate embeddings for a list of chunks"""
        texts = [chunk.page_content for chunk in chunks]
        print(f"[INFO] Generating embeddings for {len(texts)} texts...")
        embeddings = self.model.encode(texts, show_progress_bar=True)
        print(f"[INFO] Generated embeddings with shape: {embeddings.shape}")
        return embeddings

    def process(self, data_dir: str):
        """Full pipeline: load documents, split into chunks, generate embeddings"""
        documents = load_all_documents(data_dir)
        chunks = self.split_documents(documents)
        texts = [chunk.page_content for chunk in chunks]
        embeddings = self.generate_embeddings(texts)
        return chunks, embeddings


## Example usage:
# pipeline = EmbeddingPipeline()
# chunks, embeddings = pipeline.process(data_dir="data")