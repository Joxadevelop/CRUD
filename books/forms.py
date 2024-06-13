from django import forms
from .models import BookCategory, Books
from ckeditor.widgets import CKEditorWidget


class CategoryForm(forms.ModelForm):
    body = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = BookCategory
        fields = ["name", "description"]
        
        
class BookForm(forms.ModelForm):
    body = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Books
        fields = ["name", "slug", "picture", "price", "quantitiy", "status", "category"]