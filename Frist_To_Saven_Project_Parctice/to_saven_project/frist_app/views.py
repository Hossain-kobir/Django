from django.shortcuts import render
from frist_app.forms import Create_Account , StudentForm

# Create your views here.
def About_Page(request):
    if request.method == 'POST': 
        username=request.POST.get('username')
        email=request.POST.get('email')
        photo = request.FILES.get('file')
        return render(request,'frist_app/About.html',{'name':username,'email':email,'img':photo})


def Html_Form(request):
    return render(request,'frist_app/Html_Form.html')

def Django_Form_Api(request):
    if request.method == 'POST':
        form = Create_Account(request.POST,request.FILES)
        if form.is_valid():
            name = form.cleaned_data['name']
            roll = form.cleaned_data['roll']
            subs = form.cleaned_data['choice_Your_Subject']

            print(name)
            print(roll)
            print(subs)
            print(form.cleaned_data)
            
            file = form.cleaned_data['file']
            with open('./frist_app/upload/' + file.name,'wb+') as destination:
                for chunk in file.chunks():
                    destination.write(chunk)
                
            
            print(f'file name {file.name}')
            
        return render(request,'frist_app/Django_Form_Api.html',{'form':form})
    else:
        form = Create_Account(request.POST)
        return render(request,'frist_app/Django_Form_Api.html',{'form':form})

def Django_Model_Form(request):
    if request.method == 'POST':
        
        data=StudentForm(request.POST)
        if data.is_valid():
            data.save(commit=False)
            print(data.cleaned_data)
            return render(request,'frist_app/Django_Model_Form.html',{'form':data})

    else:
        data = StudentForm()
        return render(request,'frist_app/Django_Model_Form.html',{'form':data})