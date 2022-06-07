from dataclasses import fields
from django.forms import  ModelForm, models
from .models import LeaderBoard,LeaderBoardItem

class LeaderBoardForm(ModelForm):

    class Meta:
        model = LeaderBoard
        fields = ["name","visibility"]

class LeaderBoardItemForm(ModelForm):

    class Meta:
        model = LeaderBoardItem
        fields = ["score", "scoreHolder","phrase"]