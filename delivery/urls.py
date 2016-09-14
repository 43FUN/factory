from django.conf.urls import url
from delivery import views

urlpatterns = [
    url(r'^$', views.delivery, name='delivery'),
]
