from django.urls import path

from .views import first_app,Course
urlpatterns = [
    path("About_Page/",first_app),
    path("Course/",Course),

]