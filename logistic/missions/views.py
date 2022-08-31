from rest_framework import generics, permissions
from .serializers import (
    ClientSerializer, ProduitsSerializer,
    VehiculeParcsSerializer, LoueurVehiculesSerializer,
    documentVehiculesSerializer, CategorieVehiculesSerializer,
    RecetteDetailPesageSerializer, RecetteDetailSansPesageSerializer,
    MissionsSerializer,InfoDepenseMissionsSerializer,ChauffeursSerializer,
    VehiculesSerializer,TrajetsSerializer, VehiculeLouesSerializer,
     DepenseMissionsSerializer)

from .models import (
    Clients, Produits, VehiculeParcs, VehiculeLoues,
    CategorieVehicules, documentVehicules, Trajets,
    RecetteDetailPesage, RecetteDetailSansPesage,
    Chauffeurs, Missions, LoueurVehicules,
    DepenseMissions, InfoDepenseMissions, Vehicules)

class ClientListCreateAPIView(generics.ListCreateAPIView):
    '''
        View: get, post clients
    '''
    queryset = Clients.objects.all()
    serializer_class = ClientSerializer
list_create_clientAPIVIEW = ClientListCreateAPIView.as_view()


class RetUpdateDelClients(generics.RetrieveUpdateDestroyAPIView):
    '''
        View pour put, patch, delete des clients 
    '''
    queryset = Clients.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [permissions.IsAdminUser]
ret_upate_del_ClientsView = RetUpdateDelClients.as_view()


class ProduitsListCreateAPIView(generics.ListCreateAPIView):
    '''
        View: get, post produits
    '''
    queryset = Produits.objects.all()
    serializer_class = ProduitsSerializer
    permission_classes = [permissions.IsAdminUser]
list_create_ProduitsAPIVIEW = ProduitsListCreateAPIView.as_view()

class RetUpdateDelProduits(generics.RetrieveUpdateDestroyAPIView):
    '''
        View pour put, patch, delete des produits 
    '''
    queryset = Produits.objects.all()
    serializer_class = ProduitsSerializer
    permission_classes = [permissions.IsAdminUser]
ret_upate_del_ProduitsView = RetUpdateDelProduits.as_view()


class TrajetsListCreateAPIView(generics.ListCreateAPIView):
    '''
        View: get, post Trajets
    '''
    queryset = Trajets.objects.all()
    serializer_class = TrajetsSerializer
    permission_classes = [permissions.IsAdminUser]
list_create_TrajetsAPIVIEW = TrajetsListCreateAPIView.as_view()

class RetUpdateDelTrajets(generics.RetrieveUpdateDestroyAPIView):
    '''
        View pour put, patch, delete des Trajets 
    '''
    queryset = Trajets.objects.all()
    serializer_class = TrajetsSerializer
    permission_classes = [permissions.IsAdminUser]
ret_upate_del_TrajetsView = RetUpdateDelTrajets.as_view()

class CategorieVehiculesListCreateAPIView(generics.ListCreateAPIView):
    '''
        View: get, post CategorieVehicules
    '''
    queryset = CategorieVehicules.objects.all()
    serializer_class = CategorieVehiculesSerializer
    permission_classes = [permissions.IsAdminUser]
list_create_CategorieVehiculesAPIVIEW = CategorieVehiculesListCreateAPIView.as_view()

class RetUpdateDelCategorieVehicules(generics.RetrieveUpdateDestroyAPIView):
    '''
        View pour put, patch, delete des CategorieVehicules 
    '''
    queryset = CategorieVehicules.objects.all()
    serializer_class = CategorieVehiculesSerializer
    permission_classes = [permissions.IsAdminUser]
ret_upate_del_CategorieVehiculesView = RetUpdateDelCategorieVehicules.as_view()

class VehiculeParcsListCreateAPIView(generics.ListCreateAPIView):
    '''
        View: get, post VehiculeParcs
    '''
    queryset = VehiculeParcs.objects.all()
    serializer_class = VehiculeParcsSerializer
    permission_classes = [permissions.IsAdminUser]
