from django.urls import path
from .views import home,delete

urlpatterns = [
    path('',home,name="home_page"),
    path('delete/<int:id>',delete,name="data_delete"),
]