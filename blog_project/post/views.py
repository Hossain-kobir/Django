from django.shortcuts import render,redirect
from post.forms import Post_form
from .import models
# Create your views here.

def add_post(request):
    if request.method == 'POST':
        Post_Form = Post_form(request.POST)
        if Post_Form.is_valid():
            Post_Form.save()
            return redirect('add_post')
    
    Post_Form=Post_form()
    return render(request,'add_post.html',{'Post_Form':Post_Form})


def edit_post(request,id):
    post=models.Post.objects.get(pk=id)
    Post_Form = Post_form(instance=post)
    if request.method == 'POST':
        Post_Form = Post_form(request.POST,instance=post)
        if Post_Form.is_valid():
            Post_Form.save()
            return redirect('homepage')
    
    
    return render(request,'add_post.html',{'Post_Form':Post_Form})

def delete_post(request,id):
    post = models.Post.objects.get(pk=id)
    post.delete()
    return redirect('homepage')