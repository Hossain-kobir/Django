from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home_page'),
    path('about/',views.about,name='about_page'),
    path('from/',views.submit_from,name='from_page'),
    # path('djangoform/',views.Student_form,name='djangoform'),
    path('djangoform/',views.Password_validation_Projects,name='djangoform'),
]