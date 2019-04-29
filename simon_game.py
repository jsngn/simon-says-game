# Author: Mien Nguyen
# Date: 04/28/2019
# Purpose: Create a version of Simon Says
# Disclaimer: I did not write the cs1lib.py module used in this program. All graphics done by Seth Serrano.
# Note: cs1lib.py is NEEDED for this game to run. Find it at: https://www.cs.dartmouth.edu/~cs1/install-win/cs1lib.py

from cs1lib import *
from random import randint
from button import Button


# Makes background black
def draw_bg():
    set_clear_color(0, 0, 0)
    clear()


# Handles mouse presses
def mouse_pressed(mx, my):
    global choice_blue, choice_red, choice_purple, choice_green

    # If mouse press is on blue button...
    if blue_button.button_x <= mx <= blue_button.button_x + BUTTON_WIDTH and blue_button.button_y <= my <= \
            blue_button.button_y + BUTTON_HEIGHT:
        choice_blue = True  # ... sets player's choice to blue
        if player_choosing:  # ... add player's choice to choices list if computer sequence has finished displaying
            player_num_list.append(BLUE_ID)

    # If mouse press is on red button...
    if red_button.button_x <= mx <= red_button.button_x + BUTTON_WIDTH and red_button.button_y <= my <= \
            red_button.button_y + BUTTON_HEIGHT:
        choice_red = True  # ... sets player's choice to red
        if player_choosing:  # ... add player's choice to choices list if computer sequence has finished displaying
            player_num_list.append(RED_ID)

    # If mouse press is on purple button...
    if purple_button.button_x <= mx <= purple_button.button_x + BUTTON_WIDTH and purple_button.button_y <= my <= \
            purple_button.button_y + BUTTON_HEIGHT:
        choice_purple = True  # ... sets player's choice to purple
        if player_choosing:  # ... add player's choice to choices list if computer sequence has finished displaying
            player_num_list.append(PURPLE_ID)

    # If mouse press is on green button...
    if green_button.button_x <= mx <= green_button.button_x + BUTTON_WIDTH and green_button.button_y <= my <= \
            green_button.button_y + BUTTON_HEIGHT:
        choice_green = True  # ... sets player's choice to green
        if player_choosing:  # ... add player's choice to choices list if computer sequence has finished displaying
            player_num_list.append(GREEN_ID)


# Handles mouse releases
def mouse_released(mx, my):
    global choice_blue, choice_red, choice_purple, choice_green, player_choosing

    # Stops player's choice from being set to blue if mouse is released on blue button
    if blue_button.button_x <= mx <= blue_button.button_x + BUTTON_WIDTH and blue_button.button_y <= my <= \
            blue_button.button_y + BUTTON_HEIGHT:
        choice_blue = False

    # Stops player's choice from being set to red if mouse is released on red button
    if red_button.button_x <= mx <= red_button.button_x + BUTTON_WIDTH and red_button.button_y <= my <= \
            red_button.button_y + BUTTON_HEIGHT:
        choice_red = False

    # Stops player's choice from being set to purple if mouse is released on purple button
    if purple_button.button_x <= mx <= purple_button.button_x + BUTTON_WIDTH and purple_button.button_y <= my <= \
            purple_button.button_y + BUTTON_HEIGHT:
        choice_purple = False

    # Stops player's choice from being set to green if mouse is released on green button
    if green_button.button_x <= mx <= green_button.button_x + BUTTON_WIDTH and green_button.button_y <= my <= \
            green_button.button_y + BUTTON_HEIGHT:
        choice_green = False


# Generates a random sequence of numbers to be displayed in the form of buttons lighting up
def generate_sequence():
    i = 0
    while i < seq_n:  # Generates an amount of numbers that corresponds to the number of rounds the player is on
        num = randint(1, 4)
        num_list.append(num)
        i += 1


# Lights up the button that corresponds to the ID number in the ith position of the random computer sequence
def light_buttons_seq(i):
    if num_list[i] == BLUE_ID:
        blue_button.pressed()
    elif num_list[i] == RED_ID:
        red_button.pressed()
    elif num_list[i] == PURPLE_ID:
        purple_button.pressed()
    elif num_list[i] == GREEN_ID:
        green_button.pressed()


# Darkens the button that corresponds to the ID number in the ith position of the random computer sequence
def darken_buttons_seq(i):
    if num_list[i] == BLUE_ID:
        blue_button.released()
    elif num_list[i] == RED_ID:
        red_button.released()
    elif num_list[i] == PURPLE_ID:
        purple_button.released()
    elif num_list[i] == GREEN_ID:
        green_button.released()


