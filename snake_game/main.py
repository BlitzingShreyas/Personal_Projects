from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Score
import time

screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake=Snake()
food=Food()
score_card=Score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")
game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()
    # Detect food and extend the body of the snake
    if snake.snake_list[0].distance(food) < 15 :
        food.refresh()
        score_card.score_update()
        snake.extend()
    # Detect the wall and end the game if wall is detected
    if snake.snake_list[0].xcor() >280 or snake.snake_list[0].xcor() < -280 or snake.snake_list[0].ycor() >280 or snake.snake_list[0].ycor() < -280:
        game_is_on=False
        score_card.game_over()
    # End the game if you detect snake's own tail
    for seg in snake.snake_list[1:]:
        if snake.snake_list[0].distance(seg)<15:
                game_is_on=False
                score_card.game_over()
screen.exitonclick()