from sentence_transformers import SentenceTransformer
from django.core.files.storage import default_storage
from .models import Document
import os

class DocumentTransformer:
    def __init__(self):
        self.model = SentenceTransformer('stsb-mpnet-base-v2')

    def ingest_documents(self, uploaded_files):
        for uploaded_file in uploaded_files:
            file_path = default_storage.save(uploaded_file.name, uploaded_file)
            with default_storage.open(file_path, 'r') as file:
                content = file.read()
                embeddings = self.model.encode([content])
                Document.objects.create(name=uploaded_file.name, content=content, embeddings=embeddings)
            os.remove(file_path)

This code creates a class `DocumentTransformer` that uses the `stsb-mpnet-base-v2` model from the `sentence_transformers` library to ingest documents. The `ingest_documents` method takes a list of uploaded files, saves each file temporarily, reads its content, encodes the content into embeddings using the transformer model, creates a new `Document` object with the file name, content, and embeddings, and finally deletes the temporary file.
