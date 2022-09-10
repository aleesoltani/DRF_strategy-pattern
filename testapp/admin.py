from django.contrib import admin

from .models import SampleUser

@admin.register(SampleUser)
class SampleUserAdmin(admin.ModelAdmin):
    pass
