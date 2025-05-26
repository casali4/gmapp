from django.urls import path

from . import views

  

urlpatterns = [

    path('', views.landing, name='landing'),
    path('contact', views.contact, name='contact'),
    path('sign-in', views.sign_in, name='sign_in'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('encounters', views.encounters, name='encounters'),
    path('rolling-tables', views.rolling_tables, name='rolling_tables'),
    path('items-rewards', views.items_rewards, name='items_rewards'),
    path('questboard', views.questboard, name='questboard'),
    path('npcs', views.npcs, name='npcs'),
    path('music-playlists', views.music_playlists, name='music_playlists'),

]