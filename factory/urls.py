"""factory URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.flatpages import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^feedback/', include(
        'feedback.urls', namespace='feedback')),
    url(r'^products/', include(
        'products.urls', namespace='products')),
    url(r'^production/', include(
        'production.urls', namespace='production')),

]

urlpatterns += [
    url(r'^delivery/', views.flatpage,
        {'url': '/delivery/'},
        name='delivery'),
    url(r'^info/', views.flatpage,
        {'url': '/info/'},
        name='info'),
    url(r'^control', views.flatpage, {'url': '/control/'}, name='control'),
    url(r'^calculator', views.flatpage, {'url': '/calculator/'}, name='calculator'),
    url(r'^service/chamfering', views.flatpage, {'url': '/service/chamfering/'}, name='chamfering'),
    url(r'^service/metallsawing', views.flatpage, {'url': '/service/metallsawing/'}, name='metallsawing'),
    url(r'^service/plasmacutting', views.flatpage, {'url': '/service/plasmacutting/'}, name='plasmacutting'),
    url(r'^service/welding', views.flatpage, {'url': '/service/welding/'}, name='welding'),
    url(r'^companycard', views.flatpage, {'url': '/companycard/'}, name='companycard'),
    url(r'^$', views.flatpage, {'url': '/index/'}, name='index'),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
