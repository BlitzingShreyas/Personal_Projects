from turtle import Turtle

MOVE_DISTANCE = 20
UP=90
DOWN=270
RIGHT=0
LEFT=180
STARTING_POSITIONS=[(0,0),(-20,0),(-40,0)]

class Snake():
    def __init__(self):
        self.snake_list=[]
        self.create_snake()

    def create_snake(self):
        for pos in STARTING_POSITIONS:
            self.add_segment(pos)

    def add_segment(self,position):
        snake = Turtle()
        snake.shape("square")
        snake.color("white")
        snake.penup()
        snake.goto(position)
        self.snake_list.append(snake)

    def extend(self):
        self.add_segment(self.snake_list[-1].position())

    def move(self):

        for segment in range(len(self.snake_list)-1,0,-1):
            seg_x=self.snake_list[segment-1].xcor()
            seg_y=self.snake_list[segment-1].ycor()
            self.snake_list[segment].goto(seg_x,seg_y)
        self.snake_list[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.snake_list[0].heading() != DOWN:
            self.snake_list[0].setheading(UP)
        # self.snake_list[0].forward(20)

    def down(self):
        if self.snake_list[0].heading() != UP:
            self.snake_list[0].setheading(DOWN)
        # self.snake_list[0].forward(20)

    def right(self):
        if self.snake_list[0].heading() != LEFT:
            self.snake_list[0].setheading(RIGHT)
        # self.snake_list[0].forward(20)

    def left(self):
        if self.snake_list[0].heading() != RIGHT:
            self.snake_list[0].setheading(LEFT)
        # self.snake_list[0].forward(20)