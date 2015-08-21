from django import forms

from wdi.jobs import models


class JobStartForm(forms.ModelForm):
    class Meta(object):
        model = models.Job
        fields = ['name', 'uuid']


class JobEndForm(forms.Form):
    job_run = forms.ModelChoiceField(queryset=models.JobRun.objects.all(), required=True)
    succeeded = forms.BooleanField(required=True)
