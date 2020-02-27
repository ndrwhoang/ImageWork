'''
Created on Feb 25, 2020

@author: hoangqg
'''

from PIL import Image, ImageFilter, ImageDraw, ImageFont
import os, sys
import requests
from io import BytesIO
from random import randint

def load_image(filename) :
    try:
        myimage = Image.open(filename)
        myimage.load()
        return myimage
    except:
        print("Image load failed")
        return None

def save_image(imageObject, outfilename) :
    """
    Save an image to disk
    :param imageObject: The Image to save
    :param outfilename: The target file
    """
    try:
        imageObject.save(outfilename)
    except:
        print(".save() failed")
        
def crop_img(img, crop_size=(200,300,400,500)):   # an image object and a tuple  
    im = img.crop(crop_size) # (left, top, right, bottom) it's a tuple!
    return im

def write_text_to_image(imageFile, text):
    """
    Write text onto an existing image. The result is written to sample-out.jpg
    :param imageFile: The image file name
    :param text: The text to write onto the image
    """
    #**************************************************
    #* Add text to an image
    #* https://pillow.readthedocs.io/en/stable/reference/ImageDraw.html
    #* https://stackoverflow.com/questions/16373425/add-text-on-image-using-pil
    #* Free fonts: https://www.fontsquirrel.com/fonts/list/classification/sans%20serif
    #**************************************************
    myImage = load_image(imageFile);
    draw = ImageDraw.Draw(myImage)
    # https://stackoverflow.com/questions/47694421/pil-issue-oserror-cannot-open-resource
    fontStyle = ImageFont.truetype("Aaargh.ttf", 48)     # font must be in the same folder as the .py file. 
    for i in range(0, 10):
        draw.ellipse([(300, 300), (i+randint(0,800),i+randint(0,800))], outline="green", fill="white")
    x = randint(0, myImage.width-len(text)*30)
    y = randint(0, myImage.height-len(text)*10)
    x_1 = x+randint(30, 50)
    y_1 = y+randint(30,50)
    for letter in text:
        x_1 += 35 + randint(-100, 100)
        draw.text((x_1, y_1), letter, (0,255,0), font=fontStyle)
        
        
    draw.text((x, y), text, (0,255,0), font=fontStyle)    # Write in black 
    
    myImage.save("sample-out.jpg")