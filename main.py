import turtle
from turtle import Screen
from snake import Snake
from food import Food
from score import Score

import time
screen = Screen()

screen.setup(width=600,height=600)
screen.bgcolor("white")
screen.tracer(0)
screen.listen()


snake = Snake()
food = Food()
score = Score()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")




is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.ScoreAdd()


    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        is_game_on = False
        score.Game_over()

    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            is_game_on = False
            score.Game_over()


















screen.exitonclick()