from datetime import datetime

from wdi.jobs import models


def register_job_start(name, uuid):
    job, _ = models.Job.objects.get_or_create(uuid=uuid)

    if job.name != name:
        job.name = name
        job.save()

    job_run = models.JobRun.objects.create(job=job)

    return job_run


def register_job_end(job_run, succeeded):
    job_run.end_time = datetime.now()
    job_run.succeeded = succeeded
    job_run.finished = True
    job_run.save()
