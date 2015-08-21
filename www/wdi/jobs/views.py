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


class JobListView(generic.ListView):
    template_name = 'jobs/index.html'
    model = models.Job
    paginate_by = 20


class RegisterJobsView(generic.FormView):
    methods = ['post']
    form_class = forms.RegisterJobsForm

    def form_valid(self, form):
        services.register_jobs(
            jobs=json.loads(form.cleaned_data['jobs']))

        return json_response({'ok': 'ok'})

    def form_invalid(self, form):
        return json_response({'error': 'invalid form fields'}, status=400)


class JobRunStart(generic.FormView):
    methods = ['post']
    form_class = forms.JobRunStartForm

    def form_valid(self, form):
        job_run = services.register_job_start(
            name=form.cleaned_data['name'], uuid=form.cleaned_data['uuid'])

        return json_response({'job_run_id': job_run.id})

    def form_invalid(self, form):
        return json_response({'error': 'invalid form fields'}, status=400)


class JobRunEnd(generic.FormView):
    methods = ['post']
    form_class = forms.JobRunEndForm

    def form_valid(self, form):
        services.register_job_end(
            job_run=form.cleaned_data['job_run'],
            succeeded=form.cleaned_data['succeeded'])

        return json_response({'ok': 'ok'})

    def form_invalid(self, form):
        return json_response({'error': 'invalid form fields'}, status=400)


class JobRunProfiling(generic.FormView):
    methods = ['post']
    form_class = forms.JobRunProfilingForm

    def form_valid(self, form):
        services.register_job_run_profiling(
            job_run=form.cleaned_data['job_run'],
            profiling_json=form.cleaned_data['profiling_json'])

        return json_response({'ok': 'ok'})

    def form_invalid(self, form):
        return json_response({'error': 'invalid form fields'}, status=400)


class JobRunListView(generic.ListView):
    template_name = "jobs/runs/index.html"
    model = models.JobRun
    paginate_by = 10

    def get_object(self):
        return models.Job.objects.get(pk=self.kwargs['pk'])

    def get(self, request, **kwargs):
        self.job = self.get_object()

        return super(JobRunListView, self).get(request, **kwargs)

    def get_queryset(self):
        queryset = super(JobRunListView, self).get_queryset()

        queryset = queryset.filter(job=self.job)
        queryset = queryset.order_by('-start_time')

        return queryset

    def get_context_data(self, **kwargs):
        context = super(JobRunListView, self).get_context_data(**kwargs)

        context['job'] = self.job

        return context


class JobRunProfilingView(generic.DetailView):
    template_name = "jobs/runs/profiling.html"
    model = models.JobRun
