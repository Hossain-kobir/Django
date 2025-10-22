from django.http import HttpResponse

from django.shortcuts import render

# Create your views here.
def app_home(request):
    return HttpResponse("Here Is Your App Response")


def course_Page(request):
    return HttpResponse("Here is your Course List")

def home(reques):
    return render('request','first_app/home.html')

