
from django.shortcuts import render, get_object_or_404
from . import models
from .models import Tour


def tour_list_view(request):
    tour_list = Tour.objects.all().order_by('-id')

    return render(request, 'tour_list.html', {
        'tour_list': tour_list
    })


def tour_detail_view(request, tour_id):
    tour = get_object_or_404(Tour, id=tour_id)

    return render(request, 'tour_detail.html', {
        'tour': tour
    })
