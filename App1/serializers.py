from rest_framework import serializers
from .models import Work_Shift

class Work_ShiftSerializer(serializers.ModelSerializer):
    class Meta:
        model = Work_Shift
        fields =('__all__')
