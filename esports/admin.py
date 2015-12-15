from django.contrib import admin

from .models import Game, Organization, Team, Player, Tournament, Prize

admin.site.register(Game)
admin.site.register(Organization)
admin.site.register(Team)
admin.site.register(Player)
admin.site.register(Tournament)
admin.site.register(Prize)


# Register your models here.
