from django.conf.urls import url
from products import views

urlpatterns = [
    url(r'^(?P<category_id>\d+)/$', views.categories, name='categories'),
    url(r'^product/(?P<products_id>\d+)/$', views.product, name='product'),
]
