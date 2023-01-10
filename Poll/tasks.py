from celery import shared_task
from django.utils import timezone
from Poll.models import Poll
import celery
@shared_task
def adding_task(x, y):
    return x + y



@shared_task
def delete_old_polls():
    # Query all the foos in our database
    polls = Poll.objects.all()

    # Iterate through them
    for poll in polls:

        # If the expiration date is bigger than now delete it
        if poll.expiration_date < timezone.now():
            poll.delete()
            # log deletion
    return "completed deleting polls at {}".format(timezone.now())