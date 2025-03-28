from turtle import Turtle,Screen
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
    screen.update()


is_game_on = True
while is_game_on:
    for seg in segments:
        seg.forward(20)








screen.exitonclick()