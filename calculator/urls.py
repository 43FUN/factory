from django.conf.urls import url
from calculator import views

urlpatterns = [
    url(r'^', views.calculator, name='calculator'),
]