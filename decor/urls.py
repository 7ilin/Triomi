from django.conf.urls import url, include
from decor import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^contacts/$', views.contacts, name='contacts'),
    url(r'^call_me/$', views.call_me, name='call_me'),
    url(r'^portfolio/$', views.portfolio, name='portfolio'),
    url(r'^image/(?P<pk>[0-9]+)/$', views.image_view, name='image_view'),
    url(r'^post/$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^rent/$', views.rent, name='rent'),
    url(r'^image_rent/(?P<pk>[0-9]+)/$', views.rent_view, name='rent_view'),
]


urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



