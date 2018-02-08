"""URL patterns for clanhole app
"""
from django.urls import path

from . import views

app_name = 'pvpstats'
urlpatterns = [
        #Page to show leaderboard for 'stat'
        path('<str:stat>/', views.pvpstats, name = 'pvpstats'),
        #Page to show all of user 'name' stats (not using this but it is here)
        path('members/<str:name>/', views.memberpvp, name = 'memberpvp')
        ]
