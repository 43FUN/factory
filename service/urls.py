from django.conf.urls import url
from service import views

urlpatterns = [
    url(r'^chamfering', views.chamfering, name='chamfering'),
    url(r'^welding', views.welding, name='welding'),
    url(r'^plasmacutting', views.plasmacutting, name='plasmacutting'),
    url(r'^metallsawing', views.metallsawing, name='metallsawing'),
]