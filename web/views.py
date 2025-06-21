from django.shortcuts import render
from django.views import View
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import CustomUserCreationForm
# Create your views here.

class Register(CreateView):
    form_class = CustomUserCreationForm
    template_name = "signup.html"
    success_url = reverse_lazy('login')

class HomeView(View):
    def get(self, request):
        return render(request, 'home.html')