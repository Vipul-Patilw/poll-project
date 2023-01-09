from celery import shared_task
from celery.schedules import crontab
from celery.task import periodic_task
from django.utils import timezone
from Poll.models import Poll

@shared_task
def adding_task(x, y):
    return x + y



@periodic_task(run_every=crontab(minute='*/1'))
def delete_old_foos():
    # Query all the foos in our database
    polls = Poll.objects.all()

    # Iterate through them
    for poll in polls:

        # If the expiration date is bigger than now delete it
        if poll.expiration_date < timezone.now():
            poll.delete()
            # log deletion
    return "completed deleting polls at {}".format(timezone.now())