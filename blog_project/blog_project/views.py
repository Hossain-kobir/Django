from django.shortcuts import render
from post.models import Post

def home(request):
    
    data = Post.objects.all()
    print(data)
    for i in data:
        print(i)
        # print(i.title)
        for j in i.Category.all() :
            print(f"From J :{j.name}")

    return render(request,'home.html',{'data':data})