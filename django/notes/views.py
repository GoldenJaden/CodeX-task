from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Note
from .forms import NoteForm
from django.contrib import messages


def mainPage(request):
    return HttpResponse('Main Page')

def notes(request):
    ctx = {'Notes': Note.objects.all(),}
    return render(request, 'notes/notes.html', ctx)


def updateNote(request, pk):
    user = request.user
    note = user.note_set.get(id=pk)
    form = NoteForm(instance=note)

    if request.method == "POST":
        form = NoteForm(request.POST, request.FILES, instance=note)
        if form.is_valid():
            form.save()
            messages.success(request, "Your note was successfully submitted!")
            return redirect('notes')
        
    ctx = {'form': form}
    return render(request, "notes/note_form.html", ctx)


def deleteNote(request, pk):
    user = request.user
    note = user.note_set.get(id=pk)
    if request.method == "POST":
        note.delete()
        messages.success(request, 'Note was deleted successfully!')
        return redirect('notes')
    ctx = {'note': note}
    return render(request, "notes/delete_note.html", ctx)


def createNote(request):
    user = request.user
    form = NoteForm()

    if request.method == "POST":
        form = NoteForm(request.POST, request.FILES)
        if form.is_valid():
            note = form.save(commit=False)
            note.owner = user
            note.save()
            messages.success(request, 'Note was created successfully!') 
            return redirect('notes')

    ctx = {'form': form}
    return render(request, "notes/note_form.html", ctx)


