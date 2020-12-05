
from django.contrib import admin
from django.urls import path
from soccerleague import views as soccerleague_views
from soccerleague.views import PlayerCreateView, GameCreateView, TeamCreateView, ResultUpdateView, ResultCreateView
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', auth_views.LoginView.as_view(template_name="landing.html"), name="landing"),
    path('home/', soccerleague_views.home, name="home"),
    path('about/', soccerleague_views.about, name="about"),
    path('teams/', soccerleague_views.teams, name="teams"),
    path('teams/<int:team_id>', soccerleague_views.team_detail, name="team_detail"),
    path('teams/add', TeamCreateView.as_view(template_name='team_form.html'), name="teams_add"),
    path('players/', soccerleague_views.players, name="players"),
    path('players/<int:player_id>', soccerleague_views.player_detail, name="player_detail"),
    path('players/add', PlayerCreateView.as_view(template_name="player_form.html"), name="player_add"),
    path('games/', soccerleague_views.games, name="games"),
    path('games/<int:pk>', soccerleague_views.game_detail, name="game_detail"),
    path('games/add', GameCreateView.as_view(template_name="game_form.html"), name="game_add"),
    path('results/', soccerleague_views.results, name="results"),
    path('results/add', ResultCreateView.as_view(template_name="result_form.html"), name="result_add"),
    path('results/<int:pk>/', ResultUpdateView.as_view(template_name="result_form.html"), name="result_update")
]
