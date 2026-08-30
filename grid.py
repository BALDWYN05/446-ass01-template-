# Dylan Baldwin
# CSCI 446 Fall 2026
# Programming Assignment #1
# I declare that I am the author of this work, take full responsibility for it, and have disclosed any material external assistance.

import random

def make_grid(SIZE, DIRTY):
    # Creates a size * size grid
    grid = [ [0 for _ in range(SIZE)] for _ in range(SIZE) ]

    # Makes an empty list named tiles to generate random locations
    # if the tile is already created it makes a new one

    tiles = []
    dirtyLeft = DIRTY
    while dirtyLeft != 0:
        x = random.randint(0,SIZE - 1)
        y = random.randint(0,SIZE - 1)
        loc = tuple([x,y])

        if(loc in tiles):
            continue
        else:
            tiles.append(loc)
            dirtyLeft -= 1
            
    # Sets the locations in tiles to be dirty     
    for tile in tiles:
        x = tile[0]; y = tile[1]
        grid[y][x] = "D"
    return grid

def print_grid(grid, SIZE):
    for y in range(SIZE):
        for x in range(SIZE):
            print(grid[y][x], end = " ")
        print()
    print()

def print_grid_vac(grid, SIZE, vacuum):
    for y in range(SIZE):
        for x in range(SIZE):
            if x == vacuum[0] and y == vacuum[1]:
                print('V', end = " ")
                continue
            print(grid[y][x], end = " ")
        print()
    print()