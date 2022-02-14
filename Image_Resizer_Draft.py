#!/usr/bin/env python3

from pathlib import Path
from PIL import Image
import os

"""
    Walks through the Dir looking for 
    files with .dng ext.
"""
DirPath = '/Users/taylorpatterson/desktop/ImagesToResize'
ext = '.DNG'  # extension to search for
FileList = []
x = 0  # Variable for iterating through FileList

# Creating new directory to save the resized images.
NewDir = Path('/Users/taylorpatterson/desktop/ResizedImages')
NewDir.mkdir(exist_ok=True)  # Bypasses the dir exists error

for path, dir, files in os.walk(DirPath):
    for name in files:
        if name.endswith(ext):
            try:
                FileList.append(name)
                img = Image.open(FileList[x], DirPath)  # Open the image by taking the filename from FileList
                new_image = img.resize((round(img.size[0] * .5), round(img.size[1] * 0.5)))
                # resize the image to half its size
                # Saved in a new dir
                new_image.save(NewDir, "resized_picture.jpg")
                x += 1  # Step 1 to move to next img.
                new_image.show()
            except IOError:
                pass


def resizer(n):
    img = Image.open(FileList[x])
