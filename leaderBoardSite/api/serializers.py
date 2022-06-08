from rest_framework import serializers,status, permissions
from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from rest_framework.views import APIView
from leaderBoards.models import LeaderBoard,LeaderBoardItem

class LeaderBoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeaderBoard
        fields = '__all__'
class LeaderBoardItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeaderBoardItem
        fields = '__all__'