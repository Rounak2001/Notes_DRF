
from django.http import response
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.serializers import Serializer
from .models import Note
from .serializers import NoteSerializer
from api import serializers
from .utils import updateNote, getNoteDetail, deleteNote, getNotesList, createNote
# Create your views here.


@api_view(['GET'])
def getRoutes(request):

    routes = [
        {
            'Endpoint': '/notes/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of notes'
        },
        {
            'Endpoint': '/notes/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single note object'
        },
        {
            'Endpoint': '/notes/create/',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Creates new note with data sent in post request'
        },
        {
            'Endpoint': '/notes/id/update/',
            'method': 'PUT',
            'body': {'body': ""},
            'description': 'Creates an existing note with data sent in post request'
        },
        {
            'Endpoint': '/notes/id/delete/',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes and exiting note'
        },
    ]
    return Response(routes)


# /notes GET
# /notes POST
# /notes/<id> GET
# /notes/<id> PUT
# /notes/<id> DELETE

# @api_view(['GET', 'POST'])
# def getNotes(request):

#     if request.method == 'GET':
#         return getNotesList(request)

#     if request.method == 'POST':
#         return createNote(request)


# @api_view(['GET', 'PUT', 'DELETE'])
# def getNote(request, pk):

#     if request.method == 'GET':
#         return getNoteDetail(request, pk)

#     if request.method == 'PUT':
#         return updateNote(request, pk)

#     if request.method == 'DELETE':
#         return deleteNote(pk)

from rest_framework import generics
from rest_framework.response import Response
from .models import Note
from .serializers import NoteSerializer

class NoteListView(generics.ListCreateAPIView):
    """
    Handles GET (list all notes) and POST (create a new note) requests
    Replaces getNotes and createNote function-based views
    """
    queryset = Note.objects.all().order_by('updated')
    serializer_class = NoteSerializer

    def perform_create(self, serializer):
        # Optional: customize note creation if needed
        serializer.save()

class NoteDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Handles GET (retrieve), PUT (update), and DELETE requests for a specific note
    Replaces getNote, updateNote, and deleteNote function-based views
    """
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    lookup_field = 'pk'  # This is the default, can be omitted
