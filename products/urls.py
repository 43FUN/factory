from django.conf.urls import url
from products import views

urlpatterns = [
    url(r'^accessories', views.accessories, name='accessories'),
    url(r'^shell_ppu', views.shell_ppu, name='shell_ppu'),
    url(r'^system_odk', views.system_odk, name='system_odk'),
    url(r'^tubing_oc', views.tubing_oc, name='tubing_oc'),
    url(r'^tubing_pe', views.tubing_pe, name='tubing_pe'),
]
