from django.shortcuts import render , redirect
from author.forms import Author_Form
# Create your views here.
def Add_Author(request):
    if request.method == 'POST':
        Author=Author_Form(request.POST)
        if Author.is_valid():
            Author.save()
            return redirect('add_author')
    
    Author=Author_Form()        
    return render(request,'add_author.html',{'form':Author})