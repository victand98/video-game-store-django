from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from .forms import SignupForm
from django.contrib.auth.models import User
from .models import Game


# Create your views here.

def index(request):
    max_highlighted_game = 3
    max_game_list = 9
    highlighted_games_list = Game.objects.get_highlighted()
    games_list = Game.objects.get_not_highlighted()
    show_more_link_highlighted = highlighted_games_list.count() > max_highlighted_game
    show_more_link_games = games_list.count() > max_game_list

    context = {
        'highlighted_games_list': highlighted_games_list[:max_highlighted_game],
        'games_list': games_list[:max_game_list],
        'show_more_link_games': show_more_link_games,
        'show_more_link_highlighted': show_more_link_highlighted
    }

    return render(request, 'main/index.html', context)


@csrf_protect
def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password']
            )
            user.save()
            return render(request, 'main/create_account_success.html', {})
    else:
        form = SignupForm()
    return render(request, 'main/signup.html', {'form': form})


def show_all_games(request):
    games_list = Game.objects.all()
    context = {
        'games': games_list
    }
    return render(request, 'main/all_games.html', context)


def show_highlighted_games(request):
    games_list = Game.objects.get_highlighted()
    context = {
        'games': games_list
    }
    return render(request, 'main/highlighted.html', context)
