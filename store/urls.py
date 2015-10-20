from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<id>[0-9]+)$', views.details, name='details'),
    url(r'^all$', views.shop, name='shop'),
    url(r'^proceed$', views.checkout, name='checkout'),
    url(r'^showcart$', views.showcart, name='showcart'),
#   url(r'^login$', viwes.login, name='login'),
    url(r'^add/(?P<id>[0-9]+)/$', views.add, name='add'), # !!!! careful with "/$" !!!!!
    url(r'^add/$', views.add, name='add'),                              # needed (without arguments) to use in ajax-function
#   url(r'^add_to_cart/(?P<id>[0-9]+)/$', views.add_to_cart, name='add_to_cart'),
    url(r'^remove/(?P<id>[0-9]+)/$', views.remove, name='remove'),
    url(r'^remove_single/(?P<id>[0-9]+)/$', views.remove_single, name='remove_single'),
    url(r'^remove_single/$', views.remove_single, name='remove_single'),# needed (without arguments) to use in ajax-function
    url(r'^search-results/$', views.search_results),
    url(r'^search/$', views.search, name='search'),
    url(r'^categories/(?P<cat>.+)/$', views.categories, name='categories'),
    url(r'^brands/(?P<br>.+)/$', views.brands, name='brands'),
#   url(r'^auth/$', views.auth_view),
    url(r'^auth/$', views.auth_view, name='auth'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^sign_up$', views.register_user, name='signup'),
#   url(r'^products/$', views.shop, name='shop'),                                # for testing purposes only
]
