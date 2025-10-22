from django.urls import path
from .views import app_home,course_Page,home

urlpatterns = [
    path("home/",app_home),
    path("course_page/",course_Page),
    path("",home)
]
