#!/usr/bin/env python3

import random
import time

choices = ["Rock", "Paper", "Scissors"]

player_score = 0
enemy_score = 0

enemy_throw = random.choice(choices)
cont = "Y"
while cont == "Y" or cont == "y":
    print("Rock, Paper, Scissors.......")
    print("Player, maker your choice ")
    player_throw = input()
    time.sleep(2)
    print("Get ready!")
    time.sleep(2)
    print("3...")
    time.sleep(1)
    print("2...")
    time.sleep(1)
    print("1...")
    time.sleep(0.5)
    print("")
    print("")
    print(f"Computer threw {enemy_throw}!")

    while player_throw == enemy_throw:
        print("It's a tie! Throw again to settle a winner")
        print("Rock, Paper, Scissors.......")
        print("Player, maker your choice ")
        enemy_throw = random.choice(choices)
        player_throw = input()
        time.sleep(2)
        print("Get ready!")
        time.sleep(2)
        print("3...")
        time.sleep(1)
        print("2...")
        time.sleep(1)
        print("1...")
        time.sleep(0.5)
        print("")
        print("")
        print(f"Computer threw {enemy_throw}!")

    if (player_throw == "Rock" and enemy_throw == "Scissors") or (player_throw == "Paper" and enemy_throw == "Rock") or (player_throw == "Scissors" and enemy_throw == "Paper"):
        print("Player 1 wins!")
        player_score += 1
    else:
        print("Computer wins!")
        enemy_score += 1
    print("")
    print(f"Computer score: {enemy_score}\nPlayer score: {player_score}")

    print("")
    print("Continue playing?")
    cont = input()

print("")
print(f"High Scores:\nPlayer: {player_score}\nComputer: {enemy_score}")

if enemy_score > player_score:
    print("Better luck next time!")
else: 
    print("Well done!")
