from turtle import Turtle
STARTING_POSITIONS = [(0,0),(-20,0),(-40,0)]
MOVE_DIST = 20

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):
        for position in STARTING_POSITIONS:
            new_seg = Turtle("square")
            new_seg.penup()
            new_seg.color("black")
            new_seg.goto(position)
            self.segments.append(new_seg)

    def move(self):
        for seg_num in range(2, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DIST)

    def up(self):
        self.segments[0].left(90)
