from django.conf.urls import url
from Main import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view()),
    url(r'^login_alumno/$', views.login_alumno),
    url(r'^login_patrocinador/$', views.login_patrocinador),
    url(r'^login_administrador/$', views.login_administrador),
    url(r'^alumno/$', views.indexalumno),
    url(r'^patrocinador/$', views.indexpatrocinador),
    url(r'^administrador/$', views.indexadministrador),
    url(r'^logout/$', views.user_logout),
]