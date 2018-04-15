from django.shortcuts import render_to_response, render, redirect
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.contrib import auth
from django.contrib.auth.models import User
from chatapp.forms import MyRegistrationForm
from django.contrib.auth import login
##from django.context_processors import csrf
# Create your views here.

def Signup(request):
##    c= {}
##    c.update(csrf(request))
    if request.method =='POST':
        form = MyRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
##            return render_to_response('chatapp/homepage.html', {'user':user})
            return redirect('homepage')
    else:
            form = MyRegistrationForm()
    return render(request, 'signup.html', {'form':form})
