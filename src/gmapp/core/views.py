from django.shortcuts import render
from django.http import Http404
from django.utils.translation import gettext_lazy as _
from django.http import JsonResponse


import json

#handlers
from .handlers.auth import handler_login
from .handlers.encounters import handler_encounters
from django.contrib.auth import logout 
from django.shortcuts import redirect




### Public views ###

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



### Logged in views ###

def dashboard(request):
    return render(request, 'dashboard.html')

def encounters(request):
    if request.method == 'GET':
        return handler_encounters(request)
    else:
        print("Invalid request method for encounters view")
        # load the sent json
        data = json.loads(request.body.decode('utf-8'))
        # Validate the data and content (only allowed keys and values)
        allowed_settings = {"fantasy", "modern", "scifi"}
        allowed_areas = {"woods", "city", "village", "mountains", "cave", "dungeon", "tavern", "ancient_ruins", "crossroads", "ocean"}
        allowed_dangers = {"all", "safe", "dangerous"}

        setting = data.get("setting")
        area = data.get("area")
        danger = data.get("danger")

        if setting not in allowed_settings:
            return JsonResponse({'error': 'Invalid encounter setting.'}, status=400)
        if area not in allowed_areas:
            return JsonResponse({'error': 'Invalid encounter area.'}, status=400)
        if danger not in allowed_dangers:
            return JsonResponse({'error': 'Invalid danger level.'}, status=400)

        # ...existing code.

        
        return JsonResponse({'headline':'OK', 'text':'', 'data':{}}, status=200)

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


