from rest_framework import serializers
from .models import personal_detail_model
from .models import Document_model
from .models import emergency_contact
from .models import salary
from .models import socialmedialink

class persoal_detail_serializers(serializers.ModelSerializer):
    class Meta:
        model=personal_detail_model
        fields="__all__"

class Document_serializers(serializers.ModelSerializer):
        class Meta:
            model=Document_model
            fields="__all__"

class emergencycontact_serializers(serializers.ModelSerializer):
     class Meta:
            model=emergency_contact
            fields="__all__"


class salaryserializers(serializers.ModelSerializer):
     class Meta:
        model=salary
        fields="__all__"

class socialmedialserializer(serializers.ModelSerializer):
     class Meta:
          model=socialmedialink
          fields="__all__"