list_create_VehiculeParcsAPIVIEW = VehiculeParcsListCreateAPIView.as_view()

class RetUpdateDelVehiculeParcs(generics.RetrieveUpdateDestroyAPIView):
    '''
        View pour put, patch, delete des VehiculeParcs 
    '''
    queryset = VehiculeParcs.objects.all()
    serializer_class = VehiculeParcsSerializer
    permission_classes = [permissions.IsAdminUser]
ret_upate_del_VehiculeParcsView = RetUpdateDelVehiculeParcs.as_view()

class VehiculeLouesListCreateAPIView(generics.ListCreateAPIView):
    '''
        View: get, post VehiculeLoues
    '''
    queryset = VehiculeLoues.objects.all()
    serializer_class = VehiculeLouesSerializer
    permission_classes = [permissions.IsAdminUser]
list_create_VehiculeLouesAPIVIEW = VehiculeLouesListCreateAPIView.as_view()

class RetUpdateDelVehiculeLoues(generics.RetrieveUpdateDestroyAPIView):
    '''
        View pour put, patch, delete des VehiculeLoues 
    '''
    queryset = VehiculeLoues.objects.all()
    serializer_class = VehiculeLouesSerializer
    permission_classes = [permissions.IsAdminUser]
ret_upate_del_VehiculeLouesView = RetUpdateDelVehiculeLoues.as_view()


class ChauffeursListCreateAPIView(generics.ListCreateAPIView):
    '''
        View: get, post Chauffeurs
    '''
    queryset = Chauffeurs.objects.all()
    serializer_class = ChauffeursSerializer
    permission_classes = [permissions.IsAdminUser]
list_create_ChauffeursAPIVIEW = ChauffeursListCreateAPIView.as_view()

class RetUpdateDelChauffeurs(generics.RetrieveUpdateDestroyAPIView):
    '''
        View pour put, patch, delete des Chauffeurs 
    '''
    queryset = Chauffeurs.objects.all()
    serializer_class = ChauffeursSerializer
    permission_classes = [permissions.IsAdminUser]
ret_upate_del_ChauffeursView = RetUpdateDelChauffeurs.as_view()

class RecetteDetailPesageListCreateAPIView(generics.ListCreateAPIView):
    '''
        View: get, post RecetteDetailPesage
    '''
    queryset = RecetteDetailPesage.objects.all()
    serializer_class = RecetteDetailPesageSerializer
    permission_classes = [permissions.IsAdminUser]
list_create_RecetteDetailPesageAPIVIEW = RecetteDetailPesageListCreateAPIView.as_view()

class RetUpdateDelRecetteDetailPesage(generics.RetrieveUpdateDestroyAPIView):
    '''
        View pour put, patch, delete des RecetteDetailPesage 
    '''
    queryset = RecetteDetailPesage.objects.all()
    serializer_class = RecetteDetailPesageSerializer
    permission_classes = [permissions.IsAdminUser]
ret_upate_del_RecetteDetailPesageView = RetUpdateDelRecetteDetailPesage.as_view()


class documentVehiculesListCreateAPIView(generics.ListCreateAPIView):
    '''
        View: get, post documentVehicules
    '''
    queryset = documentVehicules.objects.all()
    serializer_class = documentVehiculesSerializer
    permission_classes = [permissions.IsAdminUser]
list_create_documentVehiculesAPIVIEW = documentVehiculesListCreateAPIView.as_view()

class RetUpdateDeldocumentVehicules(generics.RetrieveUpdateDestroyAPIView):
    '''
        View pour put, patch, delete des documentVehicules 
    '''
    queryset = documentVehicules.objects.all()
    serializer_class = documentVehiculesSerializer
    permission_classes = [permissions.IsAdminUser]
ret_upate_del_documentVehiculesView = RetUpdateDeldocumentVehicules.as_view()

class RecetteDetailSansPesageListCreateAPIView(generics.ListCreateAPIView):
    '''
        View: get, post RecetteDetailSansPesage
    '''
    queryset = RecetteDetailSansPesage.objects.all()
    serializer_class = RecetteDetailSansPesageSerializer
    permission_classes = [permissions.IsAdminUser]
