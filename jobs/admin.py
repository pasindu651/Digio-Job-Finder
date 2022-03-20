from django.contrib import admin
from .models import *

# Register your models here.

class Manager(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('title',)


from .models import *
admin.site.register(Job, Manager)
admin.site.register(Applicant)