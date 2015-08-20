from django.db import models


class Job(models.Model):
    class Meta:
        app_label = 'jobs'

    name = models.CharField(max_length=256, null=False)
    uuid = models.CharField(max_length=32, null=False)

    @property
    def times_run(self):
        return self.jobrun_set.count()

    @property
    def times_failed(self):
        return self.jobrun_set.filter(succeded=False).count()

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
    start_time = models.DateTimeField(null=False)
    end_time = models.DateTimeField()
    succeded = models.BooleanField()

    def __str__(self):
        return '<JobRun: %s @ %s>' % (self.job.name, self.start_time)
