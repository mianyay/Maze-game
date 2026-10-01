import turtle
import random
import time

# 2 = wall, 0 = open path, 1 = player, 3 = exit
col = 1
row = 1
level = 1
turtle.hideturtle()
turtlepen = turtle.Turtle()
turtlepen.penup()
turtlepen.color("black")
turtlepen.hideturtle()

directions = [(-1, 0), (1, 0), (0, -1), (0,1)]

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
            visited[ny][nx] = True
            row, col = cell_to_grid(cx, cy)
            grid[row + dy][col + dx] = "0"
            nr, nc = cell_to_grid(nx, ny)
            grid[nr][nc] = "0"
            stack.append((nx, ny))
            last_cell = (nx, ny)
        else:
            stack.pop()
    exit_row, exit_col = cell_to_grid(last_cell[0], last_cell[1])     
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

myarr = maze_generation(4 + level, 4 + level)

def drawMap():
    width_maze = len(myarr[0])
    height_maze = len(myarr)
    side = min(700 / width_maze, 650 / height_maze)

    x = -(width_maze * side) / 2
    y = (height_maze * side) / 2
    originalX = x


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
            elif value == "3":
                drawSquare(x, y, side, "blue")
            else:
                drawSquare(x, y, side, "black")
            x += side
        y -= side
        x = originalX
    turtle.update()

def level_text():
        global level
        turtlepen.clear()
        turtlepen.goto(0, 340)
        turtlepen.write(f"Level {level}", align="center", font=("Sans Serif", 16, "bold"))
drawMap()

def next_level():
    global myarr, row, col, level
    level += 1
    turtle.title(f"Maze Level: Level {level}")
    cols = 4 + level
    rows = 4 + level

    myarr = maze_generation(cols, rows)
    row, col = 1, 1

    turtle.clear()
    drawMap()
    level_text()

def up():
    global myarr
    global row
    global col
    if myarr[row - 1][col] in ("0", "3"):
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
    if myarr[row + 1][col] in ("0", "3"):
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
    if myarr[row][col - 1] in ("0", "3"):
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
    if myarr[row][col + 1] in ("0", "3"):
        myarr[row][col] = "0"
        col += 1
        if myarr[row][col] == "3":
                next_level()
                return
        myarr[row][col] = "1"
    turtle.clear()
    drawMap()

# turtle continous movement
key_hold = set()

def key_down(key):
    key_hold.add(key)

def key_up(key):
    key_hold.discard(key)

for key in ("w", "a", "s", "d", "Up", "Down", "Left", "Right"):
    turtle.onkeypress(lambda k=key: key_down(k), key)
    turtle.onkeyrelease(lambda k=key: key_up(k), key)

def loop_game():
    if "w" in key_hold or "Up" in key_hold:
        up()
    elif "s" in key_hold or "Down" in key_hold:
        down()
    elif "d" in key_hold or "Right" in key_hold:
        right()
    elif "a" in key_hold or "Left" in key_hold:
        left()

    turtle.ontimer(loop_game, 150)

turtle.listen()
loop_game()
turtle.mainloop()
