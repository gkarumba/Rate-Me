from django.shortcuts import render,redirect, get_object_or_404
from .models import Profiles,Projects,Reviews,RatemeLetterRecipients
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse


# Create your views here.
