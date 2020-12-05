from django import forms
from django.shortcuts import redirect
from .models import Player, Game, Team

class FreeAgent(forms.ModelForm):
    class Meta:
        model = Player
        fields = ['first_name', 'last_name', 'position', 'team']

        def form_valid(self, form):
            return super().form_valid(form)



class TeamCaptain(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['name']

        def form_valid(self, form):
            return super().form_valid(form)


class NewGame(forms.ModelForm):
    class Meta:
        model = Game
        fields = ['home_team', 'away_team', 'date', 'team']


