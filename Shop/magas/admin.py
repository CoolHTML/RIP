from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(games_names)
admin.site.register(created_sessions)
admin.site.register(Profile)
admin.site.register(players_in_current_game)
