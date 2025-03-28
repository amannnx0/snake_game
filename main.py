from turtle import Turtle,Screen
import time
screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("gray")
screen.tracer(0)
starting_position = [(0,0),(-20,0),(-40,0)]
segments = []

for position in starting_position:
    new_seg = Turtle("square")
    new_seg.penup()
    new_seg.color("black")
    new_seg.goto(position)
    segments.append(new_seg)


def forward():
    segments[0].forward(20)
is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    screen.listen()
    screen.onkey(forward,"g")
    for seg_num in range(2,0,-1):
        new_x = segments[seg_num-1].xcor()
        new_y = segments[seg_num-1].ycor()
        segments[seg_num].goto(new_x,new_y)













screen.exitonclick()