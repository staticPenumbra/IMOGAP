from django.conf.urls import url

from . import views

app_name = 'imogap'

urlpatterns = [
    url(r'^$', views.blog, name='imogap'),
]