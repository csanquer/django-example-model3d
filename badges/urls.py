from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.list, name='list'),
    url(r'^user/(?P<user_id>[0-9]+)/$', views.list_user_badges, name='list_user_badges'),

]
