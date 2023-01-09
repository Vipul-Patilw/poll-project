from django.views.generic import ListView,DetailView
from Poll.models import Poll
from django.shortcuts import  render,redirect,HttpResponse
class PollsList(ListView):
	model = Poll
	context_object_name = "poll_list"
	ordering = ["-total"]
	
		
class PollDetail(DetailView):
	model = Poll
	context_object_name = "poll"	
	
def voting(request,poll_pk):
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
				
		