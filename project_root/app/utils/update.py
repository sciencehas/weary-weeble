from django.db import transaction
from .models import Document, Content

def update_document_content(document_id, new_content):
    with transaction.atomic():
        document = Document.objects.select_for_update().get(id=document_id)
        document.content = new_content
        document.save()

def delete_content(content_id):
    with transaction.atomic():
        content = Content.objects.select_for_update().get(id=content_id)
        document = content.document
        content.delete()
        document.content = "\n".join(c.text for c in document.content_set.all())
        document.save()

def add_content(document_id, text):
    with transaction.atomic():
        document = Document.objects.select_for_update().get(id=document_id)
        new_content = Content.objects.create(document=document, text=text)
        document.content += "\n" + new_content.text
        document.save()
