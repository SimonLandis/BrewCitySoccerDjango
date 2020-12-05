from django.contrib import admin
from .models import Player, Team, Game, Result

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'position', 'team']


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ['home_team', 'away_team', 'date']

@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ['game', 'score_hometeam', 'score_awayteam']