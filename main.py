from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

my_screen = Screen()
my_screen.setup(width=600, height=600)
my_screen.tracer(0)
my_screen.bgcolor("black")
my_screen.title("SNAKE")

# using event listeners to control the snake

snake = Snake()
food = Food()
scoreboard = ScoreBoard()


my_screen.listen()

my_screen.onkey(key="Up", fun=snake.up)
my_screen.onkey(key="Down", fun=snake.down)
my_screen.onkey(key="Left", fun=snake.left)
my_screen.onkey(key="Right", fun=snake.right)


game_running = True
while game_running:
    my_screen.update()
    time.sleep(0.05)
    snake.move()

    # detecting collision with food
    if snake.head.distance(food) < 18:
        food.refresh()
        snake.extend()
        scoreboard.update_score()

    # detect collision with wall
    if snake.head.xcor() > 285 or snake.head.xcor() < -285 or snake.head.ycor() > 285 or snake.head.ycor() < -285:
        # game_running = False
        snake.restart_snake()

        scoreboard.reset_score()

    # detect collision with tail

    for i in snake.segments[1:]:
        if snake.head.distance(i) < 8:
            # game_running = False
            snake.restart_snake()
            scoreboard.reset_score()








my_screen.exitonclick()


