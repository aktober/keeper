from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render
from django.urls import reverse
from django.views import generic

from notes.models import Note
from notes.forms import NewNote


def home(request):
    return render(request, 'notes/home.html')


class ProfileView(generic.View):

    def get(self, request, *args, **kwargs):
        obj = Note.objects.filter(user=self.request.user).order_by('-date')
        context = {'obj': obj}
        return render(request, 'notes/profile.html', context)


class DetailNoteView(generic.DetailView):
    model = Note

    def get_context_data(self, **kwargs):
        context = super(DetailNoteView, self).get_context_data(**kwargs)
        if self.get_object().user != self.request.user:
            raise Http404
        return context


class NewNoteView(generic.View):

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


class EditNoteView(generic.UpdateView):
    model = Note
    fields = ['title', 'text', 'tags']
    template_name_suffix = '_update'
    success_url = '/notes/all/'

    def get_context_data(self, **kwargs):
        context = super(EditNoteView, self).get_context_data(**kwargs)
        if self.get_object().user != self.request.user:
            raise Http404
        return context
