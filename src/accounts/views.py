from django.shortcuts import render
from django.views.generic import CreateView
from django import forms

from .models import Register
from .forms import RegisterForm

class RegisterCreate(CreateView):
	template_name = 'accounts/signup.html'
	form_class = RegisterForm
	success_url = '../pages/home/'

	def register(request):
	    email = request.POST['email']
	    confirm_email = request.POST['confirm_email']
	    password = request.POST['password']
	    confirm_password = request.POST['confirm_password']
	    if email != confirm_email:
	    	raise forms.ValidationError("Emails are not the same!")
	    if password != confirm_password:
	    	raise forms.ValidationError("Passwords are not the same!")