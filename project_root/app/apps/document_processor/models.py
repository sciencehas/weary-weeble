from django.db import models

class Document(models.Model):
    docfile = models.FileField(upload_to='documents/%Y/%m/%d')
    processed = models.BooleanField(default=False)
    upload_date = models.DateTimeField(auto_now_add=True)

class Content(models.Model):
    document = models.ForeignKey(Document, on_delete=models.CASCADE)
    content = models.TextField()
    similarity_score = models.FloatField()
    duplicate = models.BooleanField(default=False)

class DuplicateContent(models.Model):
    content = models.ForeignKey(Content, on_delete=models.CASCADE)
    duplicate_count = models.IntegerField(default=0)
    documents = models.ManyToManyField(Document)
