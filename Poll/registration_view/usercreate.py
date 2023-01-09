from django.views.generic.edit import CreateView
from django.contrib.messages.views import  SuccessMessageMixin
from Poll.forms import UserCreateForm
from Poll.models import  UserRegistration
from django.contrib.auth.models import User

from django.urls import reverse_lazy
class UserCreate(CreateView):

		model = UserRegistration
		template_name = 'registration/user_registration.html'
		form_class = UserCreateForm
		success_url = reverse_lazy('login')
		def form_valid(self, form):
			first_name= form.cleaned_data['first_name']
			last_name= form.cleaned_data['last_name']
			email = form.cleaned_data['email']
			password= form.cleaned_data['password']
			myuser = User.objects.create_user(email,email,password)
			myuser.first_name = first_name
			myuser.last_name = last_name
			myuser.save()
			return super(UserCreate, self).form_valid(form)