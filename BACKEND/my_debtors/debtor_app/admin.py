from django.contrib import admin
from . models import *

# Register your models here.
admin.site.register(Discussion)
admin.site.register(Comment)
admin.site.register(Topic)