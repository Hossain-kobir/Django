from django.urls import path
from frist_app.views import Html_Form,Django_Form_Api,Django_Model_Form,About_Page
urlpatterns = [
    path('Html_Form/',Html_Form, name='H_Form'),
    path('About/',About_Page, name='A_Page'),
    path('Django_Form/',Django_Form_Api, name='D_Form_Api'),
    path('Django_Model/',Django_Model_Form, name='D_Model_Form'),
    path('Django_Model/',About_Page, name='A_Page'),
]
