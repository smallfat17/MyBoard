from django.conf.urls import url
from django.contrib.auth.views import LogoutView, LoginView
import django.contrib.auth.views
from . import views

app_name = 'accounts'

urlpatterns = [
    # url('^signup/$', views.signup, name='signup'),
    # url('^logout/$', LogoutView.as_view(), name='logout'),
    # url('^login/$', views.login, name='login')
]