# -*- coding: utf-8 -*-
"""
Created on Sun May 13 23:50:18 2018

@author: Administrator
"""

from PIL import Image
import giob,os

size = 50,50

for infile in glob.glob("er.jpg"):
    file,ext = os.path.splitext(infile)
    im = Image.open(infile)
    im.thumbnail(size,Image.ANTIALTAS)
    im.save(file+".thumbnail","]PEG)
    im.show()
    print(im.size,im.mode)