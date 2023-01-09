from django.contrib import admin

# Register your models here.
from Poll.models import UserRegistration,Poll
# Register your models here.

admin.site.register(UserRegistration)
admin.site.register(Poll)