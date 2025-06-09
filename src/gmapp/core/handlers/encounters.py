# Django imports
from django.shortcuts import render
from django.utils.translation import gettext_lazy as _

# General imports
from typing import Dict

# Model imports
from ..models import Encounters, User_encounters


def handler_encounters(request):
    """
    Handles the encounters page.
    If the user is not authenticated, redirects to the sign-in page.
    If the user is authenticated, renders the encounters page.
    """
    ctx : Dict = {}
    
    # TODO get lang of user
    lang = "en-us"  # Default to the current language code

    # TODO get one random encounter from the database
    random_encounter = Encounters.objects.filter(active=True).order_by('?').first()
    if not random_encounter:
        #TODO improve this! 
        ctx['error'] = _("No active encounters found.")
        return render(request, 'encounters.html', ctx)
    
    # get based on lang 
    random_encounter_dict : Dict = random_encounter.translations.get(lang)

    # TODO get all encounters from user (saved)


    # Add to context
    ctx['random_encounter'] = random_encounter_dict

    return render(request, 'encounters.html',ctx)