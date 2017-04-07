from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Constellation


# def index(request):
#     constellations = Constellation.objects.order_by('abbreviation')
#     return render(request, 'constellations/index.html', {'constellations': constellations})
#
# def detail(request, constellation_id):
#     constellation = get_object_or_404(Constellation, pk=constellation_id)
#
#     return render(request, 'constellations/detail.html', {'constellation': constellation})

class IndexView(generic.ListView):
    template_name = 'constellations/index.html'
    context_object_name = 'constellations'

    def get_queryset(self):
        return Constellation.objects.order_by('abbreviation')


class DetailView(generic.DetailView):
    model = Constellation
    template_name = 'constellations/detail.html'
