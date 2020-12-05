from django.shortcuts import render
from .models import Result, Team, Player, Game
from django.http import Http404
from django.views.generic import CreateView, UpdateView


def landing(request):
    teams = Team.objects.all()
    return render(request, 'landing.html',{
        'teams': teams
    })


def home(request):
    teams = Team.objects.all()
    return render(request, 'home.html',{
        'teams': teams
    })


def about(request):
    teams = Team.objects.all()
    return render(request, 'about.html', {
        'teams': teams
    })


def results(request):
    teams = Team.objects.all()
    results = Result.objects.all().order_by('game__date')
    return render(request, 'results.html', {
        'results': results,
        'teams': teams
    })


def teams(request):
    try:
        teams = Team.objects.all()
    except Team.DoesNotExist:
        raise Http404("Team Not Found")
    return render(request, 'teams.html', {
        'teams': teams
    })

def team_detail(request, team_id):
    try:
        teams = Team.objects.all()
        team = Team.objects.get(id=team_id)
        results = Result.objects.all()
        players = Player.objects.all()

    except Team.DoesNotExist:
        raise Http404('Team Not Found')
    return render(request, 'team_detail.html', {
        'teams': teams,
        'team': team,
        'results': results,
        'players': players
    })


def players(request):
    try:
        teams = Team.objects.all()
        players = Player.objects.all()
    except Player.DoesNotExist:
        raise Http404('Player Not Found')
    return render(request, 'players.html', {
        'players': players,
        'teams': teams,
    })


def player_detail(request, player_id):
    try:
        teams = Team.objects.all()
        players = Player.objects.get(id=player_id)
    except Player.DoesNotExist:
        raise Http404('Player Not Found')
    return render(request, 'player_detail.html', {
        'players': players,
        'teams': teams,
    })


def games(request):
    try:
        teams = Team.objects.all()
        games = Game.objects.all()
    except Player.DoesNotExist:
        raise Http404('Game Not Found')
    return render(request, 'games.html', {
        'teams': teams,
        'games': games
    })


def game_detail(request, game_id):
    try:
        teams = Team.objects.all()
        games = Game.objects.get(id=game_id)
    except Player.DoesNotExist:
        raise Http404('Player Not Found')
    return render(request, 'game_detail.html', {
        'teams': teams,
        'games': games
    })

class PlayerCreateView(CreateView):
    model = Player
    fields = ['first_name', 'last_name', 'position', 'team']


class TeamCreateView(CreateView):
    model = Team
    fields = ['name']


class GameCreateView(CreateView):
    model = Game
    fields = ['home_team', 'away_team', 'date']


class ResultCreateView(CreateView):
    model = Result
    fields = ['score_hometeam', 'score_awayteam']


class ResultUpdateView(UpdateView):
    model = Result
    fields = ['score_hometeam', 'score_awayteam']