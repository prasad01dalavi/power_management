from __future__ import unicode_literals
from django.contrib import admin
# This is for removing recent activities
from django.contrib.admin.models import LogEntry
from .models import Project, Service, Value


# This will clear the recent activities in admin
LogEntry.objects.all().delete()
# Above line should be commented while migrating


class ProjectAdmin(admin.ModelAdmin):
    # define which columns should be displayed
    list_display = ('created_at', 'name', 'power_in', 'power_out', 'energy')


class ServiceAdmin(admin.ModelAdmin):
    # define which columns should be displayed
    list_display = ('created_at', 'project', 'mode')


class ValueAdmin(admin.ModelAdmin):
    # define which columns should be displayed
    list_display = ('created_at', 'name', 'formula', 'file')


# This will register my models to admin
admin.site.register(Project, ProjectAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Value, ValueAdmin)
# Note: To enable list_display I have to register admin-name too
