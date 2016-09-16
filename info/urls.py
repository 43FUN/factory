from django.conf.urls import url
from info import views

urlpatterns = [
    url(r'^$', views.info, name='info'),
    url(r'^company_card', views.company_card, name='company_card')
]

