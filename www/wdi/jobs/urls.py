from django.conf.urls import include, url
from django.views.decorators.csrf import csrf_exempt

from wdi.jobs import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^runs/api/start/$', csrf_exempt(views.JobRunStart.as_view()), name='api-job-run-start'),
    url(r'^runs/api/end/$', csrf_exempt(views.JobRunEnd.as_view()), name='api-job-run-end'),
    url(r'^runs/api/profiling/$', csrf_exempt(views.JobRunProfiling.as_view()), name='api-job-run-profiling'),
]
