import time
import turtle
import random


# Global Variables

delay = 0.1

# Main Window

mw = turtle.Screen()
mw.title("DangerNoodle!")
mw.setup(600, 600)
mw.bgcolor("black")
mw.tracer()


# Functions
def go_up():
    if head.lastdirection != "down":
        head.direction = "up"


def go_down():
    if head.lastdirection != "up":
        head.direction = "down"


def go_right():
    if head.lastdirection != "left":
        head.direction = "right"


def go_left():
    if head.lastdirection != "right":
        head.direction = "left"


def movement():
    if head.direction == "up":
        y = head.ycor()
        head.lastdirection = "up"
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.lastdirection = "down"
        head.sety(y - 20)
    if head.direction == "right":
        x = head.xcor()
        head.lastdirection = "right"
        head.setx(x + 20)
    if head.direction == "left":
        x = head.xcor()
        head.lastdirection = "left"
        head.setx(x - 20)


# DangerNoodle head
head = turtle.Turtle()
head.shape("square")
head.color("yellow")
head.speed(0)
head.penup()
head.direction = "stop"
head.lastdirection = "none"
head.goto(0, 0)

# Keybinds

mw.listen()
mw.onkeypress(go_up, "w")
mw.onkeypress(go_down, "s")
mw.onkeypress(go_right, "d")
mw.onkeypress(go_left, "a")

# Game Loop

while True:
    mw.update()
    movement()
    time.sleep(delay)


