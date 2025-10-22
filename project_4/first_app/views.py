from django.shortcuts import render

# Create your views here.
def home(request):
    # d={'Name':'Hossain','Id':'1011'}
    # return render(request,'first_app/home.html',context=d)
    return render(request, 'first_app/home.html', {'name':'Hossain','id':'01','Age':5 , 'lst':['Hossain','Kobir','Siddique'], 'courses': [
        {
            'id':1,
            'name':'Hossain',
            'sub':'Data Structure',
        },
        {
            'id':2,
            'name':'Kobir',
            'sub':'Algorith',
        },
        {
            'id':3,
            'name':'Siddique',
            'sub':'OOP',
        }
    ]})