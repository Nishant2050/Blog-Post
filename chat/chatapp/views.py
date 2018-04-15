from django.shortcuts import render_to_response, render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.contrib import auth
from django.contrib.auth.models import User
from chatapp.forms import MyRegistrationForm, NewPlaceForm, PostForm
from .models import Country, VisitingPlaces,Post
from django.contrib.auth.decorators import login_required
from django.db.models import Count

# Create your views here.
def IndexView(request):
    return render_to_response('chatapp/home.html')

def LoginView(request):
##    c= {}
##    c.update(csrf(request))
    return render_to_response('chatapp/login.html')

def AuthView(request):
    username = request.POST.get('username')
    print(username)
    password = request.POST.get('password')
    print(password)
    user = auth.authenticate(username=username, password=password)
    print(user)

    if user is not None:
        auth.login(request, user)
        return redirect('homepage')
    else:
        return redirect('homepage')

def HomePage(request):
    countries = Country.objects.all()
    return render_to_response('chatapp/homepage.html', {'countries': countries})

def CountryList(request, pk):
    try:
        country = Country.objects.get(pk=pk)
    except:
        raise Http404

    places = country.vplaces.order_by('-last_updated').annotate(replies=Count('posts')-1)
    return render_to_response('chatapp/countries.html', {'country':country, 'places':places})

@login_required
def NewPlace(request, pk):
    try:
        country = Country.objects.get(pk=pk)
        print(country)
    except:
        raise Http404
##    user = User.objects.first()

    if request.method == 'POST':
        form = NewPlaceForm(request.POST)
        if form.is_valid():
            visitplaces=form.save()
            visitplaces.country1=country
            print(request.user)
            visitplaces.starter=str(request.user)
            visitplaces.save()
        
##        visitplaces = VisitingPlaces.objects.create(
##            place_name=place_name,
##            location=location,
##            country1=country,
##            starter=user
##            )
        post = Post.objects.create(
            message=form.cleaned_data.get('message'),
            visiting_places=visitplaces,
            created_by=request.user
            )
        return redirect('place', pk=pk, place_pk = visitplaces.pk)
    else:
        form = NewPlaceForm()
    return render(request, 'chatapp/newplace.html', {'country':country, 'form':form})

def Place(request, pk, place_pk):
    place = get_object_or_404(VisitingPlaces, country1_id=pk, pk=place_pk)
    place.views += 1
    place.save()
    return render(request, 'chatapp/place.html', {'place':place})

@login_required
def Reply(request, pk, place_pk):
    place = get_object_or_404(VisitingPlaces, country1_id=pk, pk=place_pk)
    print(place)
    if request.method == 'POST':
        print('form')
        form = PostForm(request.POST)
        if form.is_valid():
            print(request.user.id)
            reply = form.save(commit=False)
            reply.visiting_places=place
            reply.created_by=request.user
            reply.save()
            return redirect('place', pk=pk, place_pk = place_pk)
    else:
        form = PostForm()
    print('return')
    return render(request, 'chatapp/reply.html', {'place':place, 'form':form})


##def country(request, pk):
##    con = Country.objects.all()
##    try:
##        con1 = Country.objects.get(pk = pk)
##    except:
##        raise Http404
##    return render_to_response('chatapp/country.html', {'con1': con1, 'con':con})
##
##def VisitPlaces(request, pk):
##    try:
##        visitplaces = VisitingPlaces.objects.get(pk = pk)
##    except:
##        raise Http404
##    return render_to_response('chatapp/visitingplaces.html', {'visitplaces': visitplaces})

def LoggedinView(request):
    countries = Country.objects.all()
    states = State.objects.all().count()
##    return HttpResponse(states)
##    return render_to_response('chatapp/loggedin.html', {'full_name': request.user.username})
    return render_to_response('chatapp/loggedin.html', {'countries': countries, 'states': states})
    
def InvalidView(request):
    return render_to_response('chatapp/invalid.html')

def LogoutView(request):
    auth.logout(request)
    return render_to_response('chatapp/logout.html')

def Register(request):
    if request.method == 'POST':
        form = MyRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return render_to_response('chatapp/home.html')
    else:
        form = MyRegistrationForm()
    return render(request, 'chatapp/register.html', {'form': form})


##def CreateUser(request):
##    username = request.POST.get('username','')
##    print(username)
##    password = request.POST.get('password','')
##    print(password)
##    email = request.POST.get('email','')
##    print(email)
##
##    if username and password and email:
##        u,created = User.objects.get_or_create(username=username, email=email,defaults=None)
##        print(str(u))
##        if created:
##            u.set_password(password)
##            print('user was created')
##        else:
##            return HttpResponse('The user already exists')
##    else:
##        return HttpResponse('Please enter the username and password')
##    return render_to_response('chatapp/home.html')
