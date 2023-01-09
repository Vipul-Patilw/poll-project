import  datetime
from django.contrib.auth.models import User
from Poll.models import UserRegistration



def context_data(request):
    if request.user.is_authenticated:
        date = datetime.date.today()
        current_user = request.user
        email = current_user.email  
        user_profile = UserRegistration.objects.filter(email=email).all()
        #for search users
        
		    
    else:
        user_profile = ""
    
    
    return {'user_profile':user_profile}