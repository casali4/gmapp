from django.shortcuts import render

# Create your views here.
def landing(request):
    return render(request, 'landing.html')

def contact(request):
    return render(request, 'contact.html')

def sign_in(request):
    return render(request, 'sign-in.html')