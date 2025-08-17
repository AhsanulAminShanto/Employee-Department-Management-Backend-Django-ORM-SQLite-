from django.shortcuts import render

# Create your views here.
# accounts/views.py
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import SignupForm

class SignupView(CreateView):
    form_class = SignupForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')
