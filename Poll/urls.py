from django.contrib import admin
from django.urls import path,include
from Poll import  views
from Poll.registration_view import usercreate
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from Poll.poll_views.CUD_polls import CreatePollView,UpdatePoll
from Poll.poll_views.LD_polls import PollsList,PollDetail,voting

urlpatterns = [
path("edit/poll/<pk>",UpdatePoll.as_view(),name="edit-poll"),
path("result/<pk>",PollDetail.as_view(template_name="results.html"),name="result"),
#path("vote/<pk>",PollDetail.as_view(template_name="vote.html"),name="vote"),
path("vote/<poll_pk>",voting,name="vote"),
path("",PollsList.as_view(template_name="index.html"),name="home"),
path("personal_details",PollsList.as_view(template_name="profile.html"),name="personal_detail"),
path("create/poll",CreatePollView.as_view(),name="create-poll"),
path('bio-data',TemplateView.as_view(template_name="Devloper Resume - M.html"),name="bio-data"),
	path('accounts/', include('django.contrib.auth.urls')),
#	path('userdetail',usersdetail.userdetail,name="data"),
	path("search",views.search,name="search"),
	path('social-create/<email>/<first_name>',views.storesocialacccount,name="social-create"),
	path('after-change-password',views.logout_after_change_password,name='logout-after-change-pass'),
	path('logout-page',TemplateView.as_view(template_name="registration/logout.html"),name="logout-page"),
	  path('password_change',views.ChangePassword.as_view(),name="password"),
	  path("searchdetails",TemplateView.as_view(template_name="searchdetail.html"),name="searchdetail"),
	path('personal_details',views.updateProfile,name='personal_detail'),
#	path('superuser/login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('user/create',usercreate.UserCreate.as_view(),name='registration'), 
  
     path('about',TemplateView.as_view( template_name="about.html"),name='about'),

   ]


   