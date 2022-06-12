from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.decorators import api_view
from leaderBoards.models import LeaderBoard,LeaderBoardItem
from .serializers import LeaderBoardSerializer,LeaderBoardItemSerializer
#*API ROUTES
@api_view(["GET"])
def getBoardData(response,token):
    board = LeaderBoard.objects.get(token=token)
    res1 = LeaderBoardSerializer(board, many = False)
    res2 = LeaderBoardItemSerializer(board.leaderBoardItems.all(), many=True)
    serializer = res1.data
    serializer['entries'] = res2.data
    return Response(serializer)

@api_view(["POST"])
def addBoardItem(request,token):
    ser = LeaderBoardItemSerializer(data=request.data)
    if ser.is_valid():
        board = LeaderBoard.objects.get(token=token)
        t = ser.save()
        board.leaderBoardItems.add(t)
        t.save()
    return Response(ser.data)

