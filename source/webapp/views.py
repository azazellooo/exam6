from django.shortcuts import render

from webapp.models import Note


def index_view(request):
    notes = Note.objects.all().filter(status='active').order_by('created_at', 'updated_at')
    return render(request, 'index.html', context={'notes': notes})
# Create your views here.
