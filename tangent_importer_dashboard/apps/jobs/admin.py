from django.contrib import admin

from tangent_importer_dashboard.apps.jobs import models


admin.site.register(models.Job)
admin.site.register(models.JobRun)
