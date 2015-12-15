from __future__ import unicode_literals

from django.db import models

class Game(models.Model):
	game_name = models.CharField(max_length= 20)
	genre = models.CharField(max_length=20)
	developer = models.CharField(max_length=20)
	release_date = models.DateField('date published')

	EVERYONE = 'E'
	TEEN = 'T'
	MATURE = 'M'

	ESRB_CHOICES = (
		(EVERYONE,'EVERYONE'),
		(TEEN, 'TEEN'),
		(MATURE,'MATURE'),
	)

	esrb_rating = models.CharField(max_length = 1, choices = ESRB_CHOICES)

class Organization(models.Model):
	org_name = models.CharField(max_length=20)
	date_found = models.DateField()

class Team(models.Model):
	game = models.ForeignKey(Game, on_delete=models.CASCADE)
	organization = models.ForeignKey(Organization, on_delete=models.CASCADE)

	team_name = models.CharField(max_length=20)
	logo = models.URLField()
	team_location = models.CharField(max_length=20)
	team_coach = models.CharField(max_length=20)

class Player(models.Model):
	team = models.ForeignKey(Team, on_delete=models.CASCADE)

	player_name = models.CharField(max_length=20)
	birthday = models.DateField()

	ACTIVE = 'ACTIVE'
	BENCH = 'BENCH'
	RETIRED = 'RETIRED'
	STREAMER = 'STREAMER'

	STATUS_CHOICES = (
		(ACTIVE, 'ACTIVE'),
		(BENCH, 'BENCH'),
		(RETIRED, 'RETIRED'),
		(STREAMER, 'STREAMER'),
	)

	player_status = models.CharField(max_length=20,choices = STATUS_CHOICES)



class Tournament(models.Model):
	game = models.ForeignKey(Game, on_delete=models.CASCADE)

	tourney_name = models.CharField(max_length=20)
	tourney_date = models.DateField()
	participants = models.IntegerField()
	first_place = models.CharField(max_length=20)
	second_place = models.CharField(max_length=20)
	third_place = models.CharField(max_length=20)

class Prize(models.Model):
	tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)

	prize_pool = models.IntegerField()
	first_prize = models.IntegerField()
	second_prize = models.IntegerField()
	third_prize = models.IntegerField()
	prize_type = models.CharField(max_length=20)


# Create your models here.
