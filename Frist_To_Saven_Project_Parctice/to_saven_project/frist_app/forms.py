from django import forms
from django.core import validators
from frist_app.models import StudentModel

class Create_Account(forms.Form):
    name = forms.CharField()
    roll = forms.IntegerField()
    sub = [('C','CSE'),('E','EEE'),('P','PHY')]
    choice_Your_Subject = forms.MultipleChoiceField(choices=sub,widget=forms.CheckboxSelectMultiple)
    file = forms.FileField(validators=[validators.FileExtensionValidator(allowed_extensions=['pdf'],message="Please Upload Only PDF File")])

class StudentForm(forms.ModelForm):
    class Meta:
        model = StudentModel
        
        fields = '__all__'
        widgets = {
            'name':forms.TextInput(attrs={'class':'btn btn-primary'})
        }