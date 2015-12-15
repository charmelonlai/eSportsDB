from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Game, Organization, Team, Player, Tournament, Prize

def index(request):
		context = dict()
		context['game'] = Game.objects.all()
		context['organization'] = Organization.objects.all()
		context['team'] = Team.objects.all()
		context['player'] = Player.objects.all()
		context['tournament'] = Tournament.objects.all()
		context['prize'] = Prize.objects.all()
		return render(request,'index.html', context)

# Create your views here.
