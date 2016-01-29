from django.contrib import admin

from wdi.jobs import models


admin.site.register(models.Job)
admin.site.register(models.JobRun)
