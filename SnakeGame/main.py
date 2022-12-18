from snake import Snake
from turtle import Screen
import time
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(600, 600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.09)
    snake.snake_move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.clear()
        scoreboard.score_add()

    if snake.head.xcor() > 300 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -300:
        game_is_on = False
        scoreboard.game_over()

    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
