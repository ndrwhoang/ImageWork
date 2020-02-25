'''
Created on Feb 25, 2020

@author: hoangqg
'''

from PIL import Image, ImageFilter, ImageDraw, ImageFont
import os, sys
import requests
from io import BytesIO

def load_image( filename ) :
    try:
        myimage = Image.open(filename)
        myimage.load()
        return myimage
    except:
        print("Image load failed")
        return None

def save_image( imageObject, outfilename ) :
    """
    Save an image to disk
    :param imageObject: The Image to save
    :param outfilename: The target file
    """
    try:
        imageObject.save( outfilename )
    except:
        print(".save() failed")
        
def crop_img(img, crop_size=(200,300,400,500)):   # an image object and a tuple  
    im = img.crop(crop_size) # (left, top, right, bottom) it's a tuple!
    return im