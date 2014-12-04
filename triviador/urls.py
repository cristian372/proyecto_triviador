from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'triviador.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url ( '' , include ( 'social.apps.django_app.urls' , namespace = 'social' )),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('triviador.apps.trivia.urls')),
    url(r'^', include('triviador.apps.usuario.urls')),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
    {'document_root':settings.MEDIA_ROOT,}),	
)
