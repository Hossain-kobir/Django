from django import forms
from frist_app.models import StudentModel

class StudentForm(forms.ModelForm):
    class Meta:
        model = StudentModel
        
        fields = "__all__"
        
        labels = {
            'name':'Full Name',
            'Roll':'ID',
            'father_name':'Father Name',
            'Adress':'Adress'
        }
        
        widgets = {
            'name':forms.TextInput(attrs={'class':'btn btn-primary'})
        }
        
        help_texts = {
            'name':'Please Enter Your Full Name',
            'Roll':'Please Enter Your class Id',
            'father_name':'Please Enter Father Name',
            'Adress':'Please Enter Your Full Adress',
        }
        
        error_messages = {
            'name':{'required':'You must entered your name'}
        }