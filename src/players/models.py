from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Player(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=100, help_text="The player's chosen nickname.")
    character = models.OneToOneField('characters.Character', on_delete=models.SET_NULL, null=True, blank=True, related_name='player')

    def __str__(self):
        return self.nickname or self.user.username
    
class PlayerSession(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='sessions')
    session = models.ForeignKey('gameplay.GameSession', on_delete=models.CASCADE, related_name='player_sessions')
    status = models.CharField(max_length=20, choices=[('active', 'Active'), ('eliminated', 'Eliminated')], default='active')
    score = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.player.nickname} in session {self.session.id}"

class Action(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='actions')
    description = models.TextField(help_text="Description of the action taken.")
    timestamp = models.DateTimeField(auto_now_add=True)
    phase = models.IntegerField(help_text="The game phase during which the action occurred.")

    def __str__(self):
        return f"Action by {self.player.nickname} at {self.timestamp}: {self.description}"

class PlayerClue(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='clues')
    clue = models.ForeignKey('characters.Clue', on_delete=models.CASCADE)
    is_revealed = models.BooleanField(default=False)

    def __str__(self):
        return f"Clue for {self.player.nickname}: {self.clue.description[:30]}{'...' if len(self.clue.description) > 30 else ''}"

class Vote(models.Model):
    voter = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='votes')
    target = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='votes_received')
    reason = models.TextField(null=True, blank=True)
    phase = models.IntegerField(help_text="The game phase during which the vote occurred.")

    def __str__(self):
        return f"{self.voter.nickname} voted for {self.target.nickname} during phase {self.phase}"
