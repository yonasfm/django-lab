from django.contrib import admin
from .models import Company
from .models import Location

admin.site.register(Location)
admin.site.register(Company)
