from Poll.models import UserRegistration
import re
from PollProject import settings
from django import forms
import datetime
from django.core.exceptions import ValidationError
from django_flatpickr.widgets import DatePickerInput
from django.template.loader import render_to_string
from django.core.mail import EmailMessage  
    
from mailqueue.models import MailerMessage
          
class UserCreateForm(forms.ModelForm):
	gender=(('Male','Male'),('Female','Female'),('Other','Other'))
	password = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'type':'password','class':'form-control'}))
	confirm_password = forms.CharField(label=' Re-enter Password',widget=forms.PasswordInput(attrs={'type':'password','class':'form-control'}))
	gender = forms.ChoiceField(choices=gender, widget=forms.RadioSelect())

	def __init__(self, *args, **kwargs):
			super(UserCreateForm, self).__init__(*args, **kwargs)
			self.fields['profile_pic'].required = False
			

	class Meta:
		model = UserRegistration
		date = datetime.date.today()
		fields = '__all__'
		labels = {
		'first_name': 'First Name',
		
		'last_name':'Last Name',
		
		'mobile_number':'Mobile Number',
			
		'email':'Email',
		
		'gender':'Gender',
	
	}
		widgets = {
				'mobile_number':forms.TextInput(attrs={'type':'tel','maxlength':10,'id':'phone','onkeyup':'phoneValidation()','class':'form-control'}),
				'email':forms.EmailInput(attrs={'type':'email','class':'form-control'}),
				'first_name':forms.TextInput(attrs={'type':'text','class':'form-control'}),
					'last_name':forms.TextInput(attrs={'type':'text','class':'form-control'}),
						'username':forms.TextInput(attrs={'type':'text','class':'form-control'}),
	
					'gender':forms.RadioSelect(attrs={'class':'inline'}),
						'type':forms.Select(attrs={'class':'form-select'}),
			
					
				'profile_pic':forms.FileInput(attrs={'id':"file" , 'style':"display: none"})}
	def clean(self):
		first_name= self.cleaned_data['first_name']
		last_name= self.cleaned_data['last_name']
		mobile_number= self.cleaned_data['mobile_number']
		email = self.cleaned_data['email']
		password= self.cleaned_data['password']
		password2 = self.cleaned_data['confirm_password']
		
		if UserRegistration.objects.filter(email=email).exclude(pk=self.instance.pk).exists():
						raise ValidationError({'email':"this email address already registered with us try different email address"})
		if UserRegistration.objects.filter(mobile_number=mobile_number).exclude(pk=self.instance.pk).exists():
						raise ValidationError({'mobile_number':"this mobile number is already registered with us try different mobile number"})
		if len(mobile_number) != 10:
				raise ValidationError({'mobile_number':"please enter a valid 10 digit number"})
		if not re.search(r"@",email):
			raise ValidationError({'email':"Please enter valid email id"})
		if self.instance.pk:
			pass
		else:
						if len(password)<=16 and re.search(r"[a-z]",password) and re.search(r"[0-9]",password):
							pass
						else:
							raise ValidationError({'password':"password should not be greater than 16 character. and should contain numeric value"})
						if password != password2:
							raise ValidationError({'confirm_password':"confirm password doesn't matched with the password"})
						#Using mailqueue method
						my_email = "bankingsolutions701@gmail.com"
						my_name = "Banking Solutions"
						content = f"""
Dear {first_name} {last_name},

Your account is created successfully.


Thanks,
Poll Application
"""
						msg = MailerMessage()
						msg.subject = "Welcome To Poll Application "
						msg.to_address = email
						msg.from_address = '{} <{}>'.format(my_name, my_email)
						msg.content = content
						msg.html_content = content
						msg.sent = True
						msg.save()
	


			
				
	
		