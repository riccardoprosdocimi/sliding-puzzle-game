"""
    Riccardo Prosdocimi
    CS 5001, Fall 2021
    Final Project -- The Game: Puzzle Slider

    This is a Text class.
    This makes managing dynamic text graphics on the screen possible.
"""

import turtle


class Text:
    def __init__(self, x_coord, y_coord, message, color):
        """
        This is the constructor of the Text class.

        :param x_coord: the text's x coordinate on the screen (int)
        :param y_coord: the text's y coordinate on the screen (int)
        :param message: the text's appearance (str/int)
        :param color: the text's color (str)
        """

        self.t = turtle.Turtle()
        self.t.hideturtle()
        self.t.penup()
        self.t.speed(0)
        self.x = x_coord
        self.y = y_coord
        self.t.color(color)
        self.message = message

    def update(self, message):
        """
        This method assigns a new appearance to the text.

        :param message: the new text's appearance (str/int)
        """

        self.message = message
        self.t.clear()
        self.t.write(message, False, 'left', font=('Arial', 20, "bold"))

    def show_text(self):
        """
        This method draws/shows the text on the screen.
        """

        self.t.setpos(self.x, self.y)
        self.t.write(self.message, False, 'left', font=('Arial', 20, "bold"))

    def show_leaders(self, lst):
        """
        This method draws/shows a list of names on the screen.

        :param lst: a list of values (list)
        """

        for i in range(len(lst)):
            self.t.setpos(self.x, self.y)
            self.t.write(lst[i], False, 'left', font=('Arial', 15, "normal"))
            self.y -= 25
