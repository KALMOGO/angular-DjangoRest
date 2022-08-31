# SERIALIZER Maintenance
from rest_framework import serializers
from .models import PiecesEchanges, Mantenances, InfosPieces

class PiecesEchangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PiecesEchanges
        fields = '__all__'

class MantenanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mantenances
        fields = '__all__'

class InfosPieceSerializer(serializers.ModelSerializer):
    class Meta:
        model = InfosPieces
        fields = '__all__'