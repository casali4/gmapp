from django.shortcuts import render




#handlers
from .handlers.auth import handler_login

# Create your views here.
def landing(request):
    return render(request, 'landing.html')

def contact(request):
    return render(request, 'contact.html')

def sign_in(request):

    #if GET --> render sign-in.html
    if request.method == 'GET':
        return render(request, 'sign-in.html')

    elif request.method == 'POST':
    #if post --> process the form
        return handler_login(request)
    



def dashboard(request):
    pass
    return render(request, 'dashboard.html')

    