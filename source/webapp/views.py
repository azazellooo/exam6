from django.shortcuts import render, redirect, get_object_or_404

from webapp.models import Note, status_choices
from webapp.forms import NoteForm


def index_view(request):
    notes = Note.objects.all().filter(status='active').order_by('-created_at')
    return render(request, 'index.html', context={'notes': notes})


def note_create_view(request):
    if request.method == "GET":
        form = NoteForm()
        return render(request, 'note_create.html', context={'choices': status_choices, 'form': form})
    elif request.method == "POST":
        form = NoteForm(data=request.POST)
        if form.is_valid():
            note = Note.objects.create(
                name=form.cleaned_data.get('name'),
                email=form.cleaned_data.get('email'),
                text=form.cleaned_data.get('text')
            )
            return redirect('note-list')
        return render(request, 'note_create.html', context={'form': form})


def note_update_view(request, pk):
    note = get_object_or_404(Note, id=pk)
    if request.method == 'GET':
        form = NoteForm(initial={
            'name': note.name,
            'email': note.email,
            'text': note.text
        })
        return render(request, 'note_update.html', context={'note': note, 'form': form})
    elif request.method == 'POST':
        form = NoteForm(data=request.POST)
        if form.is_valid():
            note.name = form.cleaned_data.get('name')
            note.email = form.cleaned_data.get('email')
            note.text = form.cleaned_data.get('text')
            note.save()
            return redirect('note-list')
        return render(request, 'note_update.html', context={'form': form, 'task': note})


def note_delete_view(request, pk):
    note = get_object_or_404(Note, id=pk)
    if request.method == "GET":
        return render(request, 'note_delete.html', context={'note': note})
    elif request.method == "POST":
        note.delete()
        return redirect('note-list')
# Create your views here.

