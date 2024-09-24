from django.shortcuts import render, redirect
from .models import Game, Player, Vote

def join_game(request):
    if request.method == 'POST':
        room_code = request.Post['room_code']
        game = Game.objects.get(room_code=room_code)
        player = Player.objects.create(game=game, anonymous_id=generate_random_id())
        request.session['player_id'] = player.id
        return redirect('game', game_id=game.id)
    return render(request, 'join_game.html')

def game_view(request, game_id):
    player_id = request.session.get('player_id')
    player = Player.objects.get(id=player_id)
    game = Game.objects.get(id=game_id)
    return render(request, 'game.html', {'game': game, 'player': player})

def vote(request, game_id):
    if request.method == "POST":
        player = Player.objects.get(id=request.session['player_id'])
        voted_for = Player.objects.get(id=request.POST['voted_for_id'])
        Vote.objects.create(player=player, voted_for=voted_for)
    return redirect('game', game_id=game_id)