from turtle import Screen
from paddle import Paddle

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Juega al Pong")
screen.tracer(0)  # Desactivamos la actualización automática de la pantalla

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")

# Mostrar los paddles después de configurar los eventos
r_paddle.showturtle()
l_paddle.showturtle()

is_game_on = True
while is_game_on:
    screen.update()

screen.exitonclick()
