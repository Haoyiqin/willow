# -*- coding: utf-8 -*-
"""
Created on Mon May 14 00:17:57 2018

@author: Administrator
"""

from PIL import Image
from PIL import ImageEnhance
im = Image.open('birdnest.jpg)
om = ImageEnhance.Contrast(im)

