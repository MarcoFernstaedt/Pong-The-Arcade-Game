from turtle import Screen, Turtle, width

from numpy import pad

screen = Screen()
screen.setup(800, 600)
screen.bgcolor('black')
screen.title('Pong')
screen.tracer(0)

screen.listen()
screen.onkey(go_up, 'Up')
screen.onkey(go_down, 'Down')

game_is_on = True
while game_is_on:
    screen.update()


screen.exitonclick()