from rest_framework import serializers

from leaderBoards.models import LeaderBoard,LeaderBoardItem

class LeaderBoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeaderBoard
        fields = '__all__'
class LeaderBoardItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeaderBoardItem
        fields = '__all__'