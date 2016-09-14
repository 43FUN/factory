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
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^feedback/', include(
        'feedback.urls', namespace='feedback')),
    url(r'^delivery/', include(
        'delivery.urls', namespace='delivery')),
    url(r'^info/', include('info.urls', namespace='info')),
    url(r'^products/', include(
        'products.urls', namespace='products')),
    url(r'^calculator/', include(
        'calculator.urls', namespace='calculator')),
    url(r'^control/', include('control.urls', namespace='control')),
    url(r'^production/', include(
        'production.urls', namespace='production')),
    url(r'^service/', include('service.urls', namespace='service')),
    url(r'^$', include('index.urls', namespace='index')),

]
