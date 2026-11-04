
from django.shortcuts import render, redirect, get_object_or_404
from electronica.forms import ElectronicaForm
from electronica.models import Electronics
from django.http import HttpResponse


def create_electronica_view(request):
    if request.method == "POST":
        form = ElectronicaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/electronica_list/')
    else:
        form = ElectronicaForm()

    return render(request, 'electronica/create_electronica.html', {'form': form})


def read_electronica_view(request):
    electronica = Electronics.objects.all().order_by("-id")

    return render(request, 'electronica/electronica_list.html', {
        'electronica': electronica
    })


def update_electronica_view(request, id):
    electronica_id = get_object_or_404(Electronics, id=id)

    if request.method == "POST":
        form = ElectronicaForm(request.POST, instance=electronica_id)
        if form.is_valid():
            form.save()
            return redirect('/electronica_list/')
    else:
        form = ElectronicaForm(instance=electronica_id)

    return render(request, 'electronica/update_electronica.html', {
        'form': form,
        'electronica_id': electronica_id
    })


def delete_electronica_view(request, id):
    electronica_id = get_object_or_404(Electronics, id=id)
    electronica_id.delete()

    return HttpResponse(
        '<h1>Вы успешно удалили товар '
        '<a href="/electronica_list/">На список товаров</a></h1>'
    )
