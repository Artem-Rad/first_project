from rest_framework import serializers
from success.models import Desires
from django.contrib.auth.models import User
from timetable.models import ActionsOfDay

class UserSerializater(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('__all__')

#class ActionSerializator