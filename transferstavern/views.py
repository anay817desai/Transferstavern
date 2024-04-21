from django.http import Http404
from django.shortcuts import render
from .models import Transferstavern


def index(request):

    newest_transferstavern = Transferstavern.objects.all()

    context = {'newest_transferstavern':  newest_transferstavern}

    return render(request, 'transferstavern/index.html', context)
