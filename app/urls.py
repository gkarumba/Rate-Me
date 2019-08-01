from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    url(r'^$',views.landing_page,name='home'),
    url(r'^project/(\d+)',views.project,name ='project'),
    url(r'^new/project$', views.new_project, name='new_project'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
    