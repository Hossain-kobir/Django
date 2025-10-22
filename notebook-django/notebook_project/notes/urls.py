from django.urls import path
from notes import views

app_name = "notes"
urlpatterns = [
    path('',views.home , name = 'index'),
    path('notes/',views.notes , name ='notes'),
    path('note/<int:note_id>',views.note ,name='note'),
]