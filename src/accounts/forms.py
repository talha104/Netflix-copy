from django import forms
from django.contrib import messages

from .models import Register

class RegisterForm(forms.ModelForm):
	password 			= forms.CharField(widget=forms.PasswordInput)
	confirm_password 	= forms.CharField(widget=forms.PasswordInput)
	class Meta:
		model = Register
		fields = [
		'first_name',
		'last_name',
		'username',
		'email',
		'confirm_email',
		'password',
		'confirm_password']

	def clean(self, *args, **kwargs):
		password = self.cleaned_data.get("password")
		confirm_password = self.cleaned_data.get("confirm_password")
		email = self.cleaned_data.get("email")
		confirm_email = self.cleaned_data.get("confirm_email")
		if email != confirm_email and password != confirm_password:
			raise forms.ValidationError({
				'email': ["Email not allowed to change"],
				'confirm_email': ["Confirm email not allowed to change"],
				'password': ["Password not allowed to change"],
				'confirm_password': ["Confirm password not allowed to change"],})
		if password != confirm_password:
			raise forms.ValidationError({
				'password': ["Password not allowed to change"],
				'confirm_password': ["Confirm password not allowed to change"],})
		if email != confirm_email:
			if len(password) < 8:
				raise forms.ValidationError({
				'email': ["Email not allowed to change"],
				'confirm_email': ["Confirm email not allowed to change"],
				'password': ["Password is too short!"],})
			else:
				raise forms.ValidationError({
				'email': ["Email not allowed to change"],
				'confirm_email': ["Confirm email not allowed to change"],})
		if len(password) < 8:
			raise forms.ValidationError({
				'password': ["Password is too short!"]})

