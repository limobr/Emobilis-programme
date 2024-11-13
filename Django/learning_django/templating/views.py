from django.shortcuts import render

# Create your views here.
def home(request):
    context = {}
    return render(request, "templating/home.html", context)

def story(request):
    context = {}
    return render(request, "templating/story.html", context)

def team(request):
    context = {}
    return render(request, "templating/team.html", context)

def contact(request):
    context = {}
    return render(request, "templating/contact.html", context)
