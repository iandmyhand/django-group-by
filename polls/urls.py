from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^init/$', views.initialize_questions, name='initialize_questions'),
]
