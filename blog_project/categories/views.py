from django.shortcuts import render,redirect
from categories.forms import Category_Form
# Create your views here.

def Add_Categories(request):
    if request.method == 'POST':
        category_form = Category_Form(request.POST)
        if category_form.is_valid():
            category_form.save()
            return redirect('add_categories')
    category_form=Category_Form()
    return render(request,'add_category.html',{'category_form':category_form})