from django.contrib.auth.models import User
from django.db import models
from PIL import Image

class page_tovar(models.Model):
    photo = models.ImageField()
    description = models.TextField()
    name = models.CharField(max_length=255)

class games_names(models.Model):
    name = models.CharField(max_length=255)



class created_sessions(models.Model):
    masters_name = models.CharField(max_length=255)
    number_of_players = models.IntegerField()
    current_number_of_players = models.IntegerField()
    description = models.TextField()
    game_type = models.ForeignKey(games_names,on_delete = models.PROTECT)
    price = models.IntegerField()
    is_online = models.BooleanField(default = False)
    contacts = models.CharField(max_length=40, default = '')

class players_in_current_game(models.Model):
    user = models.IntegerField(default=0)
    player = models.CharField(max_length=255, default=None)
    game_id = models.ForeignKey(created_sessions, on_delete=models.CASCADE)
    approved_to_play = models.BooleanField(default=False)
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    avatar = models.ImageField(default='default.jpg', upload_to='profile_images')
    bio = models.TextField()
    # resizing images
    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.avatar.path)

        if img.height > 100 or img.width > 100:
            new_img = (100, 100)
            img.thumbnail(new_img)
            img.save(self.avatar.path)

    def __str__(self):
        return self.user.username





