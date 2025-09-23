#!/usr/bin/python3
"""
File: reduceimagenmodule.py
Author: John Major
Date: 2025-09-14
Description:  Class to reduce image files
"""


# Import the Images module from pillow
from PIL import Image, ExifTags
import math


class ImgReduce():
    def __init__(self, inDir, outDir, qValue, rValue):
        self.inDir = inDir
        self.outDir = outDir
        self.qValue = qValue
        self.rValue = rValue


    def process(self, file, fileName, dateOf, extension ):
        print(fileName, dateOf)
        image_path = self.inDir + "/" + file

        image_file = Image.open(image_path)

        # get rotation
        rotate = self.getOrientation(image_file)

        # get size of file
        width, height = image_file.size

        # set new size
        new_size = ( math.ceil(width*self.rValue/100), 
                    math.ceil(height*self.rValue/100) )

        # resize image
        image_file = image_file.resize(new_size)

        # set rotation
        image_file = image_file.rotate(rotate,expand=True)

        # save fiel
        image_file.save(self.outDir + "/" + fileName + "_" + dateOf  + \
                "." + extension,
            quality=self.qValue)


    def getOrientation(self, img):
        degrees = 0;

        # Get EXIF data (if available)
        exif = img._getexif()
        
        if exif:
            # Map EXIF tags to names
            exif_dict = {
                ExifTags.TAGS.get(tag, tag): value
                for tag, value in exif.items()
            }
            
            orientation = exif_dict.get("Orientation", None)
    
            match orientation:
                case 1:
                    degrees = 0
                case 2:
                    degrees = 0
                case 3:
                    degrees = 180
                case 4:
                    degrees = 0
                case 5:
                    degrees = 0
                case 6:
                    degrees = 270
                case 7:
                    degrees = 0
                case 8:
                    degrees = 90
                case _:
                    degrees = 0

        return degrees
