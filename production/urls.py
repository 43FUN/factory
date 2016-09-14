from django.conf.urls import url
from production import views

urlpatterns = [
    url(r'^$', views.production, name='production'),
]