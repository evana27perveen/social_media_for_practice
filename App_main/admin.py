from django.contrib import admin
from App_main.models import *

# Register your models here.

admin.site.register(Story)
admin.site.register(Likes)
admin.site.register(Comments)
admin.site.register(Message)