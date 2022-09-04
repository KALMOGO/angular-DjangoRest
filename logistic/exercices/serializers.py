from dataclasses import fields
from pyexpat import model
from rest_framework import serializers, validators
from .models import Exercices

class ExercicesSerializer(serializers.ModelSerializer):
    # etat_exercice = serializers.BooleanField(read_only=True)
    # maintenance = serializers.SerializerMethodField()

    class Meta:
        model = Exercices
        fields= (
            'id',
            'date_exercice',
            'etat_exercice'
        )

    # def get_maintenance(self, obj):
    #     return {
    #         'nombre':obj.maintenances.count(),
    #         'montant':obj.totalDepenseMaintenances
    #     }

class RelatedExercicesSerializer(serializers.Serializer):
    date_exercice = serializers.DateTimeField(read_only=True)
    etat_exercice = serializers.BooleanField(read_only=True)
