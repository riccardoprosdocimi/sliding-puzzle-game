"""
    Riccardo Prosdocimi
    CS 5001, Fall 2021
    Final Project -- The Game: Puzzle Slider

    This is a Screen class.
    This makes setting up the game graphics possible.
"""

import turtle
import time
from constants import *
from rectangle import Rectangle


class Screen:
    def __init__(self):
        """
        This is the constructor of the Screen class.
        """

        self.s = turtle.Screen()
        self.t = turtle.Turtle()
        self.t.hideturtle()
        self.t.speed(0)
        self.t.penup()
        self.game_area = Rectangle(GAME_AREA_X, GAME_AREA_Y, GAME_AREA_WIDTH,
                                   GAME_AREA_HEIGHT, 10, "black")
        self.leaderboard_area = Rectangle(LEADERBOARD_AREA_X,
                                          LEADERBOARD_AREA_Y,
                                          LEADERBOARD_AREA_WIDTH,
                                          LEADERBOARD_AREA_HEIGHT, 5, "blue")
        self.status_area = Rectangle(STATUS_AREA_X, STATUS_AREA_Y,
                                     STATUS_AREA_WIDTH,
                                     STATUS_AREA_HEIGHT, 10, "black")

    def set(self):
        """
        This method sets the window's size and title.
        """

        self.s.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.s.title("CS5001 Sliding Puzzle Game")

    def get_input(self, title, prompt):
        """
        This method shows a pop-up window where the user can insert text.

        :param title: the pop-up window's description (str)
        :param prompt: the pop-up window's prompt for the user (str)
        :return: user text (str)
        """

        user_input = self.s.textinput(title, prompt)
        return user_input

    def get_num_input(self, title, prompt, default, min_val, max_val):
        """
        This method shows a pop-up window where the user can insert a number.

        :param title: the pop-up window's description (str)
        :param prompt: the pop-up window's prompt for the user (str)
        :param default: the default value shown in the text field (int)
        :param min_val: the minimum value allowed (int)
        :param max_val: the maximum value allowed (int)
        :return: user number (int)
        """

        user_input = self.s.numinput(title, prompt, default, min_val, max_val)
        return user_input

    def set_pop_up(self, image):
        """
        This method shows a pop-up image/message to the user.

        :param image: the system path to a .gif file -> message (str)
        """

        t = turtle.Turtle()
        self.s.register_shape(image)
        t.showturtle()
        t.shape(image)
        time.sleep(3)
        t.hideturtle()

    def set_text(self, message, color, fontype, x_coord, y_coord):
        """
        This method draws/shows text on the screen.

        :param message: the text shown/drawn on the screen (str)
        :param color: the message's color (str)
        :param fontype: the message's font type (str)
        :param x_coord: the message's x coordinate on the screen (int)
        :param y_coord: the message's y coordinate on the screen (int)
        """

        self.t.setpos(x_coord, y_coord)
        self.t.color(color)
        self.t.write(message, False, 'left', font=('Arial', 20, fontype))

    def set_thumbnail(self, image, x_coord, y_coord):
        """
        This method draws/shows an image on the screen.

        :param image: the system path to a .gif file -> image (str)
        :param x_coord: the image's x coordinate on the screen (int)
        :param y_coord: the image's y coordinate on the screen (int)
        """

        self.s.register_shape(image)
        self.t.setpos(x_coord, y_coord)
        self.t.showturtle()
        self.t.shape(image)

    def get_screen(self):
        """
        This method returns turtle.Screen().

        :return: turtle.Screen()
        """

        return self.s
