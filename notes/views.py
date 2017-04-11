import json

from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views import generic

from notes.models import Note, Tag
from notes.forms import NewNote


def home(request):
    return render(request, 'notes/home.html')


class NotesListView(generic.ListView):
    model = Note

    def get_queryset(self):
        return Note.objects.filter(user=self.request.user).order_by('-date')


class NotesListView2(generic.View):
    # model = Note
    #
    # def get_queryset(self):
    #     return Note.objects.filter(user=self.request.user).order_by('-date')
    def get(self, request):
        notes = Note.objects.all()
        context = {'notes': notes}
        return render(request, 'notes/note_list2.html', context)


class NoteDetailView(generic.DetailView):
    model = Note

    def get_context_data(self, **kwargs):
        context = super(NoteDetailView, self).get_context_data(**kwargs)
        if self.get_object().user != self.request.user:
            raise Http404
        return context


class NewNoteView(generic.View):

    def get(self, request):
        f = NewNote()
        all_tags = Tag.objects.all()
        context = {'form': f, 'all_tags': all_tags}
        return render(request, 'notes/new_note.html', context)

    def post(self, request):
        f = NewNote(request.POST)
        if f.is_valid():
            new_note = f.save(commit=False)
            new_note.user = request.user

            tags = []
            choice = request.POST.getlist('tag_select')
            for c in choice:
                tag = Tag.objects.get(id=c)
                tags.append(tag)
            new_note.save()

            for t in tags:
                new_note.all_tags.add(t)

            return HttpResponseRedirect(reverse('notes:notes-list'))


class EditNoteView(generic.UpdateView):
    model = Note
    fields = ['title', 'text']
    template_name_suffix = '_update'
    success_url = '/notes/all/'

    def get_context_data(self, **kwargs):
        context = super(EditNoteView, self).get_context_data(**kwargs)
        if self.get_object().user != self.request.user:
            raise Http404
        return context


class TagsListView(generic.ListView):
    model = Tag

#TODO remove
def remove_note(request, pk):
    # id = int(request.POST.get('pk'))
    note = Note.objects.get(id=pk)
    note.delete()
    # remove_load = {'success': True}
    # return HttpResponse(json.dumps(remove_load), content_type='application/json')
    return HttpResponse('ok')