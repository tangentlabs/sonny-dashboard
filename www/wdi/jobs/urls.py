from django.conf.urls import include, url
from django.views.decorators.csrf import csrf_exempt

from wdi.jobs import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^api/job_start/$', csrf_exempt(views.JobStartRun.as_view()), name='api-job-start'),
    url(r'^api/job_end/$', csrf_exempt(views.JobEndRun.as_view()), name='api-job-end'),
    url(r'^api/job_profiling/$', csrf_exempt(views.JobRunProfiling.as_view()), name='api-job-run-profiling'),
]
