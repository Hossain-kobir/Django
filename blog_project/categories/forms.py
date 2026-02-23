from django import forms
from categories.models import Category

class Category_Form(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'