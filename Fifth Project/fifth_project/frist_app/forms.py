from django import forms 
from django.core import validators

class Contact_form(forms.Form):
    name = forms.CharField(label ="User name",help_text="Please Write Your Full Name",required= False ,disabled=False,widget=forms.Textarea(attrs = {"placeholder":"Enter Your Name"}))
    email = forms.EmailField(label ="User email")
    # file = forms.FileField()
    # age = forms.IntegerField()
    # weight = forms.FloatField()
    # balance = forms.DecimalField()
    # check = forms.BooleanField()
    # birthday = forms.DateField()
    # appoinment = forms.DateTimeField()
    choose = [('s','small'),('L','Large'),('M','Medium')]
    size = forms.ChoiceField(choices=choose, widget = forms.RadioSelect())
        
    food = [("A","Apple"),("B","Banana"),("M","Mango")]
    eat = forms.MultipleChoiceField(choices = food)
    


# class Student_data(forms.Form):
#     name = forms.CharField()
#     email = forms.EmailField()

#     # def clean_name(self):
#     #     valname = self.cleaned_data['name']
#     #     if len(valname) < 10:
#     #         raise forms.ValidationError('Enter a valid name at least 10 character')
#     #     return valname
    
#     # def clean_email(self):
#     #     valemail = self.cleaned_data['email']
#     #     if '.mom' not in valemail and '&' not in valemail:
#     #         raise forms.ValidationError('Please Enter A Valid Email')
#     #     return valemail
    
#     def clean(self):
#         cleaned_data = super().clean()
#         valname = self.cleaned_data['name']
#         valemail = self.cleaned_data['email']
        
#         if len(valname) < 10:
#             raise forms.ValidationError('Enter name atleast 10 character')
        
#         if '.mom' not in valemail and '&' not in valemail:
#             raise forms.ValidationError('enter a vlid email adress')

def check_name(value):
    if len(value) < 10:
        raise forms.ValidationError('Please enter atleast 10 character')
    

class Student_data(forms.Form):
            name = forms.CharField(widget= forms.TextInput,validators=[check_name])
            email = forms.EmailField(validators=[validators.EmailValidator(message=('check validation email'))])
            age = forms.IntegerField(validators=[validators.MinValueValidator(20,message=('minmum value at least 20')),validators.MaxValueValidator(1000,message=('do not give value 1000'))])
            file = forms.FileField(validators=[validators.FileExtensionValidator(allowed_extensions=['pdf'],message=('only pdf file allowed'))])

class Password_Validation_Project(forms.Form):
    name = forms.CharField(label=('Full Name'))
    password = forms.CharField(widget = forms.PasswordInput)
    confirm_password = forms.CharField(widget = forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        frist_pass = self.cleaned_data['password']
        con_pass = self.cleaned_data['confirm_password']
        
        if con_pass != frist_pass :
            raise forms.ValidationError("Password does not match")