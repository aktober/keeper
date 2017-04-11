"""keeper URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from keeper import settings
from notes import views
from notes.api.views import TagCreateAPIView, TagListAPIView, NoteListAPIView,\
NoteDestroyAPIView


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^notes/', include('notes.urls', namespace='notes')),
    url(r'^users/', include('users.urls', namespace='users')),
    url(r'^$', views.home, name='home'),

    url(r'^api/tags/add$', TagCreateAPIView.as_view(), name='api-tags-add'),
    url(r'^api/tags/list$', TagListAPIView.as_view(), name='api-tags-list'),
    url(r'^api/notes/list$', NoteListAPIView.as_view(), name='api-notes-list'),
    url(r'^api/notes/destroy/(?P<pk>[-\w]+)/$', NoteDestroyAPIView.as_view(), name='api-notes-destroy'),
    # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
