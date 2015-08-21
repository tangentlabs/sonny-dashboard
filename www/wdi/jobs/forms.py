from django import forms

from wdi.jobs import models


class RegisterJobsForm(forms.Form):
    jobs = forms.CharField(required=True)


class JobRunStartForm(forms.ModelForm):
    class Meta(object):
        model = models.Job
        fields = ['name', 'uuid']


class JobRunEndForm(forms.Form):
    job_run = forms.ModelChoiceField(queryset=models.JobRun.objects.all(), required=True)
    succeeded = forms.BooleanField(required=True)


class JobRunProfilingForm(forms.Form):
    job_run = forms.ModelChoiceField(queryset=models.JobRun.objects.all(), required=True)
    profiling_json = forms.CharField(required=True)
