from django.conf.urls import include, url
from django.views.decorators.csrf import csrf_exempt

from tangent_importer_dashboard.apps.jobs import views

urlpatterns = [
    url(r'^$', views.JobListView.as_view(), name='index'),
    url(r'^(?P<pk>\d+)/runs/$', views.JobRunListView.as_view(), name='runs'),
    url(r'^runs/(?P<pk>\d+)/profiling/$', views.JobRunProfilingView.as_view(), name='runs-profiling'),
    url(r'^api/register/$', csrf_exempt(views.RegisterJobsView.as_view()), name='api-register'),
    url(r'^runs/api/start/$', csrf_exempt(views.JobRunStart.as_view()), name='api-job-run-start'),
    url(r'^runs/api/end/$', csrf_exempt(views.JobRunEnd.as_view()), name='api-job-run-end'),
    url(r'^runs/api/profiling/$', csrf_exempt(views.JobRunProfiling.as_view()), name='api-job-run-profiling'),
]
