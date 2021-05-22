from django.contrib import admin
from .models import *

admin.site.site_header = 'FOA Administration'
admin.site.index_title = 'Admin Dashboard'

# Register your models here.
admin.site.register(Contact_us)

