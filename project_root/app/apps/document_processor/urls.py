```python
from django.urls import path
from . import views

app_name = 'document_processor'

urlpatterns = [
    path('', views.index, name='index'),
    path('upload/', views.upload_file, name='upload_file'),
    path('results/', views.process_documents, name='process_documents'),
]
```