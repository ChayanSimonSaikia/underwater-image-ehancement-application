from PySide2 import QtWidgets, QtGui, QtCore
from matplotlib.pyplot import stem
from ImageInfo import ImageInfo
from Tools.ui_hueAndSatDialog import Ui_hueAndSat_dialog
import cv2 as cv
import numpy as np


class HueAndSatTool(QtWidgets.QDialog, Ui_hueAndSat_dialog):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.setWindowFlag(QtCore.Qt.WindowCloseButtonHint, False)

        self.hueSlider.valueChanged.connect(self.changeHue)
        self.satSlider.valueChanged.connect(self.changeSat)
        self.cancelBtn.clicked.connect(self.closeWinow)
        self.okBtn.clicked.connect(self.okButton)

        self.hsv = cv.cvtColor(ImageInfo.img_bgr, cv.COLOR_BGR2HSV)
        self.h, self.s, self.v = cv.split(self.hsv)
        self.sNew = []
        self.hNew = []
    # Slider moves

    def changeHue(self):
        # Get sliders value
        hueVal = self.hueSlider.value()
        # Display in lineedit
        self.hueInput.setText(str(hueVal))

        # Operation
        hTemp = (self.h.astype("float32"))*((hueVal+100)/100)

        hTemp = np.clip(hTemp, 0, 255).astype("uint8")

        self.hNew = hTemp

        if len(self.sNew) == 0:
            merged = cv.merge([hTemp, self.s, self.v])
        else:
            merged = cv.merge([hTemp, self.sNew, self.v])

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

        if satVal == 0:
            sTemp = (self.s.astype("float32"))*1
        elif satVal > 0:
            sTemp = (self.s.astype("float32"))*((satVal+100)/100)
        else:
            sTemp = (self.s.astype("float32"))*((satVal+100)/100)

        sTemp = np.clip(sTemp, 0, 255).astype("uint8")

        self.sNew = sTemp

        if len(self.hNew) == 0:
            merged = cv.merge([self.h, sTemp, self.v])
        else:
            merged = cv.merge([self.hNew, sTemp, self.v])

        self.img_bgr = cv.cvtColor(merged, cv.COLOR_HSV2BGR)

        # Converting to pixmap And assigning
        self.img_pixmap = ImageInfo.convert_BGR2Pixmap(self,
                                                       self.img_bgr)

        # Display in main window
        self.parent().imageMainWindowLabel.setPixmap(QtGui.QPixmap(self.img_pixmap))

    def closeWinow(self):
        # Converting to pixmap
        img_pixmap = ImageInfo.convert_BGR2Pixmap(self, ImageInfo.img_bgr)
        # Display in main window
        self.parent().imageMainWindowLabel.setPixmap(QtGui.QPixmap(img_pixmap))
        ImageInfo.img_pixmap = img_pixmap
        self.close()

    def okButton(self):
        # Assigning adjusted image to image_editing variable
        ImageInfo.img_bgr = self.img_bgr
        ImageInfo.img_pixmap = self.img_pixmap
        self.close()
