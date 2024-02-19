from django.shortcuts import render

def main(request):
    content={
        "app_name" : "Tugas Tracker",
        "name": "Mikhael Deo Barli",
        "class": "A",
    }
    return render(request, "main_landingpage.html", {"content":content,})