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
    return render(request,'index.html',{'projects':projects})
    

def project(request,id):
    try:
        project = Projects.get_project_by_id(id)
    except DoesNotExist:
        raise Http404()
    current_user= request.User
    comments = Reviews.get_review_by_image(id)
    
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            comment = form.cleaned_data['comment']
            review = Reviews()
            review.image = image
            review.user = current_user
            review.review = comment
            review.save()
    else:
        form = ReviewForm()
        
    return render(request, 'project.html',{'image':image,'form':form,'comments':comments})