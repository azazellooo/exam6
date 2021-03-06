from django.shortcuts import render, redirect

from webapp.models import Note, status_choices
from webapp.forms import NoteForm


def index_view(request):
    notes = Note.objects.all().filter(status='active').order_by('created_at', 'updated_at')
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
# Create your views here.
