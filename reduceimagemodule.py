#!/usr/bin/python3
"""
File: reduceimagenmodule.py
Author: John Major
Date: 2025-09-14
Description:  Class to reduce image files
"""


# Import the Images module from pillow
from PIL import Image


class ImgReduce():
    def __init__(self, inDir, outDir, qValue):
        self.inDir = inDir
        self.outDir = outDir
        self.qValue = qValue


    def process(self,file):
        image_path = self.inDir + "/" + file
        image_file = Image.open(image_path)
        image_file.save(self.outDir + "/" + file,
            quality=self.qValue)


