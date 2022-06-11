from math import ceil
from django.urls import path,include
from . import views as v
urlpatterns = [
    path("",v.home),
    path("createBoard/",v.createLeaderBoard),
    path("viewBoards/",v.viewLeaderBoards),
    path("viewBoards/<int:id>/",v.viewLeaderBoard),
    path("userBoards/",v.viewUserLeaderBoards)
]