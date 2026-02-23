from django.shortcuts import render,redirect
from profiles.forms import Profile_form
# Create your views here.
def Add_Profile(request):
    if request.method == 'post':
        Profile_Form= Profile_form(request.POST)
        if Profile_Form.is_valid():
            Profile_Form.save()
            return redirect('add_profile')
    
    Profile_Form=Profile_form()
    return render(request,'add_profile.html',{'Profile_Form': Profile_Form})