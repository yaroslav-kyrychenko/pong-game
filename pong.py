import turtle
from winsound import PlaySound, SND_ASYNC

window = turtle.Screen()
window.title("Pong Game")
window.bgcolor("white")
window.setup(width=800, height=600)
window.tracer(0)

# Left paddle
l_paddle = turtle.Turtle()
l_paddle.speed(0)
l_paddle.shape("square")
l_paddle.color("black")
l_paddle.shapesize(stretch_wid=5, stretch_len=1)
l_paddle.penup()
l_paddle.goto(-350, 0)

# Right paddle
r_paddle = turtle.Turtle()
r_paddle.speed(0)
r_paddle.shape("square")
r_paddle.color("black")
r_paddle.shapesize(stretch_wid=5, stretch_len=1)
r_paddle.penup()
r_paddle.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("black")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.7
ball.dy = 0.7

# Score of the game
score_a = 0
score_b = 0

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write(f"Player A: {score_a} - Player B: {score_b}", align="center",
          font=("Courier", 24, "normal"))

# Functions


def l_paddle_up():
    """Moves the left paddle 20 pixels up."""
    y = l_paddle.ycor()
    y += 20
    l_paddle.sety(y)


def l_paddle_down():
    """Moves the left paddle 20 pixels down."""
    y = l_paddle.ycor()
    y -= 20
    l_paddle.sety(y)


def r_paddle_up():
    """Moves the right paddle 20 pixels up."""
    y = r_paddle.ycor()
    y += 20
    r_paddle.sety(y)


def r_paddle_down():
    """Moves the right paddle 20 pixels down."""
    y = r_paddle.ycor()
    y -= 20
    r_paddle.sety(y)


def update_the_score():
    """Clears the default score and updates the score based on the results of the game."""
    pen.clear()
    pen.write(f"Player A: {score_a} - Player B: {score_b}", align="center",
              font=("Courier", 24, "normal"))


def make_sound():
    """Plays a vintage 8-bit bounce sound."""
    PlaySound("bounce.wav", SND_ASYNC)


# Keyboard binding
window.listen()
window.onkeypress(l_paddle_up, "w")
window.onkeypress(l_paddle_down, "s")
window.onkeypress(r_paddle_up, "Up")
window.onkeypress(r_paddle_down, "Down")

# Main game loop
while True:
    window.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Setting borders of the screen
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        make_sound()
    elif ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        make_sound()
    elif ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        make_sound()
        update_the_score()
    elif ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        make_sound()
        update_the_score()

    # Contact ball and paddle
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < r_paddle.ycor() + 40 and ball.ycor() > r_paddle.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1
        make_sound()

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < l_paddle.ycor() + 40 and ball.ycor() > l_paddle.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
        make_sound()
