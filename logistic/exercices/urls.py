from django.urls import path
from .views import (
   list_create_ExercicesView ,
   ret_upate_del_ExercicesView,
   exo_test
)

urlpatterns = [
    path('', list_create_ExercicesView, name="listerCreerExerrcice"),
    path('<int:pk>/detail', ret_upate_del_ExercicesView, name="DetailExerrcice"),
    path('exo/', exo_test, name="exo"),
]