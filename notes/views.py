from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, DetailView, View, UpdateView

from notes.models import Note
from notes.forms import NewNote


def home(request):
    return render(request, 'notes/base.html')


class NotesListView(ListView):
    model = Note


class NoteDetailView(DetailView):
    model = Note

    def get_context_data(self, **kwargs):
        context = super(NoteDetailView, self).get_context_data(**kwargs)
        # context['now'] = timezone.now()
        return context


class NewNoteView(View):

    def get(self, request):
        f = NewNote()
        context = {'form': f}
        return render(request, 'notes/new_note.html', context)

    def post(self, request):
        f = NewNote(request.POST)
        if f.is_valid():
            f.save()
            return HttpResponseRedirect(reverse('notes:notes-list'))


class EditNoteView(UpdateView):
    model = Note
    fields = ['title', 'text']
    template_name_suffix = '_update'
    success_url = '/notes/'
