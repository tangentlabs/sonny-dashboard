from django.utils import timezone

from sonny_dashboard.apps.jobs import models


def register_jobs(jobs):
    uuids = []
    for job_details in jobs['importers']:
        uuid = job_details['uuid']
        name = job_details['name']
        job, _ = models.Job.objects.get_or_create(uuid=uuid)

        job.available = True
        job.name = name
        job.save()

        uuids.append(uuid)

    models.Job.objects\
        .exclude(uuid__in=uuids)\
        .update(available=False)


def register_job_start(name, uuid):
    jobs = models.Job.objects.filter(uuid=uuid)
    if jobs.exists():
        job = jobs.get()
    else:
        job = models.Job.objects.create(uuid=uuid, name=name)

    job_run = models.JobRun.objects.create(job=job)

    return job_run


def register_job_end(job_run, succeeded):
    job_run.end_time = timezone.now()
    job_run.succeeded = succeeded
    job_run.finished = True
    job_run.save()


def register_job_run_profiling(job_run, profiling_json):
    job_run.profiling_json = profiling_json
    job_run.save()
