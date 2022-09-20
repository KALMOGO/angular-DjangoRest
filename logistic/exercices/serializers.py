from dataclasses import fields
from pyexpat import model
from rest_framework import serializers, validators
from missions.models import Missions

from missions.models import InfoDepenseMissions
from .models import Exercices

class ExercicesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Exercices
        fields= (
            'id',
            'date_exercice',
            'etat_exercice',)

class RelatedExercicesSerializer(serializers.Serializer):
    date_exercice = serializers.DateTimeField(read_only=True)
    etat_exercice = serializers.BooleanField(read_only=True)


class ExercicesFinanceInfoSerializer(serializers.Serializer):
    totalDepenses= serializers.SerializerMethodField()
    totalRecette =  serializers.SerializerMethodField()
    annee = serializers.SerializerMethodField()

    class Meta:
        model = Exercices
        fields= (
            'annee',
            'totalDepenses',
            'recetteTotales'
        )
        
    def get_annee(self,obj):
        '''
            retourne l'annee d'un exercice
        '''
        return obj.date_exercice.year 

    def get_totalDepenses(self, obj):
        '''
            Retourne la somme total des depenses dans un exercice
        '''
        return obj.totalDepenseMaintenances +  obj.totalDepenseMission

    def get_totalRecette(self, obj):
        '''
            Retourne la somme total des recette dans un exercice
        '''
        return obj.recetteTotales
