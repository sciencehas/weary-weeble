```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('upload/', views.upload, name='upload'),
    path('view/<int:doc_id>/', views.view, name='view'),
    path('edit/<int:doc_id>/', views.edit, name='edit'),
]
```