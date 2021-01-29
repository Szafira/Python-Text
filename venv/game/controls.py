# Ten plik zajmuje się definiowaniem klas związanych ze sterowaniem i odczytaniem współrzędnych gracza.
# Gra korzysta jedynie z dwóch wymiarów

import pygame
from game.status import *
#Switch Case (dictionary)
actionList = {
            'w': "Góra",
            's': "Dół",
            'd': "Prawo",
            'a': "Lewo",
            'i': "check"
            }
actionCheck = ["w","a","s","d","i"]
x = 0
y = 0
message = ''

def barriersCheck(playerAction):
    global x
    global y
    if playerAction == "w":
        if y < 10:
            y = y + 1
            print(actionList[playerAction])
        else:
            print("Koniec mapy!")

    if playerAction == "a":
        if x > -10:
            x = x - 1
            print(actionList[playerAction])
        else:
            print("Koniec mapy!")

    if playerAction == "s":
        if y > -10:
            y = y - 1
            print(actionList[playerAction])
        else:
            print("Koniec mapy!")

    if playerAction == "d":
        if x < 10:
            x = x + 1
            print(actionList[playerAction])
        else:
            print("Koniec mapy!")

    if (playerAction == "i"):
        print(x, "x")
        print(y, "y")


def playerStatus(xStr,yStr):
    global message
    message = "Twoja aktualna pozycja to x:" + xStr + "y:" + yStr
    if(x==10 or x == -10 or y==10 or y== -10):
        message = "Koniec mapy!"



def movement(playerAction):
    playerAction = playerAction.lower()
    global x
    global y
    if playerAction in actionCheck:
        barriersCheck(playerAction)
    else:
        message="Koniec mapy!"



