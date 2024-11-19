from django.shortcuts import render, redirect, get_object_or_404
from .models import Booking
# Create your views here.
def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, 'about.html')
    
def book_table(request):
    """ Function to handle booking form submission """
    if request.method == 'POST':
        # Create a variable to pick the input fields and save the form data
        bookings = Booking(
            name=request.POST['name'],
            email=request.POST['email'],
            phone=request.POST['phone'],
            date=request.POST['date'],
            time=request.POST['time'],
            people=request.POST['people'],
            message=request.POST['message'],
        )
        # Saving the inputs to DB
        bookings.save()

        # Redirect to the home page
        return redirect('show_bookings')
        

    else:
        # If the request is not POST, render the booking form
        return render(request, 'book_table.html')

def retrieve_bookings(request):
    #Create a vatiable to store these appointments
    bookings = Booking.objects.all()
    context = {'bookings':bookings}
    return render(request, 'show_bookings.html', context)

def delete_booking(request, id):
    """Deleting"""
    booking = Booking.objects.get(id=id) #fetch the particular booking by its id
    booking.delete() #actual deleting
    return redirect('show_bookings') #just remain on the same page

def update_booking(request, booking_id):
    """ Function to update an existing booking """
    booking = get_object_or_404(Booking, id=booking_id)

    if request.method == 'POST':
        # Update the booking with the new data from the form
        booking.name = request.POST.get('name')
        booking.email = request.POST.get('email')
        booking.phone = request.POST.get('phone')
        booking.date = request.POST.get('date')
        booking.time = request.POST.get('time')
        booking.people = request.POST.get('people')
        booking.message = request.POST.get('message')
        
        # Save the updated booking
        booking.save()

        # Redirect to the show bookings page
        return redirect('show_bookings')

    
    return render(request, "edit_booking.html", {'booking': booking})


def events(request):
    return render(request, 'events.html')

def gallery(request):
    return render(request, 'gallery.html')

def menu(request):
    return render(request, 'menu.html')
    
def specials(request):
    return render(request, 'specials.html')