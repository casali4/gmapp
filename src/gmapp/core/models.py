from django.db import models
from django.contrib.auth.models import User

# Create your models here.


# TODO model for encounters
class Encounters(models.Model): 
    # class area options
    class AreaOptions(models.TextChoices):
        FOREST = 'Forest', 'Forest'
        MOUNTAIN = 'Mountain', 'Mountain'
        DESERT = 'Desert', 'Desert'
        CITY = 'City', 'City'
        UNDERGROUND = 'Underground', 'Underground'
        OCEAN = 'Ocean', 'Ocean'
        
    translations = models.JSONField(default=dict, help_text='Needs to be in Form: {"de-de":{"title":content, "text":content}} - DO NOT LET USER CHANGE THESE WITHOUT VERIFICATION') #TODO remove the blank and null additions #supposed to look like this {"key":"value"}
    area = models.CharField(max_length=100, choices=AreaOptions)  # Area where the encounter takes place
    active = models.BooleanField(default=True, help_text='If false, the encounter will not be shown to users')  # If the encounter is active or not

    def __str__(self):
        return str(self.translations)
    
    #TODO check when enterin a new encounter if for each translation the necessary fields are filled in


class User_encounters(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    encounter = models.ForeignKey(Encounters, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.encounter.translations

    