from django.contrib import admin
from django.conf.urls import include, url
from chatapp import views
from accounts import views as accounts_view

urlpatterns = [
##    url(r'^home/$', views.IndexView, name = 'index'),
##    url(r'^login/$', views.LoginView, name = 'login'),
##    url(r'^logout/$', views.LogoutView, name = 'logout'),
##    url(r'^loggedin/$', views.LoggedinView, name = 'loggedin'),
##    url(r'^invalid/$', views.InvalidView, name = 'invalid'),
##    url(r'^register/$', views.Register, name = 'register'),
####    url(r'^createuser/$', views.CreateUser, name = 'createuser'),
    url(r'^$', views.HomePage, name = 'homepage'),
    url(r'^country/(?P<pk>\d+)/$', views.CountryList, name='countrylist'),
    url(r'^country/(?P<pk>\d+)/new/$', views.NewPlace, name='newplace'),
    url(r'^country/(?P<pk>\d+)/place/(?P<place_pk>\d+)/$', views.Place, name='place'),
    url(r'^country/(?P<pk>\d+)/place/(?P<place_pk>\d+)/reply/$', views.Reply, name='reply'),
    url(r'^auth/$', views.AuthView, name = 'auth'),
]
