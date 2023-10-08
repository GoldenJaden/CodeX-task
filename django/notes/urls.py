from django.urls import path

from . import views

urlpatterns = [
    path("", views.notes, name="notes"),
    path("update-note/<str:pk>", views.updateNote, name='update-note'),
    path("delete-note/<str:pk>", views.deleteNote, name='delete-note'),
    path("create-note", views.createNote, name='create-note'),
]