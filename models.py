from django.db import models

class Game(models.Model):
    room_code = models.CharField(max_length=6, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    started = models.BooleanField(default=False)
    
class Player(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=50)
    anonymous_id = models.CharField(max_length=10, unique=True)

class Vote(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    voted_for = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='votes_against')
    vote_time = models.DateTimeField(auto_now_add=True)