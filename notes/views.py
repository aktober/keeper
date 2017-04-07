from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, DetailView, View, UpdateView

from notes.models import Note
from notes.forms import NewNote


def home(request):
    return render(request, 'notes/base.html')


class NotesListView(ListView):
    model = Note

    def get_queryset(self):
        return Note.objects.filter(user=self.request.user).order_by('-date')


class NoteDetailView(DetailView):
    model = Note

    def get_context_data(self, **kwargs):
        context = super(NoteDetailView, self).get_context_data(**kwargs)
        if self.get_object().user != self.request.user:
            raise Http404
        return context


class NewNoteView(View):

    def get(self, request):
        f = NewNote()
        context = {'form': f}
        return render(request, 'notes/new_note.html', context)

    def post(self, request):
        f = NewNote(request.POST)
        if f.is_valid():
            new_note = f.save(commit=False)
            new_note.user = request.user
            new_note.save()
            return HttpResponseRedirect(reverse('notes:notes-list'))


class EditNoteView(UpdateView):
    model = Note
    fields = ['title', 'text']
    template_name_suffix = '_update'
    success_url = '/notes/all/'

    def get_context_data(self, **kwargs):
        context = super(EditNoteView, self).get_context_data(**kwargs)
        if self.get_object().user != self.request.user:
            raise Http404
        return context

