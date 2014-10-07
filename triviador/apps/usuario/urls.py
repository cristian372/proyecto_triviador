from django.conf.urls import patterns, include, url
from .views import *

urlpatterns = patterns('',
    url(r'^registro/$', registro_view),
    url(r'^login/$', login_view),
    url(r'^logout/$', logout_view),
    url(r'^user/perfil/$', perfil_view),
    url(r'^perfil/modificar/$',modificar_perfil),
    url(r'^user/active/$', user_active_view),    
    url(r'^/jugar/$', jugar_view),
)
