from django.http import HttpResponse
from django.shortcuts import render


# def home(request):
#     return HttpResponse("This is Home Page For Project 3 ")

def home(request):
    return render("request","index.html")

