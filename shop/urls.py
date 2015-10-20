"""shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.i18n import i18n_patterns

from django.conf import settings
from store import views

urlpatterns = [
url(r'^setlang', 'django.views.i18n.set_language', name='setlang'),
]

urlpatterns += i18n_patterns('',

    url(r'^product/', include('store.urls')),
    url(r'^$', include('store.urls')),
    url(r'^shop/', include('store.urls')),
    url(r'^checkout/',include('store.urls')),
    url(r'^cart/',include('store.urls')),
 ##   url(r'^accounts/',include('store.urls')),
##    url(r'^login/',include('store.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^contact$', views.contact_us),
    url(r'^about$', views.about_us),
    #auth urls
##    url(r'^accounts/login$', views.login),

    url(r'^accounts/', include('store.urls')),
    #url(r'^accounts/auth/$', views.auth_view, name='auth'),
    #url(r'^accounts/logout$', views.logout),
    #url(r'^accounts/sign_up$', views.register_user, name='signup'),

##    url(r'^accounts/register$', views.register_user),
##    url(r'^accounts/register_success$', views.register_success),
)



##urlpatterns = [
##    url(r'^shop/',include('store.urls')),
##    url(r'^product/',include('store.urls')),
###    url(r'^checkout/',include('store.urls')),
##    url(r'^$',include('store.urls')),
##    url(r'^admin/', include(admin.site.urls)),
##
##]
