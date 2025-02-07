"""
source for code: https://www.perplexity.ai/search/i-need-to-use-llm-model-to-lea-9y_Ve1y4Sw.vg_6YAgn3jQ
youtube video LangChain: https://www.youtube.com/watch?v=8BV9TW490nQ&t=10s
"""


import os
from langchain_chroma import Chroma
from openai import OpenAI
from chromadb.config import Settings
from dotenv import load_dotenv
from langchain.tools import tool
from langchain_text_splitters.python import PythonCodeTextSplitter
from langchain_core.documents import Document
from langchain.embeddings import HuggingFaceEmbeddings

load_dotenv()


class ChromaTools:

    def create_documents_from_content_files(self, content_files_list: str) -> list:
        """
        create documents from the content of python files retrieved in the repo
        These documents are ready to be loaded in Chroma
        :return: list of Documents
        """
        documents = []
        for content in content_files_list:
            text_splitter = PythonCodeTextSplitter(
                chunk_size=1000,
                chunk_overlap=200
            )
            chunks = text_splitter.split_text(content)
            docs = [Document(page_content=chunk) for i, chunk in enumerate(chunks)]
            [documents.append(item) for item in docs]

        return documents

    @tool("save files into the vectorized database")
    def save(self, content_files_list: str) -> list:
        """
        Save all the code from the list of files into a vectorized database
        :param files_list: list of all the python files to save.
        :return: data saved in the database
        """
        docs = self.create_documents_from_content_files(content_files_list)

        vector_db = Chroma(
            collection_name="python_codebase",
            embedding_function=HuggingFaceEmbeddings(),
            client_settings=Settings(
                chroma_db_impl="duckdb+parquet",
                persist_directory="./chroma_db"
            )
        )

        vector_db.add_documents(
            documents=docs,
            ids=[f"doc_{i}" for i in range(len(docs))]
        )