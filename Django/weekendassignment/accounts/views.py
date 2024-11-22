from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from django.templatetags.static import static

def register(request):
    """Show the registration form and handle user registration"""
    if request.method == 'POST':
        # Get form data
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        # Check if passwords match
        if password == confirm_password:
            # Check if username already exists
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'Email already in use')
            else:
                # Create the user if validation passes
                user = User.objects.create_user(
                    username=username,
                    email=email,
                    password=password,
                    first_name=first_name,
                    last_name=last_name
                )
                user.save()
                messages.success(request, "Account created successfully")
                return redirect('home')
        else:
            messages.error(request, 'Passwords do not match')

    return render(request, 'accounts/register.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Authenticate the user
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password.")

    return render(request, 'accounts/login.html')


def logout_view(request):
    logout(request)
    return redirect('home')

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import UserProfile
from django.core.exceptions import ObjectDoesNotExist

def user_profile(request):
    """Load and update user profile information"""
    
    # Load user data on GET request
    if request.method == 'GET':
        try:
            # Get the user's profile
            user_profile = request.user.userprofile

            # If the user has a profile, populate the context with their details
            context = {
                'first_name': request.user.first_name,
                'last_name': request.user.last_name,
                'username': request.user.username,
                'email': request.user.email,
                'phone': user_profile.phone,
                'date_of_birth': user_profile.date_of_birth,
                'county_name': user_profile.county_name,
                'gender': user_profile.gender,
                'profile_picture': user_profile.profile_picture.url if user_profile.profile_picture else static('assets/img/default_dp.png')  # Default picture
            }

            return render(request, 'accounts/userprofile.html', context)

        except UserProfile.DoesNotExist:
            context = {
                'first_name': request.user.first_name,
                'last_name': request.user.last_name,
                'username': request.user.username,
                'email': request.user.email,
                'phone': '',
                'date_of_birth': '',
                'county_name': '',
                'gender': '',
                'profile_picture': 'https://bootdey.com/img/Content/avatar/avatar1.png'
            }

            return render(request, 'accounts/userprofile.html', context)

    # Handle form submission on POST request
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        date_of_birth = request.POST.get('date_of_birth')
        county_name = request.POST.get('county_name')
        gender = request.POST.get('gender')

        # Check if a new profile picture was uploaded
        profile_picture = request.FILES.get('profile_picture')

        # Update user object and save
        user = request.user
        user.first_name = first_name
        user.last_name = last_name
        user.username = username
        user.email = email

        # Check if the user has a related UserProfile
        user_profile, created = UserProfile.objects.get_or_create(user=user)

        # update users profile
        user_profile.phone = phone
        user_profile.date_of_birth = date_of_birth
        user_profile.county_name = county_name
        user_profile.gender = gender

        # If a new profile picture is provided, update it
        if profile_picture:
            user_profile.profile_picture = profile_picture

        # Save changes to both user and profile models
        user.save()
        user_profile.save()

        messages.success(request, 'Profile updated successfully' if not created else 'Profile created successfully')
        return redirect('user_profile')  # Redirect to the same page to show changes

    return render(request, 'accounts/userprofile.html')

    
