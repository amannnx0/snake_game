from turtle import Turtle,Screen
from snake import Snake
import time
screen = Screen()

screen.setup(width=600,height=600)
screen.bgcolor("gray")
screen.tracer(0)
screen.listen()


snake = Snake()
screen.onkey(snake.up,"Up")




is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
















screen.exitonclick()