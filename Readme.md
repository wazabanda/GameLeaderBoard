
# Leader Board API by Waza_dev
## Introduction
so leader boards in games are nice but i have a tough time implementing premade ones cause my brain is small so i made my own for some reason.

This API uses Django and Django REST framework cause thats what I'm learning could have use Fast API though or flask i guess.

## How to SetUP
so you are free to host this for yourself and make changes its open source so you will have to follow the steps for your hosting site.
You can also just use my site (I'll add a link once everything is don lol)

I will make a Unity SDK implementation for this later.

The only Changes you have to make to the ``settings.py`` in the Database section and configure the values based on if you are using SQL or MONGODB or something else.

# API Endpoints
## {base route}/getBoardData/{token}/  *(GET REQUEST)* 

the base route is the route of your site and the `token` is the unique ID when you get make a board (not implemented right now). No more payload is needed for this route

## Some dummy data

    GET /getBoardData/<token>/
    {
        {
            "id": 1,
            "ownerName": "WazaBanda",
            "name": "Killer Shapes Board",
            "token": "waza",
            "visibility": "Public",
            "owner": 1,
            "entries": [
                {
                    "id": 2,
                    "scoreHolder": "mega",
                    "score": 5000000.0,
                    "phrase": "me",
                    "date": "2022-06-08T16:47:55.111000Z",
                    "LeaderBoard": 1
                },
                {
                    "id": 1,
                    "scoreHolder": "waza",
                    "score": 2000.0,
                    "phrase": "waza",
                    "date": "2022-06-08T16:23:37Z",
                    "LeaderBoard": 1
                }
            ]
        }
    }

## {base route}/addBoardItem/{token}/  *(POST REQUEST)* 
Similar to the previous end point and adds an item to a specific board. 
the payload is ->

## How to make the call


    POST /addBoardItem/<token>/
    {
    
    "scoreHolder":"-score holders name-",
    
    "score": "-score-",

    "phrase": "-a unique phrase for the users score to help replace-"
    }

links

https://www.youtube.com/c/wazaDev

https://wazadev-site.herokuapp.com/

https://ko-fi.com/wazadev47169