from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from notes.views import NewNoteView, EditNoteView, NoteDetailView, NotesListView, \
    TagsListView


urlpatterns = [
    url(r'^add/', login_required(NewNoteView.as_view()), name='add_note'),
    url(r'^edit/(?P<pk>\d+)/$', login_required(EditNoteView.as_view()), name='edit_note'),
    url(r'^all/', login_required(NotesListView.as_view()), name='notes-list'),
    url(r'^tags/', login_required(TagsListView.as_view()), name='tags'),
    url(r'^(?P<pk>[-\w]+)/$', login_required(NoteDetailView.as_view()), name='note-detail'),
]
