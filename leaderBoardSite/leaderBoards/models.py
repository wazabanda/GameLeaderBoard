from random import choices
from django.db import models
from django.contrib.auth.models import User
import  datetime as dt
# Create your models here.

visibilityChoices = [("Public","Public"),("Private","Private")]
class LeaderBoard(models.Model):
    owner = models.ForeignKey(User,on_delete=models.CASCADE,related_name="leaderBoard",null=True)
    ownerName = models.CharField(max_length = 150)
    name = models.CharField(max_length = 200)
    token = models.CharField(max_length = 200,unique = True,null=True)
    visibility = models.CharField(max_length = 20,choices=visibilityChoices,blank = True)

class LeaderBoardItem(models.Model):
    
    LeaderBoard = models.ForeignKey(LeaderBoard,on_delete=models.CASCADE,related_name="leaderBoardItems",null = True)
    scoreHolder = models.CharField(max_length = 20)
    score = models.FloatField()
    phrase = models.CharField(max_length = 20)
    date = models.DateTimeField(default=dt.datetime.utcnow)

    class Meta:
        ordering = ["-score"]