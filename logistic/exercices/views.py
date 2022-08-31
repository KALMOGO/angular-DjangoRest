from rest_framework import generics, permissions
from .models import Exercices
from .serializers import ExercicesSerializer

    # Seul l'administrateur doit pouvoir effectuer ces actions
    
class ListCreateExecices(generics.ListCreateAPIView):
    '''
        View pour get, post des exercices 
    '''
    queryset = Exercices.objects.all()
    serializer_class = ExercicesSerializer
    permission_classes = [permissions.IsAdminUser]

    def perform_create(self, serializer):
        '''
            sauvegarder celui qui a creer l'exercice
        '''
        serializer.save(createur=self.request.user)

list_create_ExercicesView = ListCreateExecices.as_view()

class RetUpdateDelExercices(generics.RetrieveUpdateDestroyAPIView):
    '''
        View pour put, patch, delete des exercices 
    '''
    queryset = Exercices.objects.all()
    serializer_class = ExercicesSerializer
    permission_classes = [permissions.IsAdminUser]

ret_upate_del_ExercicesView = RetUpdateDelExercices.as_view()