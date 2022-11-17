from collections import Counter
from .models import created_sessions
from rest_framework import serializers
from rest_framework.renderers import JSONRenderer

class created_sessions_ser(serializers.ModelSerializer):
    class Meta:
        model = created_sessions
        fields = ["masters_name", "number_of_players", "current_number_of_players", "description", "game_type", "price", "is_online","pk"]