from django.urls import path
from .views import (
   list_create_ExercicesView ,
   ret_upate_del_ExercicesView
)

urlpatterns = [
    path('', list_create_ExercicesView, name="listerCreerExerrcice"),
    path('<int:pk>/update', ret_upate_del_ExercicesView, name="upateExerrcice"),
    path('<int:pk>/delete', ret_upate_del_ExercicesView, name="deleleExerrcice"),
]