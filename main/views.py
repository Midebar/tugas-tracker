from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core import serializers

from .models import Item
from .forms import ItemForm

def main(request):
    items = Item.objects.all()

    identifier={
        "app_name" : "Tugas Tracker",
        "name": "Mikhael Deo Barli",
        "class": "A",
    }

    return render(request, "main_landingpage.html", {"identifier":identifier, "items":items})

def create_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:main')

    context = {'form': form}
    return render(request, "create_item.html", context)

def show_xml(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")