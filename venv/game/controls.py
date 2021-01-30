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
actionCheck = ["w","a","s","d","i","e","z","o","q"]
x = 0
y = 0
message = ''
movMessage =''
keyPosX =5
keyPosY = 5
keyInInv = 0
game_over = False

def barriersCheck(playerAction):
    global keyInInv, x, y, movMessage, game_over
    if playerAction == "w":
        if y < 10:
            y = y + 1
            movMessage =actionList[playerAction]
        else:
            movMessage = "Koniec mapy!"

    if playerAction == "a":
        if x > -10:
            x = x - 1
            movMessage =actionList[playerAction]
        else:
            movMessage = "Koniec mapy!"

    if playerAction == "s":
        if y > -10:
            y = y - 1
            movMessage =actionList[playerAction]
        else:
            movMessage("Koniec mapy!")

    if playerAction == "d":
        movMessage = actionList[playerAction]
        if y == 5 and x < 10:
            movMessage =actionList[playerAction]
        x = x + 1

    if playerAction == "i":
        movMessage = "x" + str(x) + "y" + str(y)

    if playerAction == "e":
        if keyInInv == 1:
            movMessage = "Masz przy sobie klucz"
        else:
            movMessage = "Nic tu nie ma"

    if playerAction == "z":
        zapis = "zapis.txt"
        o = open(zapis, "w")
        o.write(str(x))
        o.write("\n")
        o.write(str(y))
        o.write("\n")
        o.write(str(keyInInv))
        o.close()
        movMessage = "Zapisano!"

    if playerAction == "o":
        zapis = "zapis.txt"
        o = open(zapis, "r")
        xO = o.readline()
        x = int(xO)
        yO =o.readline()
        y = int(yO)
        keyInInvO = o.readline()
        keyInInv = int(keyInInvO)
        o.close()


    if playerAction == "q":
        pygame.quit()
        quit()

    if keyPosX == y and keyPosX == x and keyInInv == 0:
        movMessage = "Znalazłeś klucz"
        keyInInv = 1

    if x == 10 and y == 5:
        movMessage = "Otwórz"

    if x == 11 and y == 5:
        if keyInInv == 1:
            pygame.quit()
            quit()
        else:
            movMessage = "Zamknięte!"
            x = x - 1

def playerStatus(xStr,yStr):
    global message
    message = "Twoja aktualna pozycja to x:" + xStr + "y:" + yStr
    if(x==10 or x == -10 or y==10 or y== -10):
        message = "Koniec mapy!"



def movement(playerAction):
    playerAction = playerAction.lower()
    global keyInInv, x, y, movMessage,game_over

    if playerAction in actionCheck:
        barriersCheck(playerAction)
    else:
        message="Koniec mapy!"



