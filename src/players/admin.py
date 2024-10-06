from django.contrib import admin
from .models import Player, PlayerSession, PlayerClue, Vote, Action

# Register your models here.

admin.site.register(Player)
admin.site.register(PlayerSession)
admin.site.register(PlayerClue)
admin.site.register(Vote)
admin.site.register(Action)