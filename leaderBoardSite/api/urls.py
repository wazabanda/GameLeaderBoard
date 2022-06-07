from math import ceil
from django.urls import path,include
from . import views as v
urlpatterns = [

    path("getBoardData/<token>/",v.getBoardData),
    path("addBoardItem/<token>/",v.addBoardItem)
]