```python
from django import forms

class UploadFileForm(forms.Form):
    file_field = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}), label='Upload files')

class EditContentForm(forms.Form):
    content = forms.CharField(widget=forms.Textarea, label='Content')
```