from django.contrib import admin
from . models import Contact
from . models import *
# Register your models here.

admin.site.site_header = "Restaurant Admin Panel"
admin.site.site_title = "Restaurant Admin Panel"

admin.site.register(Contact)
admin.site.register(Reservation)
admin.site.register(User)
admin.site.register(category)
admin.site.register(Menu)
