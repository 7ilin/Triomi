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
]


urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



