import random
import os
import time

def wonCase(rNumber):
    os.system("cls")
    print("Good job, you've done it! The number was {}!".format(rNumber))

def mainGame(rNumber, lE, rE):
    os.system("cls")
    print("Try to guess a number between {} and {}...".format(lE, rE))

    while int(input()) != rNumber:
        print("Wrong! Try again!")

    wonCase(rNumber)

def startNewGame():
    os.system("cls")
    print("Give me a left edge of your desired przedział: ")
    leftE = int(input())
    print("Give me a right edge of your desired przedział: ")
    rightE = int(input())
    randomizedNumber = random.randint(leftE, rightE)

    mainGame(randomizedNumber, leftE, rightE)

def showExtras():
    os.system("cls")
    print("Made by Paweł Kupczak on 25th Listopad 2016")
    timer = time.time()

    while True:
        if time.time() - timer > 2:
            break

def menuInterface(choice):
    if choice != 1 and choice != 2 and choice != 3:
        return False

    if choice == 1:
        startNewGame()
    elif choice == 2:
        showExtras()
    elif choice == 3:
        exit()

    return True

def showMenu():
    os.system("cls")
    print("Welcome to my game! You have to guess the number between the values of your choice.")
    print("[1]. Start new game")
    print("[2]. Extras")
    print("[3]. Exit")

    while not menuInterface(int(input())):
        print("There's no option with this number!")

showMenu()