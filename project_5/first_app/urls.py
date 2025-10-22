from django.urls import path
from . import views

urlpatterns = [
    path('app/',views.about, name='about'),
    path('contact/',views.contact , name='contact'),
    

]