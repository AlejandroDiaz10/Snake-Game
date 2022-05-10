"""
Game: Paint (May 10th, 2022)
Student 1: Alejandro Díaz Villagómez | A01276769
Student 2: Emiliano Saucedo Arriola | A01659258

Exercises

1. Moving food. [DONE BY ALEJANDRO]
2. Random colors. [DONE BY EMILIANO]
"""

from random import randrange
from turtle import *

from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)


def change(x, y):
    """Change snake direction."""
    aim.x = x
    aim.y = y


def inside(head):
    """Return True if head inside boundaries."""
    return -200 < head.x < 190 and -200 < head.y < 190


cont = 0


def move():
    """Creating a cont"""
    global cont
    cont += 1

    """Move snake forward one segment."""
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, 'black')

    """Moving food randomly while checking is not traspassing the boundaries"""
    if (cont % 8 == 0):
        options = randrange(1, 5)
        if options == 1 and food.y < 150:  # Goes up
            food.y += 10
        else:
            food.y -= 10

        if options == 2 and food.x < 150:  # Goes right
            food.x += 10
        else:
            food.x -= 10

        if options == 3 and food.y > -150:  # Goes down
            food.y -= 10
        else:
            food.y += 10

        if options == 4 and food.x > -150:  # Goes left
            food.x -= 10
        else:
            food.x += 10

    square(food.x, food.y, 9, 'green')
    update()
    ontimer(move, 100)


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()
