from __future__ import unicode_literals
from django.contrib import admin
# This is for removing recent activities
from django.contrib.admin.models import LogEntry
from .models import Project, Service, Value


# This will clear the recent activities in admin
LogEntry.objects.all().delete()
# Above line should be commented while migrating

admin.site.register([Project, Service, Value])
