from django.conf.urls import url, include
from decor import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^contacts/$', views.contacts, name='contacts'),
]
