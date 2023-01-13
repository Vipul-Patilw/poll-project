from django.views.generic import ListView,DetailView
from Poll.models import Poll
from django.utils import timezone
from django.shortcuts import  render,redirect,HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin

class PollsList(LoginRequiredMixin,ListView,):
	model = Poll
	context_object_name = "poll_list"
	ordering = ["-total"]
	def get_queryset(self):
	   polls = Poll.objects.all()
	   for poll in polls:
	           	if poll.expiration_date < timezone.now():
	           		poll.delete()
	   return super(PollsList,self).get_queryset()
	
		
class PollDetail(LoginRequiredMixin,DetailView):
	model = Poll
	context_object_name = "poll"	
	
def voting(request,poll_pk):
		if request.user.is_anonymous:
			return redirect('login')
		poll = Poll.objects.get(pk=poll_pk)
		if request.method == "POST":
			submit_option = request.POST.get('poll')
			if submit_option == "op1":
				poll.option_one_count += 1
			elif submit_option == "op2":
				poll.option_two_count += 1
			elif submit_option == "op3":
				poll.option_three_count += 1
			elif submit_option == "op4":
				poll.option_four_count += 1
			else:
				return HttpResponse(400, 'Invalid form option')
			poll.total = poll.option_one_count + poll.option_two_count + poll.option_three_count + poll.option_four_count
			poll.save()
			return redirect ("result",poll.id)
		return render (request,"vote.html",{"poll":poll})
				
		