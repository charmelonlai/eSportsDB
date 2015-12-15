from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Game, Organization, Team, Player, Tournament, Prize

class FrontPageView(TemplateView):
	template_name = 'index.html'


	def index(request):
		game = Game.objects.all()
		organization = Organization.objects.all()
		team = Team.objects.all()
		player = Player.objects.all()
		tournament = Tournament.objects.all()
		prize = Prize.objects.all()
		return render(request,'index.html')

# Create your views here.
