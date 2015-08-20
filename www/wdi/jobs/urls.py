from django.conf.urls import include, url

from wdi.jobs import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
]
