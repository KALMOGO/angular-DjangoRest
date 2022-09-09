from rest_framework import serializers

from .linkSerializer import RelatedChauffeursSerializer
from .models import (
    Clients, Produits, VehiculeParcs, VehiculeLoues,
    CategorieVehicules, documentVehicules, Trajets,
    RecetteDetailPesage, RecetteDetailSansPesage,
    Chauffeurs, Missions, LoueurVehicules,
    DepenseMissions, InfoDepenseMissions, Vehicules
    )

class ClientSerializer(serializers.ModelSerializer):
    '''
        Serializer du model client
    '''
    class Meta:
        model = Clients
        fields= ('id','nom', 'prenom')

class ProduitsSerializer(serializers.ModelSerializer):
    '''
        Serializer du model Produit
    '''
    class Meta:
        model = Produits
        fields= ('id', 'nom', 'unite')

class TrajetsSerializer(serializers.ModelSerializer):
    '''
        Serializer du model Produit
    '''
    intitule = serializers.SerializerMethodField()
    class Meta:
        model = Trajets
        fields= ('id', 'intitule')

    def get_intitule(self, obj):
        return f"{obj.ville_depart}-{obj.ville_arrivee}"

class CategorieVehiculesSerializer(serializers.ModelSerializer):
    '''
        Serializer du model des Categories de vehicule 
    '''
    class Meta:
        model = CategorieVehicules
        fields= '__all__'

class VehiculesSerializer(serializers.ModelSerializer):
    '''
        Serializer pour lestous les vehicules du parc
    '''

    class Meta:
        model = Vehicules
        fields = '__all__'

class documentVehiculesSerializer(serializers.ModelSerializer):
    '''
        Serializer pour le model documentVehicules
    '''
    class Meta:
        model = documentVehicules
        fields = '__all__'

class VehiculeParcsSerializer(VehiculesSerializer):
    # nbreDocument = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = VehiculeParcs
        fields = (
            'immat',
            'marque' ,
            'couleur',
            # 'chauffeur'
            )

    # def get_nbreDocument(self, obj):
    #     return  obj.infos_documents.count()

class VehiculeLouesSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehiculeLoues
        fields = '__all__'

class ChauffeursSerializer(serializers.ModelSerializer):
    '''
        Serializer pour le model chauffeurs
    '''
    class Meta:
        model = Chauffeurs
        fields = '__all__'

class RecetteDetailPesageSerializer(serializers.ModelSerializer):
    '''
        Serializer pour le model RecetteDetailPesage
    '''
    class Meta:
        model = RecetteDetailPesage
        fields = '__all__'

class RecetteDetailSansPesageSerializer(serializers.ModelSerializer):
    '''
        Serializer pour le model RecetteDetailSansPesage
    '''
    class Meta:
        model = RecetteDetailSansPesage
        fields = '__all__'

class DepenseMissionsSerializer(serializers.ModelSerializer):
    '''
        Serializer pour le model DepenseMissions
    '''
    class Meta:
        model = DepenseMissions
        fields =('id','intitule', 'montant')

class MissionsSerializer(serializers.ModelSerializer):
    '''
        Serializer pour le model Missions
    '''
    class Meta:
        model = Missions
        fields = '__all__'
    

class LoueurVehiculesSerializer(serializers.ModelSerializer):
    '''
        Serializer pour le model LoueurVehicules
    '''
    class Meta:
        model = LoueurVehicules
        fields = '__all__'

class InfoDepenseMissionsSerializer(serializers.ModelSerializer):
    '''
        Serializer pour le model InfoDepenseMissions
    '''
    class Meta:
        model = InfoDepenseMissions
        fields = '__all__'

# ----- serializer specifique concernant l'exercice ------

class listAcceuilMissionExerciceSerializer(serializers.ModelSerializer):
    
    chauffeur = serializers.SerializerMethodField()
    class Meta:
        model = Missions
        fields =(
            'id',
            'chauffeur',
            'etat_mission'
        )

    def get_chauffeur(self, obj):
        vehicule = obj.vehicule_concerne_id
        chauffeur  = Chauffeurs.objects.filter(vehicule=vehicule)
        return chauffeur.values("nom", "prenom")


class chauffeurVehiculeMissionSerializer(serializers.ModelSerializer):
    chauff = serializers.SerializerMethodField()
    class Meta:
      model = VehiculeParcs
      fields = ('id','immat','chauff')

    def get_chauff(self, obj):
      '''
        retourner les informations 
        sur les chauffeurs du vehicules: nom, prenon
      '''
      return obj.chauffeur.values('nom', 'prenom')[0] # reourne une liste d'un element par vehicule

#Group.objects.filter(members=my_person_object)