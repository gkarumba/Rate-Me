from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    url(r'^$',views.landing_page,name='home'),
    url(r'^project/(?P<project_id>\d+)',views.project,name ='project'),
    url(r'^new/project$', views.new_project, name='new_project'),
    url(r'^edit/profile$', views.edit_profile, name='edit_profile'),
    url(r'^about',views.view_about,name='about'),
    url(r'^accounts/profile/$', views.profile, name='profile'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
    