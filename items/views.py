from django.shortcuts import render
from django.http import JsonResponse
from .models import Item
from django.shortcuts import get_object_or_404

# Create your views here.
def getItems(request):
    items = list(Item.objects.values())
    return JsonResponse(items, safe=False)

def getItem(request, id):
    item = Item.objects.get(id = id)
    # item = get_object_or_404(Item, id = id) # busca el item con ese id, si no lo encuentra tira un 404
    return JsonResponse(item, safe=False)

def addItem(request):
    title = request.GET["title"]
    price = request.GET["price"]
    quantity = request.GET["quantity"]
    completed = request.GET["completed"]

    task = Item.objects.create(title, price, quantity, completed)

def deleteItem(request, id):
    Item.objects.delete(id)