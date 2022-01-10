from django.contrib import admin
from .models import Location,Package,Booking

# Register your models here.

admin.site.register(Location)
admin.site.register(Package)
admin.site.register(Booking)
