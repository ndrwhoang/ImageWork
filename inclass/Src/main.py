'''
Created on Feb 25, 2020

@author: hoangqg
'''
from image_fnc import *

# open an image file. The default path is where this python module is
im = Image.open("SiriusAndViolet.jpg")
print(im.width, im.height, im.mode, im.format)  # Display some info about the image
