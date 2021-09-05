from rest_framework import serializers
from .models import *

class NinoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Nino
        fields="__all__"
        
        
class BitacoraSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bitacora
        fields = "__all__"
        

class RutinaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rutina
        fields = "__all__"
