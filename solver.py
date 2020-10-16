import numpy as np
from random import shuffle, randint

grid = np.array([[0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0]])

zgrid = np.array([[0,0,0,0,2,4,3,0,7],
                 [9,0,0,0,6,0,0,0,0],
                 [7,0,0,0,0,0,0,0,0],
                 [0,0,0,5,0,0,7,9,4],
                 [0,6,5,0,0,0,0,0,0],
                 [0,0,0,8,0,3,0,0,0],
                 [0,5,4,0,0,0,0,6,0],
                 [0,0,0,0,0,0,0,5,9],
                 [0,0,3,4,0,8,0,0,0]])

new_grid = np.array([[]])

numberList = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def possible(y, x, n) :
    global grid
    for i in range(0, 9) :
        if grid[y][i] == n :
            return False
    for i in range(0, 9) :
        if grid[i][x] == n :
            return False
    x0 = (x//3)*3
    y0 = (y//3)*3
    for i in range(3) :
        for j in range(3) :
            if grid[y0+i][x0+j] == n :
                return False
    return True

def fullCheck(grid) :
    for i in range(9) :
        for j in range(9) :
            if grid[i][j] == 0 :
                return False
    return True

def fill(grid) :
    global numberList
    for i in range(0, 9) :
        for j in range(0, 9) :
            if grid[i][j] == 0 :
                shuffle(numberList)
                for n in numberList :
                    if possible(i, j, n) :
                        grid[i][j] = n
                        if fullCheck(grid) :
                            # print(grid)
                            return True
                        if fill(grid) :
                            return True
                        grid[i][j] = 0
                return False

counter = 1

def solve(grid) :
    global counter
    global numberList
    for i in range(0, 9) :
        for j in range(0, 9) :
            if grid[i][j] == 0 :
                shuffle(numberList)
                for n in numberList :
                    if possible(i, j, n) :
                        grid[i][j] = n
                        if fullCheck(grid) :
                            counter += 1
                            print(grid)
                            return True
                        if fill(grid) :
                            return True
                        # grid[i][j] = 0
                return False
    grid[i][j] = 0

# fill(grid)
# print(grid)

solve(grid)
print(grid)