# Checks whether player's sequence matches computer sequence by comparing the 2 lists of player and computer sequences
def check_player_choice():
    if player_num_list == num_list:
        return True  # Returns True if sequences match
    return False  # Returns False if they don't match


# Resets the game when the next round starts or when game starts from the beginning again
def reset_game():
    global player_choosing, light_seq_secs, button_lighted_i, darken_seq_secs, inter_rounds_darken_secs

    # Deletes every item in the list with the computer sequence
    i = 0
    while i < len(num_list):
        del num_list[i]

    # Deletes every item in the list with the player's sequence
    j = 0
    while j < len(player_num_list):
        del player_num_list[j]

    player_choosing = False  # Prevents the player from choosing at the moment the round starts
    button_lighted_i = 0  # Allows the index used to light up every button corresponding to random sequence to be reset
    # to 0 so that every number in the new sequence will result in a button lighting up

    # Resets the counts that delay the events of buttons lighting up and darkening
    light_seq_secs = LIGHT_SEQ_INITIAL_TIME
    darken_seq_secs = DARK_SEQ_INITIAL_TIME
    inter_rounds_darken_secs = DARK_SEQ_INITIAL_TIME


# Displays graphical components, calls necessary functions for game, and handles lighting up and darkening buttons
def draw_simon():
    global light_seq_secs, player_choosing, seq_n, button_lighted_i, darken_seq_secs, inter_rounds_darken_secs, score

    draw_bg()  # Draws background every frame to give the animation effect

    # Draws the 4 buttons
    blue_button.draw()
    red_button.draw()
    purple_button.draw()
    green_button.draw()

    set_stroke_color(1, 1, 1)  # Sets text color to white
    set_font("Impact")
    draw_text("Score: " + str(score), 165, 27)  # Displays player's score at top center
    draw_text("Follow the sequence!", 115, 380)  # Displays an instruction at bottom center

    # Prevents a button that player pressed from previous round to be lit up throughout the time when buttons light up
    # for the computer sequence in the upcoming round
    if not choice_blue:
        blue_button.released()
    if not choice_red:
        red_button.released()
    if not choice_purple:
        purple_button.released()
    if not choice_green:
        green_button.released()

    if not player_choosing:  # Players can't choose buttons when computer sequence is generated and buttons are lighting
        # up for computer sequence

        # Generates a new random sequence only if length of random sequence is less than the length that the sequence
        # should be, according to the round number
        if len(num_list) < seq_n:
            generate_sequence()

        # Lights up each button for each number in the computer sequence one after another and allows a small delay
        # between player choosing buttons for previous sequence and buttons lighting up for new random sequence
        while button_lighted_i < len(num_list):
            inter_rounds_darken_secs += DARK_SEQ_TIME_INCR  # Increments the count which allows the delay between rounds

            if inter_rounds_darken_secs < DARK_SEQ_TIME:  # Breaks out of loop if the delay hasn't been long enough yet
                break
            else:  # Once the delay is long enough OR at least 1 button has been lit up for new random sequence...
                light_buttons_seq(button_lighted_i)  # ... lights a button for a number in the sequence
                light_seq_secs += LIGHT_SEQ_TIME_INCR  # ... increments count which allows delay before button darkens

                if light_seq_secs < LIGHT_SEQ_TIME:  # Breaks loop if the delay before darkening hasn't been long enough
                    break
                else:  # Once the delay is long enough...
                    darken_buttons_seq(button_lighted_i)  # ... darkens a button for a number in the sequence
                    darken_seq_secs += DARK_SEQ_TIME_INCR  # ... increments count which allows delay before next button
                    # lights up

                    if darken_seq_secs < DARK_SEQ_TIME:  # Breaks loop if delay before lighting hasn't been long enough
                        break
                    elif darken_seq_secs == DARK_SEQ_TIME:  # Once the delay is long enough...
                        button_lighted_i += 1  # ... increments the count to light up buttons so next button is lighted
                        light_seq_secs = LIGHT_SEQ_INITIAL_TIME  # Resets the count for delay before button darkens
                        darken_seq_secs = DARK_SEQ_INITIAL_TIME  # Resets the count for delay before next button lights

                # Allows player to choose buttons once all buttons have been lighted for the random sequence
                if button_lighted_i == len(num_list):
                    player_choosing = True
    else:  # If player can make choices...
        # ... lights up blue button if player pressed mouse on that button and darkens it when mouse released
        if choice_blue:
            blue_button.pressed()
        else:
            blue_button.released()

        # ... lights up red button if player pressed mouse on that button and darkens it when mouse released
        if choice_red:
            red_button.pressed()
        else:
            red_button.released()

        # ... lights up purple button if player pressed mouse on that button and darkens it when mouse released
        if choice_purple:
            purple_button.pressed()
        else:
            purple_button.released()

        # ... lights up green button if player pressed mouse on that button and darkens it when mouse released
        if choice_green:
            green_button.pressed()
        else:
            green_button.released()

    # If player has made a number of choices that corresponds to the number of items in the random sequence,
    # and neither list of player and computer sequence is empty, and the player's sequence matches random sequence...
    if len(player_num_list) == len(num_list) and len(player_num_list) != 0 and check_player_choice():
        seq_n += SEQ_INCR  # ... increases the number of items for next round's sequence
        score += SCORE_INCR  # ... increments player's score
        reset_game()  # ... resets the game
    # If player has made a number of choices that corresponds to the number of items in the random sequence,
    # and neither list of player and computer sequence is empty, but the player's sequence is incorrect...
    elif len(player_num_list) == len(num_list) and len(player_num_list) != 0 and not check_player_choice():
        seq_n = SEQ_INITIAL_N  # ... resets the number of items for next round's sequence to 0
        score = SCORE_INITIAL  # ... resets score to 0
        reset_game()  # ... resets the game


