import time
from machine import Pin, Timer
from neopixel import Neopixel

# Configure the Neopixel
pixels = Neopixel(1, 0, 23, "RGB")
pixels.brightness(50)

# Define the colors
colors = [(20, 20, 20), (100, 100, 100), (170, 170, 170), (255, 255, 255), (0, 50, 50), (0, 120, 120), (0, 255, 255)]

# Function to set the LED to the desired color
def set_color(color):
    pixels.set_pixel(0, color)
    pixels.show()

# Configure the button and its press handler
button = Pin(24, Pin.IN, Pin.PULL_UP)

# Index to track the current color
current_color_index = 0

# Function to toggle the color
def toggle_color(pin):
    global current_color_index
    current_color_index = (current_color_index + 1) % len(colors)
    set_color(colors[current_color_index])

# Attach the button press handler
button.irq(trigger=Pin.IRQ_FALLING, handler=toggle_color)

# Set the initial color
set_color(colors[current_color_index])

# Main loop (not needed for button handling)
while True:
    pass

