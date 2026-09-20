import os
import turtle
import random
import time

# 2 = wall, 0 = open path, 1 = player, 3 = exit
myarr = []
col = 1
row = 1
turtle.hideturtle()

script_dir = os.path.dirname(os.path.abspath(__file__))
map_file_path = os.path.join(script_dir, "map.txt")

def maze_generation(cols, rows):
    width = cols * 2 + 1
    height = rows * 2 + 1
    grid = [["2"] * width for i in range(height)]
    visited =[[False] * cols for i in range(rows)]

    def cell_to_grid(cx, cy):
        return (2 * cy + 1, 2 * cx + 1)

    stack = [(0, 0)]
    visited[0][0] = True
    row, col = cell_to_grid(0, 0)
    grid[row][col] = "1"
    last_cell = (0, 0)
    # directions = [(-1, 0), (1, 0), (0, -1), (0,1)]
    #left =	cx - 1, cy
    #right = cx + 1, cy
    #up	= cx, cy - 1
    # down = cx, cy + 1

    while stack:
        cx, cy = stack[-1]
        neighbours = []
        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < cols and 0<= ny < rows and not visited[ny][nx]:
                neighbours.append((nx, ny, dx, dy))
                # even rows/columns are cells, odd rows/columns are walls

        if neighbours:
            nx, ny, dx, dy = random.choice(neighbours)
            visited[ny, nx] = True
            row, col = cell_to_grid(cx, cy)
            grid[row + dy][col + dx] = "0"
            nr, nc = cell_to_grid(nx, ny)
            grid[nr][nc] = "0"
            stack.append((nx, ny))
            last_cell(nx, ny)
        else:
            stack.pop()
    exit_row, exit_col = cell_to_grid(last_cell)     
    grid[exit_row][exit_col] = "3"
        

    return grid

def drawSquare(x, y, side, colour):
    turtle.up()
    turtle.goto(x, y)
    if (not colour == "none"):
        turtle.color(colour)
        turtle.begin_fill()
        for x in range(4):
            turtle.forward(side)
            turtle.right(90)
        turtle.end_fill()

def drawMap():
    x = -120
    y = 60
    originalX = -120
    side = 10

    turtle.tracer(0, 0)
    for arr in myarr:
        for value in arr:
            if value == "0":
                drawSquare(x, y, side, "green")
            elif value == "1":
                drawSquare(x, y, side, "yellow")
            elif value == "2":
                drawSquare(x, y, side, "red")
            elif value == "\n":
                drawSquare(x, y, side, "none")
            else:
                drawSquare(x, y, side, "black")
            x += side
        y -= side
        x = originalX
    turtle.update()

drawMap()

def up():
    global myarr
    global row
    global col
    if (myarr[row - 1][col] == "0"):
        myarr[row][col] = "0"
        row -= 1
        if myarr[row][col] == "3":
            next_level()
            return
        myarr[row][col] = "1"
    turtle.clear()
    drawMap()

def down():
    global myarr
    global row
    global col
    if (myarr[row + 1][col] == "0"):
        myarr[row][col] = "0"
        row += 1
        if myarr[row][col] == "3":
                next_level()
                return
        myarr[row][col] = "1"
    turtle.clear()
    drawMap()

def left():
    global myarr
    global row
    global col
    if (myarr[row][col - 1] == "0"):
        myarr[row][col] = "0"
        col -= 1
        if myarr[row][col] == "3":
                next_level()
                return
        myarr[row][col] = "1"
    turtle.clear()
    drawMap()

def right():
    global myarr
    global row
    global col
    if (myarr[row][col + 1] == "0"):
        myarr[row][col] = "0"
        col += 1
        if myarr[row][col] == "3":
                next_level()
                return
        myarr[row][col] = "1"
    turtle.clear()
    drawMap()

# turtle movement using keys
turtle.onkey(up, "w")
turtle.onkey(left, "a")
turtle.onkey(down, "s")
turtle.onkey(right, "d")
turtle.onkey(up, "Up")
turtle.onkey(left, "Left")
turtle.onkey(down, "Down")
turtle.onkey(right, "Right")

turtle.listen()
turtle.mainloop()
