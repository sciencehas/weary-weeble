from django.urls import path
from .apps.document_processor import views

urlpatterns = [
    path('', views.index, name='index'),
    path('upload/', views.upload_file, name='upload_file'),
    path('results/', views.process_documents, name='process_documents'),
]
