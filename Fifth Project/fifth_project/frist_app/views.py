from django.shortcuts import render
from . forms import Contact_form , Student_data , Password_Validation_Project
# Create your views here.
def about(request):
    if request.method == "POST":
        name = request.POST.get("username")
        email = request.POST.get("email")
        return render(request,'frist_app/about.html',{'cname':name,'cemail':email})
    else:    
        return render(request,'frist_app/about.html')

def home(request):
    return render(request,'frist_app/home.html')

def submit_from(request):
    #print(request.POST)
    return render(request,'frist_app/from.html')

def Django_form(request):
    if request.method == "POST":
        form = Contact_form(request.POST,request.FILES)
        if form.is_valid():
            file = form.cleaned_data['file']
            with open("./frist_app/upload/" + file.name, "wb+") as destination:
                for chunk in file.chunks():
                    destination.write(chunk)
            print(form.cleaned_data)
            print(file.name)
        

    else:
        form = Contact_form()
        return render(request,"frist_app/djangoform.html",{"form":form})

def Student_form(request):
    if request.method == "POST":
        form = Student_data(request.POST,request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
            file = form.cleaned_data['file']
            print(file.name)
        return render(request,"frist_app/djangoform.html",{"form":form})
        
    else:
        form = Student_data()
        return render(request,"frist_app/djangoform.html",{"form":form})

def Password_validation_Projects(request):
    if request.method == "POST":
        form = Password_Validation_Project(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
        return render(request,'frist_app/djangoform.html',{"form":form})
    
    else:
        form = Password_Validation_Project()
        return render(request,'frist_app/djangoform.html',{"form":form})