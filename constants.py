"""
    Riccardo Prosdocimi
    CS 5001, Fall 2021
    Final Project -- The Game: Puzzle Slider

    This file contains the constant values.
"""


SCREEN_WIDTH = 720
SCREEN_HEIGHT = 670

GAME_AREA_X = -320
GAME_AREA_Y = 280
GAME_AREA_WIDTH = 420
GAME_AREA_HEIGHT = 420

LEADERBOARD_AREA_X = 120
LEADERBOARD_AREA_Y = 280
LEADERBOARD_AREA_WIDTH = 190
LEADERBOARD_AREA_HEIGHT = 420

LEADERS_TEXT_X = LEADERBOARD_AREA_X + 10
LEADERS_TEXT_Y = LEADERBOARD_AREA_Y - 30

LEADERS_X = LEADERBOARD_AREA_X + 10
LEADERS_Y = LEADERBOARD_AREA_Y - 90

THUMBNAIL_X = LEADERBOARD_AREA_X + LEADERBOARD_AREA_WIDTH - 20
THUMBNAIL_Y = LEADERBOARD_AREA_Y - 10

STATUS_AREA_X = -320
STATUS_AREA_Y = -180
STATUS_AREA_WIDTH = 630
STATUS_AREA_HEIGHT = 100

QUIT_BUTTON_X = STATUS_AREA_X + (STATUS_AREA_WIDTH - 60)
QUIT_BUTTON_Y = STATUS_AREA_Y - 50
QUIT_BUTTON_WIDTH = 80
QUIT_BUTTON_HEIGHT = 53

LOAD_BUTTON_X = STATUS_AREA_X + (STATUS_AREA_WIDTH - 150)
LOAD_BUTTON_Y = STATUS_AREA_Y - 50
LOAD_BUTTON_WIDTH = 80
LOAD_BUTTON_HEIGHT = 76

RESET_BUTTON_X = STATUS_AREA_X + (STATUS_AREA_WIDTH - 240)
RESET_BUTTON_Y = STATUS_AREA_Y - 50
RESET_BUTTON_WIDTH = RESET_BUTTON_HEIGHT = 80

PLAYER_MOVES_TEXT_X = STATUS_AREA_X + 20
PLAYER_MOVES_TEXT_Y = STATUS_AREA_Y - ((STATUS_AREA_HEIGHT / 2) + 10)

CLICKS_COUNTER_X = PLAYER_MOVES_TEXT_X + 140
CLICKS_COUNTER_Y = PLAYER_MOVES_TEXT_Y

CLICKS_SLASH_X = PLAYER_MOVES_TEXT_X + 175
CLICKS_SLASH_Y = PLAYER_MOVES_TEXT_Y

USER_CLICKS_X = PLAYER_MOVES_TEXT_X + 185
USER_CLICKS_Y = PLAYER_MOVES_TEXT_Y

MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct",
          "Nov", "Dec"]

DAYS = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
