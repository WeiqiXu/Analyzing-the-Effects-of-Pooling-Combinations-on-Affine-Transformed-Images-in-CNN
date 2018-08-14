# Linear Transformation of an Image with PIL.Image
# Meringue
# 5/3/2017

import numpy as np
from PIL import Image
import cv2

## Translation
def cv2_Translate(img_dir,pixel_R,pixel_B):
    PIL_img_array = np.array(Image.open(img_dir))
    rows, cols = PIL_img_array.shape[:2]
    M = np.float32([[1,0,pixel_R],[0,1,pixel_B]])
    res = cv2.warpAffine(PIL_img_array,M,(rows,cols))
    return Image.fromarray(res)

## Rotation
def PIL_Rotate(img_dir, angle):
    PIL_img = Image.open(img_dir)
    return PIL_img.rotate(angle)

## Horizontal reflection
def PIL_Flip_LR(img_dir):
    PIL_img = Image.open(img_dir)
    return PIL_img.transpose(Image.FLIP_LEFT_RIGHT)

## Vertical reflection
def PIL_Flip_TB(img_dir):
    PIL_img = Image.open(img_dir)
    return PIL_img.transpose(Image.FLIP_TOP_BOTTOM)

## Brightness
def PIL_Enhance(img_dir,k):
    PIL_img = Image.open(img_dir)
    return PIL_img.point(lambda i:i*k)

## Affine
def cv2_Affine(img_dir,delta_pix,pts1 = np.float32([[0,0],[32,0],[0,32]])):
    PIL_img_array = np.array(Image.open(img_dir))
    rows, cols = PIL_img_array.shape[:2]
    pts2 = pts1+delta_pix
    M = cv2.getAffineTransform(pts1,pts2)
    res = cv2.warpAffine(PIL_img_array,M,(rows,cols))
    return Image.fromarray(res)

