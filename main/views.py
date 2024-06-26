import datetime, json
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound, JsonResponse
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse

from .models import Item
from .forms import ItemForm

@login_required(login_url='/login')
def main(request):
    user = request.user
    last_login = user.last_login
    items = Item.objects.filter(user=user)

    # Convert datetime fields in items queryset to formatted strings
    formatted_items = []
    for item in items:
        formatted_item = {
            'id': item.id,
            'name': item.name,
            'amount': item.amount,
            'description': item.description,
            'date_added': item.date_added.strftime("%B %d, %Y"),
            'deadline': item.deadline.strftime("%B %d, %Y, %I:%M %p"),
        }
        formatted_items.append(formatted_item)

    identifier = {
        "app_name": "Tugas Tracker",
        "name": user.username,
        "class": "A",
        "last_login": last_login.strftime("%B %d, %Y, %I:%M %p"),
    }

    # Encode the formatted items queryset to JSON
    items_json = json.dumps(formatted_items)
    items = items_json
    return render(request, "main_landingpage.html", {"identifier":identifier, "items":items})

@login_required(login_url='/login')
def create_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        item = form.save(commit=False)
        item.user = request.user
        item.save()
        return redirect('main:main')

    context = {'form': form}
    return render(request, "create_item.html", context)

@login_required(login_url='/login')
def edit_item(request, id):
    item = Item.objects.get(pk = id)

    form = ItemForm(request.POST or None, instance=item)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:main'))

    context = {'form': form}
    return render(request, "edit_item.html", context)

@login_required(login_url='/login')
def delete_item(request, id):
    item = Item.objects.get(pk = id)
    item.delete()
    return HttpResponseRedirect(reverse('main:main'))

@csrf_exempt
def create_item_ajax(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        amount = request.POST.get("amount")
        description = request.POST.get("description")
        deadline = request.POST.get("deadline")
        user = request.user

        new_item = Item(name=name, amount=amount, description=description, deadline=deadline, user=user)
        new_item.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()

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

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("main:main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

@csrf_exempt
def create_item_flutter(request):
    if request.method == 'POST':

        data = json.loads(request.body)

        new_item = Item.objects.create(
            user = request.user,
            name = data["name"],
            amount = int(data["amount"]),
            description = data["description"],
            deadline = data["deadline"],
        )

        new_item.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)