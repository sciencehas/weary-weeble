
from sentence_transformers import SentenceTransformer
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from .models import Document
import os

def ingest_documents(file):
    model = SentenceTransformer('stsb-mpnet-base-v2')
    file_path = default_storage.save('tmp/'+file.name, ContentFile(file.read()))
    tmp_file = os.path.join(settings.MEDIA_ROOT, file_path)

    with open(tmp_file, 'r') as f:
        content = f.read()
        sentences = content.split('.')
        embeddings = model.encode(sentences)

    os.remove(tmp_file)

    for i, sentence in enumerate(sentences):
        doc = Document(content=sentence, embedding=embeddings[i])
        doc.save()

    return True
