
from django.urls import path
from .views import NoteListView, NoteDetailView
from . import views

# urlpatterns = [
#     path('', views.getRoutes, name="routes"),
#     path('notes/', views.getNotes, name="notes"),
#     path('notes/create/', views.createNote, name="create-note"),
#     path('notes/<str:pk>/update/', views.updateNote, name="update-note"),
#     path('notes/<str:pk>/delete/', views.deleteNote, name="delete-note"),

#     path('notes/<str:pk>/', views.getNote, name="note"),
# ]
urlpatterns = [
    path('', views.getRoutes, name="routes"),
    # URL for listing all notes and creating a new note
    path('notes/', NoteListView.as_view(), name='note-list'),
    
    # URL for retrieving, updating, or deleting a specific note
    path('notes/<int:pk>/', NoteDetailView.as_view(), name='note-detail'),
]