from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^profile/$', views.profile_view, name='profile'),
    url(r'^security/$', views.my_password_change, name='security'),
    url(r'^password_reset/$', views.my_password_reset, name='reset_password'),
    url(r'^password_reset_done/$', views.my_password_reset_done, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.my_password_reset_confirm, name='password_reset_confirm'),
]
