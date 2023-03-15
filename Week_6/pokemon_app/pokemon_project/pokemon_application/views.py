from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'pokemon_application/pokemon.html')

def item(request):
    item_title = request.POST.get('pokemon')
    print(item_title)
    return render(request, 'pokemon_application/item.html')
