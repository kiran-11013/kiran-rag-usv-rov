from pathlib import Path
from typing import List, Any
from langchain_community.document_loaders import PyPDFLoader, TextLoader, CSVLoader
from langchain_community.document_loaders import Docx2txtLoader
from langchain_community.document_loaders.excel import UnstructuredExcelLoader
from langchain_community.document_loaders import JSONLoader


def load_all_documents(data_dir: str) -> List[Any]:
    """
    Load all supported files from the data directory and convert to LangChain document structure.
    Supported: PDF, TXT, CSV, Excel, Word, JSON, SQL
    """
    data_path = Path(data_dir).resolve()
    print(f"[DEBUG] Data path: {data_path}")
    documents = []

    # PDF files
    pdf_files = list(data_path.glob('**/*.pdf'))
    print(f"[DEBUG] Found {len(pdf_files)} PDF files: {[str(f) for f in pdf_files]}")
    for pdf_file in pdf_files:
        print(f"[DEBUG] Loading PDF: {pdf_file}")
        try:
            loader = PyPDFLoader(str(pdf_file))
            documents.extend(loader.load())
        except Exception as e:
            print(f"[ERROR] Failed to load {pdf_file}: {e}")

    # TXT files
    txt_files = list(data_path.glob('**/*.txt'))
    print(f"[DEBUG] Found {len(txt_files)} TXT files: {[str(f) for f in txt_files]}")
    for txt_file in txt_files:
        print(f"[DEBUG] Loading TXT: {txt_file}")
        try:
            loader = TextLoader(str(txt_file), encoding='utf-8')
            documents.extend(loader.load())
        except Exception as e:
            print(f"[ERROR] Failed to load {txt_file}: {e}")

    # CSV files
    csv_files = list(data_path.glob('**/*.csv'))
    print(f"[DEBUG] Found {len(csv_files)} CSV files: {[str(f) for f in csv_files]}")
    for csv_file in csv_files:
        print(f"[DEBUG] Loading CSV: {csv_file}")
        try:
            loader = CSVLoader(str(csv_file))
            documents.extend(loader.load())
        except Exception as e:
            print(f"[ERROR] Failed to load {csv_file}: {e}")

    # Word files
    docx_files = list(data_path.glob('**/*.docx'))
    print(f"[DEBUG] Found {len(docx_files)} DOCX files: {[str(f) for f in docx_files]}")
    for docx_file in docx_files:
        print(f"[DEBUG] Loading DOCX: {docx_file}")
        try:
            loader = Docx2txtLoader(str(docx_file))
            documents.extend(loader.load())
        except Exception as e:
            print(f"[ERROR] Failed to load {docx_file}: {e}")

    # Excel files
    excel_files = list(data_path.glob('**/*.xlsx')) + list(data_path.glob('**/*.xls'))
    print(f"[DEBUG] Found {len(excel_files)} Excel files: {[str(f) for f in excel_files]}")
    for excel_file in excel_files:
        print(f"[DEBUG] Loading Excel: {excel_file}")
        try:
            loader = UnstructuredExcelLoader(str(excel_file), mode="elements")
            documents.extend(loader.load())
        except Exception as e:
            print(f"[ERROR] Failed to load {excel_file}: {e}")

    # JSON files
    json_files = list(data_path.glob('**/*.json'))
    print(f"[DEBUG] Found {len(json_files)} JSON files: {[str(f) for f in json_files]}")
    for json_file in json_files:
        print(f"[DEBUG] Loading JSON: {json_file}")
        try:
            loader = JSONLoader(file_path=str(json_file), jq_schema=".", text_content=False)
            documents.extend(loader.load())
        except Exception as e:
            print(f"[ERROR] Failed to load {json_file}: {e}")

    # SQL files
    sql_files = list(data_path.glob('**/*.sql'))
    print(f"[DEBUG] Found {len(sql_files)} SQL files: {[str(f) for f in sql_files]}")
    for sql_file in sql_files:
        print(f"[DEBUG] Loading SQL: {sql_file}")
        try:
            loader = TextLoader(str(sql_file), encoding='utf-8')
            documents.extend(loader.load())
        except Exception as e:
            print(f"[ERROR] Failed to load {sql_file}: {e}")

    print(f"[DEBUG] Total documents loaded: {len(documents)}")
    return documents