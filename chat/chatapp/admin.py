from django.contrib import admin
from .models import Country, VisitingPlaces, Post, State
# Register your models here.

admin.site.register(Country)
admin.site.register(State)
admin.site.register(VisitingPlaces)
admin.site.register(Post)

