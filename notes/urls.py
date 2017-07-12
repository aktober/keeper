from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from notes.views import NewNoteView, EditNoteView, DetailNoteView, ProfileView


urlpatterns = [
    url(r'^add/', login_required(NewNoteView.as_view()), name='add_note'),
    url(r'^edit/(?P<pk>\d+)/$', login_required(EditNoteView.as_view()), name='edit_note'),
    url(r'^all/', login_required(ProfileView.as_view()), name='notes-list'),#todo update names

    url(r'^(?P<pk>[-\w]+)/$', login_required(DetailNoteView.as_view()), name='note-detail'),
]