# Stores the identification numbers for buttons of each color
BLUE_ID = 1
RED_ID = 2
PURPLE_ID = 3
GREEN_ID = 4

BUTTON_HEIGHT = 150  # Stores button's height
BUTTON_WIDTH = 150  # Stores button's width

LIGHT_SEQ_TIME = 15  # Stores the value which the counter that allows delay of button in computer sequence darkening
# must meet for delay to be long enough
LIGHT_SEQ_INITIAL_TIME = 0  # Stores the initial value for the counter that allows delay of button in computer sequence
# darkening
LIGHT_SEQ_TIME_INCR = 1  # Stores the increment value for delay of button in computer sequence darkening
DARK_SEQ_TIME = 15  # Stores the value which the counter that allows delay of buttons lighting up between rounds AND
# before next button in computer sequence lights up must meet for delay to be long enough
DARK_SEQ_INITIAL_TIME = 0  # Stores the initial value for the counters that allow delay of buttons lighting between
# rounds AND before next button in computer sequence lights up
DARK_SEQ_TIME_INCR = 1  # Stores the increment value for delay of buttons lighting up between rounds AND before next
# button in computer sequence lights up

SEQ_INCR = 1  # Stores the increment value for number of items in computer sequence
SEQ_INITIAL_N = 1  # Stores the initial number of items in computer sequence

SCORE_INCR = 1  # Stores the increment value for score
SCORE_INITIAL = 0  # Stores the initial score

light_seq_secs = LIGHT_SEQ_INITIAL_TIME  # Serves as a counter that allows delay before button in computer sequence
# darkens
darken_seq_secs = DARK_SEQ_INITIAL_TIME  # Serves as a counter that allows delay before next button in computer sequence
# lights up
inter_rounds_darken_secs = DARK_SEQ_INITIAL_TIME  # Serves as a counter that allows delay between player choosing and
# buttons lighting up for next computer sequence
button_lighted_i = 0  # Keeps track of the index of buttons that are being lighted for the computer sequence

score = SCORE_INITIAL  # Keeps track of player's score
seq_n = SEQ_INITIAL_N  # Keeps track of number of items that should be in computer sequence depending on round number

player_choosing = False  # Updates to True when player can choose and False when computer sequence is still displaying

# Update to True when player clicks on buttons of corresponding colors and False when they release the mouse click
choice_blue = False
choice_red = False
choice_purple = False
choice_green = False

# Creates objects of Button class that correspond to buttons of each color
blue_button = Button(BLUE_ID)
red_button = Button(RED_ID)
purple_button = Button(PURPLE_ID)
green_button = Button(GREEN_ID)

num_list = []  # Creates an empty list for random computer sequence
player_num_list = []  # Creates an empty list for player's sequence

# Starts the game
start_graphics(draw_simon, mouse_press=mouse_pressed, mouse_release=mouse_released)
