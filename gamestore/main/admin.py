from django.contrib import admin
from .models import GamePlatform, Game, PriceList

# Register your models here.

admin.autodiscover()

admin.site.register(GamePlatform)
admin.site.register(Game)
admin.site.register(PriceList)
