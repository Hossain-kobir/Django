from django.shortcuts import render
from frist_app.forms import StudentForm

def home(request):
    if request.method == "POST":
        data = StudentForm(request.POST)
        if data.is_valid():
            data.save()
            print(data.cleaned_data)
            context = {'form':data}
            return render(request,'home.html',context)
    
    else:
        data=StudentForm()
        context = {'form':data}
        return render(request,'home.html',context)