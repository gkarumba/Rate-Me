from django.shortcuts import render,redirect, get_object_or_404,render_to_response
from .models import Profiles,Projects,Reviews,RatemeLetterRecipients
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from .forms import NewProjectForm,ReviewForm,UpdateProfileForm,RatemeSubscriptionForm
from .email import send_welcome_email
from django.template import RequestContext

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
        
    return render(request, 'project.html',{'project':project,'form':form,'comments':comments})

@login_required(login_url='/accounts/login/')
def new_project(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.user = current_user
            project.save()
        return redirect('home')

    else:
        form = NewProjectForm()
    return render(request, 'new_project.html', {"form": form})

@login_required(login_url='/accounts/login/')
def edit_profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = UpdatebioForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = current_user
            image.save()
        return redirect('home')

    else:
        form = UpdatebioForm()
    return render(request, 'edit_profile.html', RequestContext(request, {}))

@login_required(login_url='/accounts/login/')
def profile(request, username = None):
    user = request.user
    profile = Profiles.filter_profile_by_id(user.id)
    # if not username:
    #     username = request.user.username
    # current_user = request.user
    # projects by user id
    projects = Projects.objects.filter(profile_id=user.id)

    return render(request, 'profile.html', locals())