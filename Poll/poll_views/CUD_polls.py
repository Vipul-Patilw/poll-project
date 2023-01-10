from django.views.generic.edit import CreateView,UpdateView
from Poll.forms import CreatePollForm
from django.urls import reverse_lazy
from Poll.models import Poll
from django.utils import timezone
import datetime
from django.contrib.auth.mixins import LoginRequiredMixin
class CreatePollView(LoginRequiredMixin,CreateView,):
	template_name = "create-poll.html"
	form_class = CreatePollForm
	success_url = reverse_lazy("home")

	
class UpdatePoll(LoginRequiredMixin,UpdateView):
	template_name = "create-poll.html"
	model = Poll
	form_class = CreatePollForm
	success_url = reverse_lazy("personal_detail")
	def form_valid(self, form):
			form.clean()
			return super(UpdatePoll, self).form_valid(form)
	