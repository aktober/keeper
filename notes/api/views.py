from rest_framework import generics
from rest_framework.response import Response

from notes.models import Tag, Note
from .serializers import TagSerializer, NoteSerializer


class TagCreateAPIView(generics.CreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = []
    authentication_classes = []


class TagListAPIView(generics.ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = []
    authentication_classes = []


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


class TagDestroyAPIView(generics.DestroyAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = []
    authentication_classes = []

    def delete(self, request, pk):
        qs = Tag.objects.get(id=pk)
        qs.delete()
        return Response(data={'result': "OK"}, status=200)