list_create_RecetteDetailSansPesageAPIVIEW = RecetteDetailSansPesageListCreateAPIView.as_view()

class RetUpdateDelRecetteDetailSansPesage(generics.RetrieveUpdateDestroyAPIView):
    '''
        View pour put, patch, delete des RecetteDetailSansPesage 
    '''
    queryset = RecetteDetailSansPesage.objects.all()
    serializer_class = RecetteDetailSansPesageSerializer
    permission_classes = [permissions.IsAdminUser]
ret_upate_del_RecetteDetailSansPesageView = RetUpdateDelRecetteDetailSansPesage.as_view()


class MissionsListCreateAPIView(generics.ListCreateAPIView):
    '''
        View: get, post Missions
    '''
    queryset = Missions.objects.all()
    serializer_class = MissionsSerializer
    permission_classes = [permissions.IsAdminUser]
list_create_MissionsAPIVIEW = MissionsListCreateAPIView.as_view()

class RetUpdateDelMissions(generics.RetrieveUpdateDestroyAPIView):
    '''
        View pour put, patch, delete des Missions 
    '''
    queryset = Missions.objects.all()
    serializer_class = MissionsSerializer
    permission_classes = [permissions.IsAdminUser]
ret_upate_del_MissionsView = RetUpdateDelMissions.as_view()


class DepenseMissionsListCreateAPIView(generics.ListCreateAPIView):
    '''
        View: get, post DepenseMissions
    '''
    queryset = DepenseMissions.objects.all()
    serializer_class = DepenseMissionsSerializer
    permission_classes = [permissions.IsAdminUser]
list_create_DepenseMissionsAPIVIEW = DepenseMissionsListCreateAPIView.as_view()

class RetUpdateDelDepenseMissions(generics.RetrieveUpdateDestroyAPIView):
    '''
        View pour put, patch, delete des DepenseMissions 
    '''
    queryset = DepenseMissions.objects.all()
    serializer_class = DepenseMissionsSerializer
    permission_classes = [permissions.IsAdminUser]
ret_upate_del_DepenseMissionsView = RetUpdateDelDepenseMissions.as_view()

class LoueurVehiculesListCreateAPIView(generics.ListCreateAPIView):
    '''
        View: get, post LoueurVehicules
    '''
    queryset = LoueurVehicules.objects.all()
    serializer_class = LoueurVehiculesSerializer
    permission_classes = [permissions.IsAdminUser]
list_create_LoueurVehiculesAPIVIEW = LoueurVehiculesListCreateAPIView.as_view()

class RetUpdateDeLoueurVehicules(generics.RetrieveUpdateDestroyAPIView):
    '''
        View pour put, patch, delete des LoueurVehicules 
    '''
    queryset = LoueurVehicules.objects.all()
    serializer_class = LoueurVehiculesSerializer
    permission_classes = [permissions.IsAdminUser]
ret_upate_del_LoueurVehiculesView = RetUpdateDeLoueurVehicules.as_view()


class InfoDepenseMissionsListCreateAPIView(generics.ListCreateAPIView):
    '''
        View: get, post InfoDepenseMissions
    '''
    queryset = InfoDepenseMissions.objects.all()
    serializer_class = InfoDepenseMissionsSerializer
    permission_classes = [permissions.IsAdminUser]
list_create_InfoDepenseMissionsAPIVIEW = InfoDepenseMissionsListCreateAPIView.as_view()

class RetUpdateDeInfoDepenseMissions(generics.RetrieveUpdateDestroyAPIView):
    '''
        View pour put, patch, delete des InfoDepenseMissions 
    '''
    queryset = InfoDepenseMissions.objects.all()
    serializer_class = InfoDepenseMissionsSerializer
    permission_classes = [permissions.IsAdminUser]
ret_upate_del_InfoDepenseMissionsView = RetUpdateDeInfoDepenseMissions.as_view()