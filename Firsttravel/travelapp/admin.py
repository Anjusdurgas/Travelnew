from django.contrib import admin
from .models import Place  #import model place
from .models import Team

# Register your models here.
admin.site.register(Place)
admin.site.register(Team)