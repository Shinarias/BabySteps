import turtle
import time
import random


# Global Variables

updateDelay = 0.1


# Set up the Screen

mainWindow = turtle.Screen()
mainWindow.title("DangerNoodle!")
mainWindow.bgcolor("black")
mainWindow.setup(width=600, height=600)
mainWindow.tracer(0)

# Segment list
segments = []


# Functions

def movement():
    if noodleHead.direction == "up":
        ypos = noodleHead.ycor()
        noodleHead.sety(ypos + 20)
    if noodleHead.direction == "down":
        ypos = noodleHead.ycor()
        noodleHead.sety(ypos - 20)
    if noodleHead.direction == "left":
        xpos = noodleHead.xcor()
        noodleHead.setx(xpos - 20)
    if noodleHead.direction == "right":
        xpos = noodleHead.xcor()
        noodleHead.setx(xpos + 20)


def go_up():
    if noodleHead.lastdirection != "down":
        noodleHead.direction = "up"
        noodleHead.lastdirection = "up"


def go_down():
    if noodleHead.lastdirection != "up":
        noodleHead.direction = "down"
        noodleHead.lastdirection = "down"

def go_left():
    if noodleHead.lastdirection != "right":
        noodleHead.direction = "left"
        noodleHead.lastdirection = "left"


def go_right():
    if noodleHead.lastdirection != "left":
        noodleHead.direction = "right"
        noodleHead.lastdirection = "right"


# Keyboard bindings

mainWindow.listen()
mainWindow.onkeypress(go_up, "Up")
mainWindow.onkeypress(go_down, "Down")
mainWindow.onkeypress(go_left, "Left")
mainWindow.onkeypress(go_right, "Right")

# DangerNoodle setup

noodleHead = turtle.Turtle()
noodleHead.speed(0)
noodleHead.shape("square")
noodleHead.color("yellow")
noodleHead.penup()
noodleHead.goto(0, 0)
noodleHead.direction = "stop"
noodleHead.lastdirection = "none"

# DangerNoodle's nommies

food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)



# Main game loop

while True:
    mainWindow.update()

    # Check for collision
    if noodleHead.distance(food) < 20:
        # Randomizing food Coordinates
        foodxpos = random.randint(-290, 290)
        foodypos = random.randint(-290, 290)
        food.goto(foodxpos, foodypos)
        # Creating a new segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("white")
        new_segment.penup()
        segments.append(new_segment)

    # Reverse movement of DangerNoodle segments
    for index in range(len(segments)-1, 0, -1):
        segPosX = segments[index-1].xcor()
        segPosY = segments[index-1].ycor()
        segments[index].goto(segPosX, segPosY)

    # Move first Segment to where DangerNoodles head is
    if len(segments) > 0:
        segPosY = noodleHead.ycor()
        segPosX = noodleHead.xcor()
        segments[0].goto(segPosX, segPosY)

    movement()

    time.sleep(updateDelay)


mainWindow.mainloop()
