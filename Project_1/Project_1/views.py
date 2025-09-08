from django.http import HttpResponse
import datetime

def contact(request):
    return HttpResponse("This Is Contact Page")

def Home(request):
    return HttpResponse("This Is Home Page")