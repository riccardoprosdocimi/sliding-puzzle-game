"""
    Riccardo Prosdocimi
    CS 5001, Fall 2021
    Final Project -- The Game: Puzzle Slider

    This is a Rectangle class.
    This makes drawing rectangles of various sizes and colors possible.
"""

import turtle


class Rectangle:
    def __init__(self, x_coord, y_coord, width, height, size, color):
        """
        This is the constructor of the Rectangle class.

        :param x_coord: the rectangle's x coordinate on the screen (int)
        :param y_coord: the rectangle's y coordinate on the screen (int)
        :param width: the rectangle's width (int)
        :param height: the rectangle's height (int)
        :param size: the rectangle's border's size (int)
        :param color: the rectangle's border's color (str)
        """

        self.t = turtle.Turtle()
        self.t.hideturtle()
        self.t.penup()
        self.t.speed(0)
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.width = width
        self.height = height
        self.size = size
        self.color = color

    def draw(self):
        """
        This method draws/shows the rectangle on the screen.
        """

        self.t.setpos(self.x_coord, self.y_coord)
        self.t.pendown()
        self.t.pencolor(self.color)
        self.t.pensize(self.size)
        self.t.forward(self.width)
        self.t.right(90)  # side 1
        self.t.forward(self.height)
        self.t.right(90)  # side 2
        self.t.forward(self.width)
        self.t.right(90)  # side 3
        self.t.forward(self.height)
        self.t.right(90)  # side 4
