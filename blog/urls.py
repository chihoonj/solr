from django.conf.urls import url

from . import views

urlpatterns = [
		url(r'^$', views.posts, name='posts'),
        url(r'^list$', views.post_list, name='post_list'),
        url(r'^item/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
		]
