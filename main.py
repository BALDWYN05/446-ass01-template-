# Dylan Baldwin
# CSCI 446 Fall 2026
# Programming Assignment #1
# I declare that I am the author of this work, take full responsibility for it, and have disclosed any material external assistance.

# Sources:
# I used https://www.w3schools.com/python/module_random.asp for help with the randomization.

import vacuum as vc
import grid as m
import random
import time

def main():
    # Sets Grid size and number of dirty tiles
    SIZE = 5
    DIRTY = random.randint(1, (SIZE - 1) **2)

    # Gives the vacuum a starting position
    jerryTheMouse = [random.randint(0,SIZE - 1), random.randint(0,SIZE - 1)]

    # Creates the grid
    grid = m.make_grid(SIZE, DIRTY)

    # Marks Start Time
    start = time.perf_counter()

    moves = 0
    dirtyCount = DIRTY

    m.print_grid_vac(grid, SIZE, jerryTheMouse)

    # While there are still dirty squares the Vacuum makes a move choice and tests to see if the tile is dirty
    while dirtyCount != 0:
        move = vc.moveChoice(jerryTheMouse, SIZE)
        match move:
            case "up":
                vc.moveUp(jerryTheMouse)

            case "down":
                vc.moveDown(jerryTheMouse)

            case "left":
                vc.moveLeft(jerryTheMouse)

            case "right":
                vc.moveRight(jerryTheMouse)
        m.print_grid_vac(grid, SIZE, jerryTheMouse)
        if grid[jerryTheMouse[1]][jerryTheMouse[0]] == 'D':
            vc.suck(jerryTheMouse, grid)
            dirtyCount -= 1
        moves += 1

    end = time.perf_counter() - start
    print(f"TIME : {end}")
    print(f"Moves: {moves}")
    m.print_grid_vac(grid, SIZE, jerryTheMouse)

if __name__ == "__main__":
    main()