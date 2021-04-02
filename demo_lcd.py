#! /usr/bin/env python

# Simple string program. Writes and updates strings.
# Demo program for the I2C 16x2 Display from Ryanteck.uk
# Created by Matthew Timmons-Brown for The Raspberry Pi Guy YouTube channel

# Import necessary libraries for communication and display use
import drivers
from time import sleep, time
import pyrebase


from datetime import datetime

now = datetime.now()
current_time = now.strftime("%H:%M")
print("Current Time =", current_time)

config = {
  "apiKey": "AIzaSyDFvJAre2oelCzHLjqFjviAf0hesiu-FcE",
  "authDomain": "garageeye-e2848.firebaseapp.com",
  "databaseURL": "https://garageeye-e2848-default-rtdb.firebaseio.com",
  "storageBucket": "garageeye-e2848.appspot.com"
}

# initialisatiing pyrebase
firebase = pyrebase.initialize_app(config)

# initialisatiing Database
db = firebase.database()

# Load the driver and set it to "display"
# If you use something from the driver library use the "display." prefix first
display = drivers.Lcd()

# Main body of code
try:
    while True:
        # Remember that your sentences can only be 16 characters long!
        print("Writing to display")
        GarageState = db.child("GarageState").get().val()
        time = now.strftime("%H:%M")
        display.lcd_display_string("Garage: " + GarageState, 1)  # Write line of text to first line of display
        display.lcd_display_string(current_time, 2)  # Write line of text to second line of display
        sleep(5)                                           # Give time for the message to be read
        #display.lcd_display_string("I am a display!", 1)   # Refresh the first line of display with a different message
        #sleep(2)                                           # Give time for the message to be read
        display.lcd_clear()                                # Clear the display of any data
        sleep(2)                                           # Give time for the message to be read
except KeyboardInterrupt:
    # If there is a KeyboardInterrupt (when you press ctrl+c), exit the program and cleanup
    print("Cleaning up!")
    display.lcd_clear()
