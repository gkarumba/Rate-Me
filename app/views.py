from django.shortcuts import render,redirect, get_object_or_404
from .models import Profiles,Projects,Reviews,RatemeLetterRecipients
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from .forms import NewProjectForm,ReviewForm,UpdateProfileForm,RatemeSubscriptionForm
from .email import send_welcome_email

# Create your views here.
@login_required(login_url='/accounts/login/')
def landing_page(request):
    projects = Projects.get_all_projects()
    retur render(request,'index.html',{'projects':projects})
    
