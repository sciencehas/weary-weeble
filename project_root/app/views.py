from django.shortcuts import render, redirect
from .forms import UploadFileForm
from .models import Document
from .utils.transformers import ingest_document
from .utils.cleaning import clean_data
from .utils.vectorization import create_word_vector
from .utils.similarity import calculate_similarity
from .utils.update import update_document
from .utils.create_document import create_new_document

def index(request):
    documents = Document.objects.all()
    return render(request, 'app/index.html', {'documents': documents})

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile=request.FILES['docfile'])
            newdoc.save()

            # Ingest document into db
            ingest_document(newdoc.docfile.path)

            return redirect('index')
    else:
        form = UploadFileForm()
    return render(request, 'app/upload.html', {'form': form})

def view_document(request, doc_id):
    document = Document.objects.get(id=doc_id)
    return render(request, 'app/view.html', {'document': document})

def edit_document(request, doc_id):
    document = Document.objects.get(id=doc_id)
    if request.method == 'POST':
        # Update document
        update_document(document, request.POST['content'])
        return redirect('view', doc_id=document.id)
    return render(request, 'app/edit.html', {'document': document})

def process_documents(request):
    documents = Document.objects.all()
    for document in documents:
        # Clean data
        cleaned_data = clean_data(document.content)
        # Create word vector
        word_vector = create_word_vector(cleaned_data)
        # Calculate similarity
        similarity = calculate_similarity(word_vector)
        # Update document with similarity
        document.similarity = similarity
        document.save()
    return redirect('index')

def create_new(request):
    documents = Document.objects.filter(similarity__gte=0.5)
    # Create new document from remaining text
    new_document = create_new_document(documents)
    return redirect('view', doc_id=new_document.id)
