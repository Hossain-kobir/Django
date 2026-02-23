from django.urls import path
from frist_app.views import home , signup ,login_page , profile , user_logout,pass_change
urlpatterns = [
    path("",home,name="HomePage"),
    path("signup/",signup,name="signup_page"),
    
    path("login/",login_page,name="login_page"),
    
    path("profile/",profile, name="profile"),
    path("logout/",user_logout, name="logout"),
    path("passchange",pass_change, name="pass_change")
    
]