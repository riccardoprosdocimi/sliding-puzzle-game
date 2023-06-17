"""
    Riccardo Prosdocimi
    CS 5001, Fall 2021
    Final Project -- The Game: Puzzle Slider

    This is a Button class.
    This makes creating on-screen buttons possible.
"""

import turtle


class Button:
    def __init__(self, x_coord, y_coord, image, height, width=80):
        """
        This is the constructor of the Button class.

        :param x_coord: the button's x coordinate on the screen (int)
        :param y_coord: the button's y coordinate on the screen (int)
        :param image: the button's appearance (str that refers to a .gif file)
        :param height: the button's height (int)
        :param width: the button's width (int)
        """

        self.screen = turtle.Screen()
        self.t = turtle.Turtle()
        self.t.hideturtle()
        self.t.penup()
        self.x = x_coord
        self.y = y_coord
        self.image = image
        self.width = width
        self.height = height

    def show_button(self):
        """
        This method draws/shows the button on the screen.
        """

        self.t.setpos(self.x, self.y)
        self.screen.register_shape(self.image)
        self.t.showturtle()
        self.t.shape(self.image)

    def is_clicked(self, x, y):
        """
        This method calculates the button's area to make it clickable.

        :param x: the mouse click's x coordinate (int)
        :param y: the mouse click's y coordinate (int)
        :return: bool
        """

        return abs(x - self.x) <= self.width / 2 and abs(y - self.y) <= self.\
            height / 2
