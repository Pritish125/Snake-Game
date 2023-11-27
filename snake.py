from turtle import Turtle, Screen
import time
my_screen = Screen()

SEGMENTS_COORDINATES = [(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE = 10
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:

    def __init__(self):

        self.segments = []
        self.make()
        self.head = self.segments[0]

    # code below is to create the snake body

    def make(self):
        for i in SEGMENTS_COORDINATES:
            self.add_segment(i)


    def add_segment(self, position):

        turtle = Turtle("square")
        turtle.color("white")
        turtle.penup()
        turtle.goto(position)
        self.segments.append(turtle)


    # to add a new segment everytime we score a point
    def extend(self):
        self.add_segment(self.segments[-1].position())






    # code below is to make the snake body move as a linked object rather than separate segments
    def move(self):

        for i in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[i - 1].xcor()
            new_y = self.segments[i - 1].ycor()
            self.segments[i].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
            self.move()

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
            self.move()

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
            self.move()

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
            self.move()

    def restart_snake(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.make()
        self.head = self.segments[0]
