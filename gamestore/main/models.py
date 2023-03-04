from django.db import models


# Create your models here.
class GamePlatform(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class GameManager(models.Manager):
    def get_highlighted(self):
        return self.filter(highlighted=True)

    def get_not_highlighted(self):
        return self.filter(highlighted=False)

    def get_by_platform(self, platform):
        return self.filter(game_platform__name=platform)


class Game(models.Model):
    class Meta:
        ordering = ['-highlighted', 'name']

    name = models.CharField(max_length=50)
    release_year = models.IntegerField(null=True)
    developer = models.CharField(max_length=50)
    published_by = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/', default='images/default.png', max_length=100)
    game_platform = models.ForeignKey(GamePlatform, null=False, on_delete=models.CASCADE)
    highlighted = models.BooleanField(default=False)
    objects = GameManager()

    def __str__(self):
        return f'{self.game_platform.name} - {self.name}'


class PriceList(models.Model):
    added_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    price_per_unit = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    game = models.OneToOneField(Game, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.game.name
