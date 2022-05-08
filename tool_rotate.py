import cv2
import numpy as np

from ImageInfo import ImageInfo


class Rotate:
    def rotate(self):
        return cv2.rotate(ImageInfo.img_bgr, rotateCode=cv2.ROTATE_90_CLOCKWISE)
