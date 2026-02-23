from django import forms
from author.models import Author
class Author_Form(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'