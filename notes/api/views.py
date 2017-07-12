from rest_framework import generics
from rest_framework.response import Response

from notes.models import Note
from .serializers import NoteSerializer


class NoteListAPIView(generics.ListAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = []
    authentication_classes = []


class NoteDestroyAPIView(generics.DestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = []
    authentication_classes = []

    def delete(self, request, pk):
        qs = Note.objects.get(id=pk)
        qs.delete()
        return Response(data={'result': "OK"}, status=200)
