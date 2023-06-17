"""
    Riccardo Prosdocimi
    CS 5001, Fall 2021
    Final Project -- The Game: Puzzle Slider

    This is a Tiles class.
    This makes handling the behavior of the tiles on the screen possible.
"""

import turtle


class Tiles:
    def __init__(self, x_coord, y_coord, size, image):
        """
        This is the constructor of the Tiles class.

        :param x_coord: the x coordinate of the tile on the screen (int)
        :param y_coord: the y coordinate of the tile on the screen (int)
        :param size: the size of the tile (int)
        :param image: the system path to a .gif file -> tile's appearance (str)
        """

        self.t = turtle.Turtle()
        self.t.hideturtle()
        self.t.speed(0)
        self.t.penup()
        self.screen = turtle.Screen()
        self.x = x_coord
        self.y = y_coord
        self.size = size
        self.image = image

    def draw_tiles(self):
        """
        This method draws/shows the tile on the screen assigning an image to it
        and drawing/showing a black contour around it.
        """

        s = self.size + 2
        self.t.setpos(self.x - (s / 2), self.y - (s / 2))
        for _ in range(4):  # draws the contour
            self.t.pendown()
            self.t.pencolor("black")
            self.t.forward(s)
            self.t.left(90)
        self.t.penup()
        self.t.setpos(self.x, self.y)
        self.screen.register_shape(self.image)
        self.t.showturtle()
        self.t.shape(self.image)

    def clear_tiles(self):
        """
        This method erases the tile from the screen together with its contour.
        """

        self.t.clear()  # erases the contour
        self.t.shape("blank")  # assigns a blank image to each tile

    def get_x_coord(self):
        """
        This method returns the tile's x coordinate on the screen.

        :return: tile's x coordinate (int)
        """

        return self.x

    def get_y_coord(self):
        """
        This method returns the tile's y coordinate on the screen.

        :return: tile's y coordinate (int)
        """

        return self.y

    def set_image(self, image):
        """
        This method assigns a new image to the tile.
        """

        self.image = image

    def is_blank(self):
        """
        This method/predicate returns True if it finds the puzzle's blank tile.

        :return: bool
        """

        if "blank" in self.image:
            return True
        return False

    def is_clicked(self, x, y):
        """
        This method calculates the tile's area to make it clickable.

        :param x: the mouse click's x coordinate (int)
        :param y: the mouse click's y coordinate (int)
        :return: bool
        """

        return abs(x - self.x) <= self.size / 2 and abs(y - self.y) <= \
            self.size / 2

    def get_image(self):
        """
        This method returns the image assigned to a tile.

        :return: the system path to a .gif file -> tile's appearance (str)
        """

        return self.image

    def swap_tiles(self, image):
        """
        This method assigns a new image to a tile and draws/shows it on the
        screen.

        :param image: the system path to a .gif file -> tile's appearance (str)
        """

        self.set_image(image)
        self.t.shape(image)
