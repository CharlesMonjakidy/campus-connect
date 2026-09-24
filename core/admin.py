from django.contrib import admin
from .models import Announcement, Course, ScheduleItem

admin.site.register(Course)
admin.site.register(Announcement)
admin.site.register(ScheduleItem)
