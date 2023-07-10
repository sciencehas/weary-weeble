from django.db import models

class Document(models.Model):
    name = models.CharField(max_length=255)
    docfile = models.FileField(upload_to='documents/%Y/%m/%d')
    uploaded_at = models.DateTimeField(auto_now_add=True)

class Content(models.Model):
    document = models.ForeignKey(Document, on_delete=models.CASCADE)
    content = models.TextField()
    similarity_score = models.FloatField()
    is_duplicate = models.BooleanField(default=False)
    duplicate_count = models.IntegerField(default=0)

class Error(models.Model):
    document = models.ForeignKey(Document, on_delete=models.CASCADE)
    error_message = models.TextField()
