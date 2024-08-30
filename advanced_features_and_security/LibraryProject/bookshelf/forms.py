from django import forms
from .models import Book, ExampleModel

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year']
        widgets = {
            'publication_year': forms.NumberInput(attrs={'min': 1900, 'max': 2100}),
        }

    def clean_publication_year(self):
        year = self.cleaned_data.get('publication_year')
        if year < 1900 or year > 2100:
            raise forms.ValidationError("Publication year must be between 1900 and 2100.")
        return year

class ExampleForm(forms.ModelForm):
    class Meta:
        model = ExampleModel
        fields = ['user']

    def clean_user(self):
        user = self.cleaned_data.get('user')
        if not user:
            raise forms.ValidationError("User field cannot be empty.")
        return user
