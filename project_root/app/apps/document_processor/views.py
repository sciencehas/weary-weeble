```python
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Document
from .utils import cleaning, ranking, vectorization, merging, similarity, transformer

def index(request):
    documents = Document.objects.all()
    return render(request, 'document_processor/index.html', {'documents': documents})

def upload(request):
    if request.method == 'POST':
        uploaded_files = request.FILES.getlist('documents')
        if not uploaded_files:
            messages.error(request, 'No file selected.')
            return redirect('index')
        for file in uploaded_files:
            document = Document(file=file)
            document.save()
            messages.success(request, f'{file.name} uploaded successfully.')
        return redirect('process_documents')
    return render(request, 'document_processor/upload.html')

def process_documents(request):
    documents = Document.objects.all()
    for document in documents:
        content = document.file.read().decode('utf-8')
        cleaned_content = cleaning.clean(content)
        ranked_content = ranking.rank(cleaned_content)
        vectorized_content = vectorization.vectorize(ranked_content)
        merged_content = merging.merge(vectorized_content)
        similarity_results = similarity.calculate(merged_content)
        document.processed_content = transformer.ingest(similarity_results)
        document.save()
    messages.success(request, 'Documents processed successfully.')
    return redirect('results')

def results(request):
    documents = Document.objects.all()
    return render(request, 'document_processor/results.html', {'documents': documents})

def delete_document(request, document_id):
    document = Document.objects.get(id=document_id)
    document.delete()
    messages.success(request, 'Document deleted successfully.')
    return redirect('index')

def update_document(request, document_id):
    if request.method == 'POST':
        document = Document.objects.get(id=document_id)
        new_content = request.POST.get('content')
        document.file.save(new_content)
        document.save()
        messages.success(request, 'Document updated successfully.')
        return redirect('index')
    return render(request, 'document_processor/update.html', {'document': document})
```