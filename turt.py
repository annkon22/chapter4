import turtle

my_turtle = turtle.Turtle()
my_win = turtle.Screen()

def draw_spiral(my_turtle, line_len):
    if line_len > 0:
        my_turtle.forward(line_len)
        my_turtle.right(90)
        draw_spiral(my_turtle, line_len -5)

#draw_spiral(my_turtle, 100)
#my_win.exitonclick()

def tree(branch_len, t):   #how to control the width so the line doesn't disappear
    if branch_len > 5:
        t.forward(branch_len)
        t.right(20)
        tree(branch_len - 15, t)
        t.width(t.width() - 1)
        t.left(40)
        tree(branch_len -10, t)
        t.right(20)
        t.backward(branch_len)
        t.width(t.width() + 1)


def main():
    t = turtle.Turtle()
    my_win = turtle.Screen()
    t.width(10)
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color('brown')
    tree(75, t)
    my_win.exitonclick()

#main()




###############################################
###############################################
# THE SIERPINSKI TRIANGLE #

def draw_triangle(points, color, my_turtle):
    my_turtle.fillcolor(color)
    my_turtle.up()
    my_turtle.goto(points[0][0], points[0][1])
    my_turtle.down()
    my_turtle.begin_fill()
    my_turtle.goto(points[1][0], points[1][1])
    my_turtle.goto(points[2][0], points[2][1])
    my_turtle.goto(points[0][0], points[0][1])
    my_turtle.end_fill()

def get_mid(p1, p2):
    return ((p1[0] + p2[0]) / 2, (p1[1] +p2[1]) / 2)

def sierpinski(points, degree, my_turtle):
    color_map = ['blue', 'red', 'green', 'white', 'yellow', 'violet', 'orange']
    draw_triangle(points, color_map[degree], my_turtle)
    if degree > 0:
        sierpinski([points[0],
        get_mid(points[0], points[1]), 
        get_mid(points[0], points[2])],
        degree - 1, my_turtle)

        sierpinski([points[1],
        get_mid(points[0], points[1]),
        get_mid(points[1], points[2])],
        degree - 1, my_turtle)

        sierpinski([points[2],
        get_mid(points[2], points[1]),
        get_mid(points[0], points[2])],
        degree -1, my_turtle)

    
def main1():
    my_turtle = turtle.Turtle()
    my_win = turtle.Screen()
    my_points = [[-100, -50], [0, 100], [100, -50]]
    sierpinski(my_points, 3, my_turtle)
    my_win.exitonclick()

#main1()


########################################################
########       THE TOWERS OF HANOI          ############
########################################################


def move_tower(height, from_pole, to_pole, with_pole):
    if height >= 1:
        move_tower(height - 1, from_pole, with_pole, to_pole)
        move_tower(height - 1, from_pole, with_pole, to_pole)
        move_tower(height - 1, with_pole, to_pole, from_pole)


def move_disk(fp, tp):
    print('moving disk from', fp, 'to', tp)

#move_tower(3, 'A', 'B', 'C')




###########################################################
###########               MAZE            ################# 
###########################################################




PART_OF_PATH = 'O'
TRIED = '.'
OBSTACLE = '+'
DEAD_END = '-'

class Maze:
    def __init__(self, maze_file_name):
        rows_in_maze = 0
        columns_in_maze = 0
        self.maze_list = []
        maze_file = open(maze_file_name, 'r')
        rows_in_maze = 0
        for line in maze_file:
            row_list = []
            col = 0
            for ch in line[: -1]:
                row_list.append(ch)
                if ch == 'S':
                    self.start_row = rows_in_maze
                    self.start_col = col
                col += 1
            rows_in_maze = rows_in_maze + 1
            self.maze_list.append(row_list)
            columns_in_maze = len(row_list)
        
        self.rows_in_maze = rows_in_maze
        self.columns_in_maze = columns_in_maze
        self.x_translate = - columns_in_maze / 2
        self.y_translate = rows_in_maze / 2
        self.t = turtle.Turtle()
        self.t.shape('turtle')
        self.wn = turtle.Screen()
        self.wn.setworldcoordinates(- (columns_in_maze - 1) / 2 - .5, 
        - (rows_in_maze - 1) / 2 - .5, 
        (columns_in_maze -1) / 2 + .5, 
        (rows_in_maze - 1) / 2 + .5) 


    def draw_maze(self):
        self.t.speed(10)
        for y in range(self.rows_in_maze):
            for x in range(self.columns_in_maze):
                if self.maze_list[y][x] == OBSTACLE:
                    self.draw_centered_box(x + self.x_translate,
                    - y + self.y_translate, 'orange')
        self.t.color('black')
        self.t.fillcolor('blue')


    def draw_centered_box(self, x, y, color):
        self.t.up()
        self.t.goto(x - .5, y - .5)
        self.t.color(color)
        self.t.fillcolor(color)
        self.t.setheading(90)
        self.t.down()
        self.t.begin_fill()
        
        for i in range(4):
            self.t.forward(1)
            self.t.right(90)

        self.t.end_fill()


    def move_turtle(self, x, y):
        self.t.up()
        self.t.setheading(self.t.towards(x + self.x_translate, - y + self.y_translate))
        self.t.goto(x + self.x_translate, - y + self.y_translate)

    def drop_bread_crumb(self, color):
        self.t.dot(10, color)

    def update_position(self, row, col, val = None):
        if val:
            self.maze_list[row][col] = val
        self.move_turtle(col, row)

        if val == PART_OF_PATH:
            color = 'green'
        elif val == OBSTACLE:
            color = 'red'
        elif val == TRIED:
            color = 'black'
        elif val == DEAD_END:
            color = 'red'
        else:
            color = None
            
        if color:
            self.drop_bread_crumb(color)

    
    def is_exit(self, row, col):
        return (row == 0 or
        row == self.rows_in_maze - 1 or
        col == 0 or
        col == self.columns_in_maze - 1)

    def __getitem__(self, idx):
        return self.maze_list[idx]

    
def search_from(maze,start_row, start_column):
        #try each of four directions from this point untill
        #we find a way out

        # base Case return values:
        #1. We have run into an obstacle, retun false
    maze.update_position(start_row, start_column)
    if maze[start_row][start_column] == OBSTACLE:
        return False
        #2. We have found a square that has already been explored
    if maze[start_row][start_column] == TRIED or maze[start_row][start_column] == DEAD_END:
        return False

        #3. We have found an outside edge not occupied by an obstacle
    if maze.is_exit(start_row,start_column):
        maze.update_position(start_row, start_column, PART_OF_PATH)
        return True
    maze.update_position(start_row, start_column, TRIED)

        #Otherwise, use logical shortcircuiting to try each direction
        #in turn (if needed)

    found = search_from(maze, start_row - 1, start_column) or \
    search_from(maze, start_row + 1, start_column) or \
    search_from(maze, start_row, start_column - 1) or \
    search_from(maze, start_row, start_column + 1)

    if found:
        maze.update_position(start_row, start_column, PART_OF_PATH)
    else:
        maze.update_position(start_row, start_column, DEAD_END)
    return found

my_maze = Maze('maze2.txt')
my_maze.draw_maze()
my_maze.update_position(my_maze.start_row, my_maze.start_col)

search_from(my_maze, my_maze.start_row, my_maze.start_col)
        




