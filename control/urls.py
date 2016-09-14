from django.conf.urls import url
from control import views

urlpatterns = [
    url(r'^$', views.control, name='control'),
]
