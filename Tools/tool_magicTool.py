import cv2
import numpy as np

from ImageInfo import ImageInfo


class MagicTool:
    def runMagicTool(self):

        img = ImageInfo.img_bgr
        out = self.simplest_cb(img, 1)
        out = self.applyClahe(out)

        return cv2.fastNlMeansDenoisingColored(out, None, 10, 10, 3, 7)

    def applyClahe(self, img):
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        h, s, v = cv2.split(hsv)

        clahe = cv2.createCLAHE(clipLimit=2.5, tileGridSize=(1, 1))
        v = clahe.apply(v)

        merged = cv2.merge([h, s, v])
        return cv2.cvtColor(merged, cv2.COLOR_HSV2BGR)

    def simplest_cb(self, img, percent=1):
        out_channels = []
        cumstops = (
            img.shape[0] * img.shape[1] * percent / 200.0,
            img.shape[0] * img.shape[1] * (1 - percent / 200.0)
        )
        for channel in cv2.split(img):
            cumhist = np.cumsum(cv2.calcHist(
                [channel], [0], None, [256], (0, 256)))

            low_cut, high_cut = np.searchsorted(cumhist, cumstops)

            lut = np.concatenate((
                np.zeros(low_cut),
                np.around(np.linspace(0, 255, high_cut - low_cut + 1)),
                255 * np.ones(255 - high_cut)
            ))

            out_channels.append(cv2.LUT(channel, lut.astype('uint8')))
        return cv2.merge(out_channels)
