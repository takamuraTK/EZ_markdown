from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm
from django.views import generic
from django.urls import reverse_lazy

class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'

@login_required
def home(request):
    return render(request, 'accounts/home.html')