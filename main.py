from turtle import Turtle,Screen
screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
starting_position = [(0,0),(-20,0),(-40,0)]
fragment = []
for i in starting_position:
    new_frag = Turtle("square")
    new_frag.color("white")
    new_frag.goto(i)
    fragment.append(new_frag)
















screen.exitonclick()