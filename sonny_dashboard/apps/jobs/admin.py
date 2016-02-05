from django.contrib import admin

from sonny_dashboard.apps.jobs import models


admin.site.register(models.Job)
admin.site.register(models.JobRun)
