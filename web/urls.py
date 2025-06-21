from web.views import *
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', LoginView.as_view(template_name="login.html"), name="login"),
    path('logout/', LogoutView.as_view(next_page='login'), name="logout"),
    path('register/', Register.as_view(), name="register"),
    path('home/', HomeView.as_view(), name="home"), 
]