import sys
import numpy as np
import random
import string
from PIL import Image
import os

if len(sys.argv) < 2:
    print("Usage: python3 script.py input_image.png")
    sys.exit()

# Get the input image file from command line argument
input_image_file = sys.argv[1]

# Open the input image
input_image = Image.open(input_image_file)

# Get the width and height of the input image
width, height = input_image.size

# Calculate the width and height of each smaller image
small_width = width // 2
small_height = height // 2

# Iterate through the rows and columns
for row in range(2):
    for col in range(2):
        # Calculate the coordinates of the current small image
        left = col * small_width
        top = row * small_height
        right = left + small_width
        bottom = top + small_height

        # Crop the small image from the input image
        small_image = input_image.crop((left, top, right, bottom))

        while True:
            # Generate a random string for the output file name
            random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
            output_file_name = random_string + ".png"
            # check if the file already exists
            if not os.path.isfile(output_file_name):
                break
        
        # Save the small image to a file
        small_image.save(output_file_name)
