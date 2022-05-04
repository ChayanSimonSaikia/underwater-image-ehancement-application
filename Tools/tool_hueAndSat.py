from PySide2 import QtWidgets, QtGui
from ImageInfo import ImageInfo
from Tools.ui_hueAndSatDialog import Ui_hueAndSat_dialog
import cv2 as cv
import numpy as np


class HueAndSatTool(QtWidgets.QDialog, Ui_hueAndSat_dialog):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        self.hueSlider.valueChanged.connect(self.changeHue)
        self.satSlider.valueChanged.connect(self.changeSat)
        self.cancelBtn.clicked.connect(self.closeWinow)
        self.okBtn.clicked.connect(self.okButton)

        self.tempImage = ImageInfo.img_bgr
    # Slider moves

    def changeHue(self):
        # Get sliders value
        hueVal = self.hueSlider.value()

        # Display in lineedit
        self.hueInput.setText(str(hueVal))

        # Operation
        hsv = cv.cvtColor(self.tempImage, cv.COLOR_BGR2HSV)
        h, s, v = cv.split(hsv)

        h = (h.astype("float32"))*((hueVal+100)/100)

        h = np.clip(h, 0, 255).astype("uint8")

        merged = cv.merge([h, s, v])

        self.img_bgr = cv.cvtColor(merged, cv.COLOR_HSV2BGR)

        # Converting to pixmap And assigning
        self.img_pixmap = ImageInfo.convert_BGR2Pixmap(self,
                                                       self.img_bgr)

        # Display in main window
        self.parent().imageMainWindowLabel.setPixmap(QtGui.QPixmap(self.img_pixmap))

    def changeSat(self):
        # Get sliders value
        satVal = self.satSlider.value()

        # Display in lineedit
        self.satInput.setText(str(satVal))

        # Operation
        hsv = cv.cvtColor(self.tempImage, cv.COLOR_BGR2HSV)
        h, s, v = cv.split(hsv)

        if satVal == 0:
            s = (s.astype("float32"))*1
        elif satVal > 0:
            s = (s.astype("float32"))*((satVal+100)/100)
        else:
            s = (s.astype("float32"))*((satVal+100)/100)

        s = np.clip(s, 0, 255).astype("uint8")

        merged = cv.merge([h, s, v])

        self.img_bgr = cv.cvtColor(merged, cv.COLOR_HSV2BGR)

        # Converting to pixmap And assigning
        self.img_pixmap = ImageInfo.convert_BGR2Pixmap(self,
                                                       self.img_bgr)

        # Display in main window
        self.parent().imageMainWindowLabel.setPixmap(QtGui.QPixmap(self.img_pixmap))

    def closeWinow(self):
        # Converting to pixmap
        img_pixmap = ImageInfo.convert_BGR2Pixmap(self, self.tempImage)
        # Display in main window
        self.parent().imageMainWindowLabel.setPixmap(QtGui.QPixmap(img_pixmap))
        ImageInfo.img_pixmap = img_pixmap
        self.close()

    def okButton(self):
        # Assigning adjusted image to image_editing variable
        ImageInfo.img_bgr = self.img_bgr
        ImageInfo.img_pixmap = self.img_pixmap
        self.close()
