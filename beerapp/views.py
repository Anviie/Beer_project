from django.shortcuts import render


from .forms import BeerForm
from .models import Beer


def index(request):
    beer = Beer.objects.get(pk=4)
    context = {
        'beer': beer
    }
    return render(request, 'beer_app/index.html', context)


def beer_form(request):
    beer = BeerForm(
        request.POST or None,
        files=request.FILES or None
        )
    context = {
        'beer': beer
    }
    if beer.is_valid():
        beer.save()
    return render(request, 'beer_app/beer_form.html', context)
