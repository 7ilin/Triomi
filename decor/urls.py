from django.conf.urls import url, include
from decor import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^contacts/$', views.contacts, name='contacts'),
    url(r'^call_me/$', views.call_me, name='call_me'),
    url(r'^portfolio/$', views.portfolio, name='portfolio'),
]
