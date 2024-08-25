from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'published_date', 'isbn', 'summary']
        widgets = {
            'summary': forms.Textarea(attrs={'rows': 4}),
        }

    def clean_isbn(self):
        isbn = self.cleaned_data.get('isbn')
        if not isbn.isdigit():
            raise forms.ValidationError("ISBN should only contain digits.")
        return isbn

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get('title')

        # Example validation: Ensure the title doesn't contain malicious content
        if "<script>" in title:
            self.add_error('title', "Invalid title content.")
        
        return cleaned_data
