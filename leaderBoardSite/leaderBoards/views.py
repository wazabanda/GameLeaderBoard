from urllib import request
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseForbidden , HttpResponseRedirect
from .forms import LeaderBoardForm,LeaderBoardItemForm
from .models import LeaderBoard,LeaderBoardItem
from .utilities import Utilities as util
# API STUFF


#*Create your views here.
def home(response):
    return render(response,"home.html")
def createLeaderBoard(response):
    
    if response.method == "POST":
        form = LeaderBoardForm(response.POST)
        if form.is_valid():
            lb = form.save(commit=True)
            response.user.leaderBoard.add(lb)
            lb.ownerName = response.user.username
            lb.token = util.generateToken(response.user.username,lb.name,str(lb.id))
            lb.save()
    form = LeaderBoardForm()
    params = {"form":form}
    return render(response,"createBoard.html",params)
def viewLeaderBoards(response):
    lb = LeaderBoard.objects.all()

    params = {"boards":lb}
    return render(response,"listBoards.html",params)
def viewUserLeaderBoards(response):
    lb = response.user.leaderBoard.all()
    params = {"boards":lb}
    return render(response,"yourBoards.html",params)

def viewLeaderBoard(response,id):
    board = LeaderBoard.objects.get(pk = id)

    params = {
        "board": board
    }
    return render(response,"leaderBoardView.html",params)   

def deleteBoard(response,id):
    board:LeaderBoard = LeaderBoard.objects.get(pk=id)
    board.delete()
    lb = response.user.leaderBoard.all()
    params = {"boards":lb}
    return render(response,"yourBoards.html",params)