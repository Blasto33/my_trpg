#!/usr/bin/python3

from os import system
import os
import time
import json
from game import launch_new_game

def check_save():
    f = None

    print("Loading saves", end='', flush=True)
    time.sleep(1)
    print(".", end='', flush=True)
    time.sleep(1)
    print(".", end='', flush=True)
    time.sleep(1)
    print(".", flush=True)
    try :
        f = open("save1.json", "r")
    except FileNotFoundError :
        print("No save file found, creating a new one...")
        f = open("save1.json", "w")
        time.sleep(1)
        print("Save file created!")

def init_game():
    time.sleep(0.5)
    print("Initializing game...");
    time.sleep(1)
    check_save()
    print("Initialization complete!")
    time.sleep(0.25)
    system('clear')

def main_menu():
    choice = 0
    valid_choice = False

    print("Hello adventurer! What do you want to do today?")
    print("1 - Go on a new adventure")
    print("2 - Continue an existing adventure")
    print("3 - Settings")
    print("4 - Exit")
    choice = input()
    while valid_choice == False:
        try :
            val = int(choice)
        except ValueError: 
            print("You have to type a number!")
            time.sleep(1)
            system('clear')
            print("Hello adventurer! What do you want to do today?")
            print("1 - Go on a new adventure")
            print("2 - Continue an existing adventure")
            print("3 - Settings")
            print("4 - Exit")
            choice = input()
        else:
            valid_choice = True
    if val == 1:
        launch_new_game()

if __name__ == '__main__':
    init_game()
    main_menu()