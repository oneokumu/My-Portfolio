from django.shortcuts import render
from django.contrib import messages
from .forms import ContactForm

def home_view(request):
    return render(request, 'portfolio_app/home.html')

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your message has been submitted successfully!")
            form = ContactForm()  # Clear the form after successful submission
        else:
            messages.error(request, "There was an error in your submission.")
    else:
        form = ContactForm()

    return render(request, 'portfolio_app/contact.html', {'form': form})
