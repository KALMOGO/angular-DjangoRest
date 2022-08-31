from rest_framework import serializers, validators
from .models import Exercices

class ExercicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercices
        exclude= ('createur',)

class RelatedExercicesSerializer(serializers.Serializer):
    date_exercice = serializers.DateTimeField(read_only=True)
    etat_exercice = serializers.BooleanField(read_only=True)