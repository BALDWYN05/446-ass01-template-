# Dylan Baldwin
# CSCI 446 Fall 2026
# Programming Assignment #1
# I declare that I am the author of this work, take full responsibility for it, and have disclosed any material external assistance.

import random

def moveUp(vacuum):
    vacuum[1] += 1

def moveDown(vacuum):
    vacuum[1] -= 1


def moveLeft(vacuum):
    vacuum[0] -= 1


def moveRight(vacuum):
    vacuum[0] += 1


def suck(vacuum , grid):
    grid[vacuum[1]][vacuum[0]] = '0'

def moveChoice(vacuum, SIZE):
    move = random.choice(["up", "down", "left", "right"])
    match move:
        case "up":
            if vacuum[1] == SIZE - 1:
                return moveChoice(vacuum, SIZE)

        case "down":
            if vacuum[1] == 0:
                return moveChoice(vacuum, SIZE)
            
        case "left":
            if vacuum[0] == 0:
                return moveChoice(vacuum, SIZE)
            
        case "right":
            if vacuum[0] == SIZE - 1:
                return moveChoice(vacuum, SIZE)
    return move