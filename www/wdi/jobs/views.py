import json

from django.views import generic
from django.http import HttpResponse
from django.core.serializers.json import DjangoJSONEncoder

from wdi.jobs import forms
from wdi.jobs import services

from wdi.jobs import models


def json_response(response, **kwargs):
    json_dump = json.dumps(response, cls=DjangoJSONEncoder)
    return HttpResponse(json_dump, content_type="application/json", **kwargs)


class IndexView(generic.ListView):
    template_name = 'jobs/index.html'
    model = models.Job


class JobStartRun(generic.FormView):
    methods = ['post']
    form_class = forms.JobStartForm

    def form_valid(self, form):
        job_run = services.register_job_start(
            name=form.cleaned_data['name'], uuid=form.cleaned_data['uuid'])

        return json_response({'job_run_id': job_run.id})

    def form_invalid(self, form):
        return json_response({'error': 'invalid form fields'}, status=400)


class JobEndRun(generic.FormView):
    methods = ['post']
    form_class = forms.JobEndForm

    def form_valid(self, form):
        services.register_job_end(
            job_run=form.cleaned_data['job_run'],
            succeeded=form.cleaned_data['succeeded'])

        return json_response({'ok': 'ok'})

    def form_invalid(self, form):
        return json_response({'error': 'invalid form fields'}, status=400)
