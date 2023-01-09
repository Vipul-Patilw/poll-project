from django.db import models
from PIL import Image
#import numpy as np

from django.contrib.auth.models import User
from django import forms
import os
from django.urls import reverse
from datetime import datetime
from django_quill.fields import QuillField
# Create your models here.



class UserRegistration(models.Model):
	
	profile_pic = models.ImageField(upload_to= "User_Portal/profiles",blank=True)

	first_name = models.CharField(max_length=80)
	
	last_name = models.CharField(max_length=80)
	
	mobile_number= models.CharField(max_length=122)
		
	email= models.CharField(max_length=122)
	
	gender = models.CharField(max_length=122)
	
	class Meta:
		db_table= "Poll_user_registration"
		
	def __str__(self):
		return self.first_name 
		
class Poll(models.Model):
    question = QuillField()
    option_one = models.CharField(max_length=80)
    option_two = models.CharField(max_length=80)
    option_three = models.CharField(max_length=80)
    option_four = models.CharField(max_length=80)
    option_one_count = models.IntegerField(default=0)
    option_two_count = models.IntegerField(default=0)
    option_three_count = models.IntegerField(default=0)
    option_four_count = models.IntegerField(default=0)
    name = models.CharField(max_length=80)
    profile= models.CharField(max_length=222,blank=True)
    email = models.CharField(max_length=80)
    total = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    expiration_date = models.DateTimeField(default=datetime.now())
    def __str__(self):
    	return self.question
	