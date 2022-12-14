from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import *
from rest_framework.serializers import Serializer, ModelSerializer, CharField
from rest_framework.authtoken.models import Token
from rest_framework.renderers import JSONRenderer

class created_sessions_ser(ModelSerializer):
    class Meta:
        model = created_sessions
        # fields = ["masters_name", "number_of_players", "current_number_of_players", "description", "game_type", "price", "is_online","pk"]
        fields='__all__'

class UserSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'

class UsersInGameSerializer(ModelSerializer):

    class Meta:
        model = players_in_current_game
        fields = '__all__'

class gametype(ModelSerializer):

    class Meta:
        model = games_names
        fields = '__all__'
class usersS(ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'

class BagSerializer(ModelSerializer):

    class Meta:
        model = players_in_current_game
        fields = '__all__'
        depth=2

class LoginRequestSerializer(Serializer):
    model = User

    username = CharField(required=True)
    password = CharField(required=True)


class TokenSeriazliser(ModelSerializer):

    class Meta:
        model = Token
        fields = ['key']