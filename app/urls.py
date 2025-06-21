from django.urls import path
from app.views import HomeView, LoginView, SignupView

urlpatterns = [
    path('home/', HomeView.as_view(), name='home'),
    path('login/', LoginView.as_view(), name='login'),
    path('signup/', SignupView.as_view(), name='login'),
]
