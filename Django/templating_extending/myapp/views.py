from django.shortcuts import render

# Create your views here.
def index_page(request):
    context = {}
    return render(request, "index.html", context)

def story(request):
    context = {}
    return render(request, "mystory.html", context)

def team(request):
    context = {}
    return render(request, "team.html", context)

def contact(request):
    context = {}
    return render(request, "contact.html", context)