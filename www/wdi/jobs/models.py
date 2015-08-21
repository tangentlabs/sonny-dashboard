import json

from django.db import models


class Job(models.Model):
    class Meta:
        app_label = 'jobs'

    name = models.CharField(max_length=256, null=False)
    uuid = models.CharField(max_length=64, null=False)

    @property
    def times_run(self):
        return self.jobrun_set.count()

    @property
    def times_failed(self):
        return self.jobrun_set.filter(succeeded=False).count()

    @property
    def times_succeeded(self):
        return self.jobrun_set.filter(succeeded=True).count()

    @property
    def times_pending(self):
        return self.jobrun_set.filter(finished=False).count()

    @property
    def recent_history(self):
        runs = self.jobrun_set.order_by('-start_time')

        return runs[:5:-1]

    @property
    def last_run(self):
        runs = self.jobrun_set.order_by('-start_time')

        if not runs.exists():
            return None

        return runs[0]

    def __str__(self):
        return '<Job: %s>' % self.name


class JobRun(models.Model):
    class Meta:
        app_label = 'jobs'

    job = models.ForeignKey('jobs.Job')
    start_time = models.DateTimeField(auto_now_add=True, null=False)
    end_time = models.DateTimeField(null=True)
    succeeded = models.NullBooleanField()
    finished = models.BooleanField(default=False)
    profiling_json = models.TextField(null=True)

    @property
    def duration(self):
        if self.finished:
            return self.end_time - self.start_time

    @property
    def profiling(self):
        return json.loads(self.profiling_json)

    def __str__(self):
        return '<JobRun: %s @ %s>' % (self.job.name, self.start_time)
