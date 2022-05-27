""" Loppis app views file """
from django.shortcuts import render
from .models import Loppis

def all_loppis(request):
    """ A view to return list of all the loppises """
    loppis = Loppis.objects.all()

    context = {
        'loppis': loppis,
    }
    return render(request, 'loppis/loppis.html', context)
