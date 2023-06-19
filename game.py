"""
    Riccardo Prosdocimi
    CS 5001, Fall 2021
    Final Project -- The Game: Puzzle Slider

    This is a Game class.
    This resembles the Puzzle Slider Game.
"""

from constants import *
import turtle
import os
import random
from screen import Screen
from button import Button
from text import Text
from puzzle import Puzzle
from tiles import Tiles
from error import Error


class Game:
    def __init__(self):
        """
        This is the constructor of the Game class.
        """

        self.screen = Screen()
        self.screen.set()
        self.screen.set_pop_up("Resources/splash_screen.gif")
        self.user = ""
        self.clicks = 0
        self.moves = 0
        self.get_user()
        self.get_moves()
        self.screen.game_area.draw()
        self.screen.leaderboard_area.draw()
        self.screen.status_area.draw()
        self.leaderboard = []
        self.read_leaderboard()
        self.screen.get_screen().onclick(self.get_click)
        self.leaders = Text(LEADERS_X, LEADERS_Y, self.leaderboard,
                            "blue")
        self.clicks_count = Text(CLICKS_COUNTER_X, CLICKS_COUNTER_Y,
                                 self.clicks, "black")
        self.reset_button = Button(RESET_BUTTON_X, RESET_BUTTON_Y,
                                   "Resources/resetbutton.gif", 80)
        self.load_button = Button(LOAD_BUTTON_X, LOAD_BUTTON_Y,
                                  "Resources/loadbutton.gif", 76)
        self.quit_button = Button(QUIT_BUTTON_X, QUIT_BUTTON_Y,
                                  "Resources/quitbutton.gif", 53)
        self.show_graphics()
        self.puzzle = Puzzle()
        self.master_dict = {}
        self.loaded_puzzle = {}
        self.tiles = []
        self.winning_list = []
        self.load_default_puzzle()
        turtle.done()

    def get_user(self):
        """
        This method gets user input for their name.

        :return: user name capitalized (str)
        """

        while self.user == '':  # keeps asking until name is entered
            self.user = self.screen.get_input("Enter Name",
                                              "Your Name (11 characters max):")
            if self.user is None:  # user clicks cancel
                os._exit(0)  # shuts down the program
            else:
                self.user = self.user.capitalize()

    def get_moves(self):
        """
        This method gets user input for the number of moves or chances.

        :return: number of moves/chances (int)
        """

        self.moves = self.screen.get_num_input("Enter Moves",
                                               "Number of moves (chances) you "
                                               "want (5-200):", 50, 5, 200)
        if self.moves is None:  # user clicks cancel
            os._exit(0)
        else:
            return self.moves

    def print_moves(self):
        """
        This method casts the number of moves to an int and returns it.

        :return: number of moves/chances (int)
        """

        return int(self.moves)

    def show_graphics(self):
        """
        This method shows/draws the game graphics and controls.
        """

        self.screen.set_text("Leaders:", "blue", "normal", LEADERS_TEXT_X,
                             LEADERS_TEXT_Y)
        self.leaders.show_leaders(self.leaderboard)
        self.screen.set_text("Player Moves:", "black", "bold",
                             PLAYER_MOVES_TEXT_X, PLAYER_MOVES_TEXT_Y)
        self.clicks_count.show_text()
        self.screen.set_text("/", "black", "bold", CLICKS_SLASH_X,
                             CLICKS_SLASH_Y)
        self.screen.set_text(self.print_moves(), "black", "bold",
                             USER_CLICKS_X, USER_CLICKS_Y)
        self.reset_button.show_button()
        self.load_button.show_button()
        self.quit_button.show_button()

    def load_default_puzzle(self):
        """
        This method shows/draws the mario puzzle, which is the default puzzle.
        """

        self.master_dict = self.puzzle.get_puz()
        default_puzzle = "mario"
        if default_puzzle in self.master_dict:
            self.loaded_puzzle = self.master_dict[default_puzzle]
            self.screen.set_thumbnail(self.loaded_puzzle["thumbnail"],
                                      THUMBNAIL_X, THUMBNAIL_Y)
            self.set_tiles()
            self.set_scrambled_tiles()
        else:
            self.screen.set_pop_up("Resources/file_error.gif")
            error = Error("mario.puz", "Game.load_default_puzzle()")
            error.write_puz_error()
            self.puzzle.warn_user()
            self.validate_puzzle()

    def load_puzzle(self):
        """
        This method lets the user choose a puzzle from a list.

        :return: the selected puzzle (str)
        """

        puzzles = list(self.master_dict.keys())
        if "malformed_mario" in puzzles:  # known faulty puzzle among options?
            puzzles.remove("malformed_mario")  # get rid of it
        puzzles = "\n".join(puzzles)
        selected_puzzle = self.screen.get_input("Load Puzzle",
                                                f"Enter the name of the "
                                                f"puzzle you wish to load. "
                                                f"Choices are:\n{puzzles}")
        return selected_puzzle

    def validate_puzzle(self):
        """
        This method homogenizes user input for loading a new puzzle and checks
        if the selected puzzle is both loadable and among the available
        options.
        """

        selected_puzzle = self.load_puzzle()
        if selected_puzzle is not None:  # user doesn't click cancel
            selected_puzzle = selected_puzzle.lower()
            # puzzle name among available options?
            if selected_puzzle in self.master_dict.keys():
                self.loaded_puzzle = self.master_dict[selected_puzzle]
                tiles_number = self.loaded_puzzle["number"]
                # is the puzzle loadable?
                if tiles_number not in ["4", "9", "16"]:
                    self.screen.set_pop_up("Resources/file_error.gif")
                else:  # if it's loadable
                    for i in range(len(self.tiles)):
                        for j in range(len(self.tiles)):
                            self.tiles[i][j].clear_tiles()  # clears game area
                    self.tiles = []  # resets nested list containing the tiles
                    self.winning_list = []  # resets winning configuration
                    self.clicks = 0  # resets user clicks count
                    self.clicks_count.update(self.clicks)  # updates graphics
                    # shows/draws the correct thumbnail
                    self.screen.set_thumbnail(self.loaded_puzzle["thumbnail"],
                                              THUMBNAIL_X, THUMBNAIL_Y)
                    self.set_tiles()
                    self.set_scrambled_tiles()
            else:  # puzzle not in available options
                self.screen.set_pop_up("Resources/file_error.gif")

    def set_tiles(self):
        """
        This method calculates the tiles position on the screen and creates an
        object of each tile, saving the tiles to one nested list and their
        images to another nested list.
        """

        tiles_size = int(self.loaded_puzzle["size"])
        tiles_number = int(int(self.loaded_puzzle["number"]) ** 0.5)
        if tiles_number == 2:
            r = 200 - (tiles_size * tiles_number)  # puzzle's total space left
        elif tiles_number == 3:
            r = 300 - (tiles_size * tiles_number)
        else:  # tiles_number == 4
            r = 400 - (tiles_size * tiles_number)
        space = r / (tiles_number + 1)  # available space in between borders
        counter = 1
        for i in range(tiles_number):
            row = []  # initializes inner lists
            winning_row = []  # initializes winning configuration's inner lists
            for j in range(tiles_number):
                x_coord = (GAME_AREA_X + 10 + (tiles_size / 2) + (
                            tiles_size + space) * j)
                y_coord = (GAME_AREA_Y - 10 - (tiles_size / 2) - (
                            tiles_size + space) * i)
                image = self.loaded_puzzle[str(counter)]
                counter += 1
                # creates an object of each tile on the screen
                tiles = Tiles(x_coord, y_coord, tiles_size, image)
                row.append(tiles)  # adds tiles to the inner lists
                winning_row.append(image)  # populates winning configuration
            # data structure that reflects the puzzle grid on the screen
            self.tiles.append(row)  # adds lists to the outer list
            # completes winning configuration
            self.winning_list.append(winning_row)

    def set_scrambled_tiles(self):
        """
        This method shuffles the tiles on the screen letting the user solve the
        puzzle.
        """

        tiles_number = int(int(self.loaded_puzzle["number"]) ** 0.5)
        # creates a random list of numbers from 1 to the number of puzzle tiles
        num_list = random.sample(
            range(1, int(self.loaded_puzzle["number"]) + 1),
            int(self.loaded_puzzle["number"]))
        counter = 0
        for i in range(tiles_number):
            for j in range(tiles_number):
                # scrambles the puzzle's tiles
                image = self.loaded_puzzle[str(num_list[counter])]
                self.tiles[i][j].set_image(image)  # sets tile object's image
                self.tiles[i][j].draw_tiles()  # draws/shows the tiles
                counter += 1

    def reset_tiles(self):
        """
        This method draws/shows the puzzle's winning configuration.
        """

        tiles_number = int(int(self.loaded_puzzle["number"]) ** 0.5)
        counter = 1
        for i in range(tiles_number):
            for j in range(tiles_number):
                image = self.loaded_puzzle[str(counter)]
                self.tiles[i][j].set_image(image)
                self.tiles[i][j].t.shape(image)
                counter += 1

    def find_blank(self):
        """
        This method searches for the blank tile in the puzzle.
        """

        for row in self.tiles:
            for tiles in row:
                tiles.is_blank()

    def is_adjacent(self, row, column):
        """
        This method checks if a tile is adjacent to the blank tile and swaps
        the two tiles if it is while checking if the player has won after each
        swap. It also updates user clicks.

        :param row: index traversing the outer list (int)
        :param column: index traversing the inner lists (int)
        """

        # sifts through the tiles nested list checking if a tile on the screen
        # is next to the blank tile either horizontally or vertically
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        for i in range(len(directions)):
            new_row = directions[i][0] + row
            new_column = directions[i][1] + column
            # blank tile next to the clicked tile?
            if 0 <= new_row < len(self.tiles) and 0 <= new_column < len(
                    self.tiles) and self.tiles[new_row][new_column].is_blank():
                # swap tiles -> clicked tile shifts to blank tile's place
                # and vice versa
                blank_image = self.tiles[new_row][new_column].get_image()
                image = self.tiles[row][column].get_image()
                self.tiles[new_row][new_column].swap_tiles(image)
                self.tiles[row][column].swap_tiles(blank_image)
                # each time a tile shifts -> +1 click
                self.count_clicks()
                self.clicks_count.update(self.clicks)
                self.check_end_game()  # nested list == winning configuration

    def quit_game(self):
        """
        This method shows a pop-up message and shuts the game down.
        """

        self.screen.set_pop_up("Resources/quitmsg.gif")
        os._exit(0)

    def get_click(self, x, y):
        """
        This method gets user clicks and calls other methods based on the
        click's location on the screen.

        :param x: x coordinate of the click on the screen (int)
        :param y: y coordinate of the click on the screen (int)
        """

        for i in range(len(self.tiles)):
            for j in range(len(self.tiles[0])):
                if self.tiles[i][j].is_clicked(x, y):
                    # clicked tile next to the blank tile?
                    self.is_adjacent(i, j)
        if self.reset_button.is_clicked(x, y):  # click on reset button
            self.reset_tiles()
        if self.load_button.is_clicked(x, y):  # click on load button
            self.puzzle.warn_user()
            self.validate_puzzle()
        if self.quit_button.is_clicked(x, y):  # click on quit button
            self.quit_game()

    def count_clicks(self):
        """
        This method updates the number of clicks every time a tile is shifted.
        """

        self.clicks = self.clicks + 1

    def check_end_game(self):
        """
        This method checks if the player has won (unscrambles the puzzle) by
        comparing the nested list containing the winning configuration with the
        nested list shown/drawn on the screen. It also keeps track of the total
        clicks to check if the user has gone above the chances they chose,
        hence losing the game.
        """

        is_win = True  # flag variable
        for i in range(len(self.winning_list)):
            for j in range(len(self.winning_list)):
                # nested list != winning configuration?
                if self.winning_list[i][j] != self.tiles[i][j].get_image():
                    is_win = False  # continue playing
                    break
        if is_win:  # player wins
            self.screen.set_pop_up("Resources/winner.gif")
            self.screen.set_pop_up("Resources/credits.gif")
            self.write_leaderboard()  # saves score and player's name
            os._exit(0)
        # player hasn't won but has reached the number of clicks chosen
        elif is_win is False and self.clicks == self.moves + 1:
            self.screen.set_pop_up("Resources/Lose.gif")
            self.screen.set_pop_up("Resources/credits.gif")
            os._exit(0)

    def write_leaderboard(self):
        """
        This method saves a player's name and number of clicks to a file.
        """

        file = "leaderboard.txt"
        try:
            # name's length longer than 11 characters -> keep first 11
            player = lambda user: str(user) if len(user) <= 11 else \
                str(user[:11] + "...")
            with open(file, "a") as leaders_file:
                leaders_file.write(str(self.clicks) + ": " +
                                   str(player(self.user)) + "\n")
        except FileNotFoundError:
            self.screen.set_pop_up("Resources/leaderboard_error.gif")
            error = Error(file, "Game.write_leaderboard()")
            error.write_file_error()  # logs error if file not found
        except OSError:
            print("Some unknown error occurred")

    def read_leaderboard(self):
        """
        This method reads players' names and number of moves from a file and
        populates a list with them.
        """

        file = "leaderboard.txt"
        try:
            with open(file, "r") as leaders_file:
                for line in leaders_file:
                    leaders = line.strip("\n")
                    self.leaderboard.append(leaders)
            # sort the list in ascending order based off of the number of moves
            self.leaderboard.sort(key=lambda entry: int(entry.split(": ")[0]))
            # keeps the top 14 players
            self.leaderboard = self.leaderboard[:14]
        except FileNotFoundError:
            self.screen.set_pop_up("Resources/leaderboard_error.gif")
            error = Error(file, "Game.read_leaderboard()")
            error.write_file_error()
        except OSError:
            print("Some unknown error occurred")
