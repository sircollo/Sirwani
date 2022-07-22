from django import http
from django.shortcuts import render
from .models import *
from .forms import *
from django.contrib import messages
# Create your views here.

def index(request):
  projects = Projects.objects.all()
  if request.method == 'POST':
    form = FeedBackForm(request.POST)
    if form.is_valid():
      name = form.cleaned_data['name']
      form.save()
      messages.success(request, name+' for your Message, I will get back to you soon.')
      form = FeedBackForm()
      return http.HttpResponseRedirect("/")        
  form = FeedBackForm()
  context = {'projects': projects, 'form': form}
  return render(request, 'index.html', context)