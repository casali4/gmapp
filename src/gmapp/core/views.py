from django.shortcuts import render




#handlers
from .handlers.auth import handler_login
from django.contrib.auth import logout 
from django.shortcuts import redirect

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
    return render(request, 'dashboard.html')

def encounters(request):
    return render(request, 'encounters.html')

def rolling_tables(request):
    return render(request, 'rolling_tables.html')

def items_rewards(request):
    return render(request, 'items_rewards.html')

def questboard(request):
    return render(request, 'questboard.html')

def npcs(request):
    return render(request, 'npcs.html')

def music_playlists(request):
    return render(request, 'music_playlists.html')



# settings

def settings(request):
    return render(request, 'settings.html')

def account(request):
    return render(request, 'account.html')


def logout(request):
    logout(request)
    return redirect('sign_in')


