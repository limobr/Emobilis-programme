from django.shortcuts import render

# Create your views here.
def welcome_home(request):
    """Function to display landig page"""
    context = {

    }

    return render(request, "index.html", context)

def story_view(request):
    context = {

    }

    return render(request, "story.html", context)

def team_view(request):
    context = {

    }

    return render(request, "team.html", context)

def contact_view(request):
    context = {

    }

    return render(request, "contact.html", context)