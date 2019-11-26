from django.db import models
from django import forms

# Create your models here.
class Register(models.Model):
	first_name			= models.CharField(max_length=150)
	last_name			= models.CharField(max_length=150)
	username			= models.CharField(max_length=150)
	email				= models.EmailField(max_length=150)
	confirm_email		= models.EmailField(max_length=150)
	password			= models.CharField(max_length=150)
	confirm_password	= models.CharField(max_length=150)