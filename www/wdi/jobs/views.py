from django.views import generic

from wdi.jobs import models


class IndexView(generic.ListView):
    template_name = 'jobs/index.html'
    model = models.Job
