# Author: Mien Nguyen
# Date: 04/28/2019
# Purpose: Create a Button class for a version of Simon Says

from cs1lib import *

# Store x & y coordinates and identification number for blue button
BLUE_X = 40
BLUE_Y = 40
BLUE_ID = 1

# Store x & y coordinates and identification number for red button
RED_X = 40
RED_Y = 200
RED_ID = 2

# Store x & y coordinates and identification number for purple button
PURPLE_X = 200
PURPLE_Y = 40
PURPLE_ID = 3

# Store x & y coordinates and identification number for green button
GREEN_X = 200
GREEN_Y = 200
GREEN_ID = 4


# Button class definition
class Button:
    def __init__(self, identifier):

        self.identifier = identifier

        # Assigns the appropriate x & y coordinates and .png files of un-pressed buttons to the right color buttons,
        # as indicated by ID number
        if self.identifier == BLUE_ID:
            self.button_x = BLUE_X
            self.button_y = BLUE_Y
            self.button_img = load_image("Outline Blue.png")
        elif self.identifier == RED_ID:
            self.button_x = RED_X
            self.button_y = RED_Y
            self.button_img = load_image("Outline Red.png")
        elif self.identifier == PURPLE_ID:
            self.button_x = PURPLE_X
            self.button_y = PURPLE_Y
            self.button_img = load_image("Outline Purple.png")
        elif self.identifier == GREEN_ID:
            self.button_x = GREEN_X
            self.button_y = GREEN_Y
            self.button_img = load_image("Outline Green.png")

    # Assigns .png files of pressed buttons to the right color buttons
    def pressed(self):
        if self.identifier == BLUE_ID:
            self.button_img = load_image("Blue.png")
        elif self.identifier == RED_ID:
            self.button_img = load_image("Red.png")
        elif self.identifier == PURPLE_ID:
            self.button_img = load_image("Purple.png")
        elif self.identifier == GREEN_ID:
            self.button_img = load_image("Green.png")

    # Assigns .png files of un-pressed buttons to the right color buttons
    def released(self):
        if self.identifier == BLUE_ID:
            self.button_img = load_image("Outline Blue.png")
        elif self.identifier == RED_ID:
            self.button_img = load_image("Outline Red.png")
        elif self.identifier == PURPLE_ID:
            self.button_img = load_image("Outline Purple.png")
        elif self.identifier == GREEN_ID:
            self.button_img = load_image("Outline Green.png")

    # Draws the right buttons at the right x & y coordinates
    def draw(self):
        draw_image(self.button_img, self.button_x, self.button_y)
