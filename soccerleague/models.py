from django.db import models
from django.urls import reverse

class Team(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('teams')

class Player(models.Model):
    POSITION_CHOICES = [
        {'G', 'Goalie'},
        {'D', 'Defender'},
        {'M', 'Midfielder'},
        {'F', 'Forward'}
    ]
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    position = models.CharField(max_length=10, choices=POSITION_CHOICES)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

    def __str__(self):
        return '%s %s'%(self.last_name, self.first_name)

    def get_absolute_url(self):
        return reverse('players')


class Game(models.Model):
    home_team = models.ForeignKey(Team, related_name="home_games", on_delete=models.CASCADE)
    away_team = models.ForeignKey(Team, related_name="away_games", on_delete=models.CASCADE)
    date = models.DateTimeField()

    class Meta:
        ordering = ['date']

    def __str__(self):
        return '%s %s'%(self.home_team.name, self.away_team.name)

    def get_absolute_url(self):
        return reverse('games')


class Result(models.Model):
    game = models.OneToOneField(Game, on_delete=models.CASCADE)
    score_hometeam = models.IntegerField(default=0)
    score_awayteam = models.IntegerField(default=0)
    team = models.ManyToManyField(Team)

    def __str__(self):
        return '%s %s'%(self.game.home_team.name, self.score_hometeam)

    def get_absolute_url(self):
        return reverse('game_detail', kwargs={'pk':self.pk})


