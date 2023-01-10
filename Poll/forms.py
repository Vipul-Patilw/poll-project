from Poll.registration_form.userlogin import UserCreateForm
from django import forms
from.models import Poll
from django.forms import ModelForm
UserCreateForm
from django.core.exceptions import ValidationError

class CreatePollForm(ModelForm):
#    def __init__(self,*args,**kwargs):
#        user = kwargs.pop('user', None)
#        super(CreatePollForm, self).__init__(*args, **kwargs)
#        self.fields['used_his'].queryset = User.objects.filter(pk = user.id)
    class Meta:
        model = Poll
        fields= "__all__"
        exclude = ("option_one_count",
    "option_two_count",
    "option_three_count","option_four_count","total","created_at",'expiration_date')
        widgets= {
        	"option_one":forms.TextInput(attrs={"class":"form-control"}),
        'option_two':forms.TextInput(attrs={"class":"form-control"}),
'option_three':forms.TextInput(attrs={"class":"form-control"}),
'option_four':forms.TextInput(attrs={"class":"form-control"}),
        }
        labels= {"question":"Enter Poll Question"}
    def clean(self):
       email = self.cleaned_data["email"]
       op1 = self.cleaned_data["option_one"]
       op2 = self.cleaned_data["option_two"]
       op3 = self.cleaned_data["option_three"]
       op4 = self.cleaned_data["option_four"]
       poll_limit = Poll.objects.filter(email=email).count()
       if not self.instance.pk:
         	if poll_limit >= 4:
         		raise ValidationError({'question':'Sorry you already created 4 polls, your limit is over you need to wait till 24hrs to again create new poll'})	
       if op1 == op2 or  op2 == op3 or op1==op3 or op1==op4 or op2 == op4 or op3 == op4:
       	raise ValidationError({'option_one':'Options should be unique from each other','option_two':'Options should be unique from each other','option_three':'Options should be unique from each other','option_four':'Options should be unique from each other'})
       
       	
       	
       	
			    
			    