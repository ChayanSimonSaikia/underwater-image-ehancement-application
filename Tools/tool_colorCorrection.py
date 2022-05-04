from PySide2 import QtWidgets, QtGui
from ImageInfo import ImageInfo
from Tools.ui_colorCorrectionDialog import Ui_colorCorrection_dialog
import cv2 as cv
import numpy as np


class ColorCorrection(QtWidgets.QDialog, Ui_colorCorrection_dialog):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        self.rSlider.valueChanged.connect(self.changeR)
        self.gSlider.valueChanged.connect(self.changeG)
        self.bSlider.valueChanged.connect(self.changeB)
        self.cancelBtn.clicked.connect(self.closeWinow)
        self.okBtn.clicked.connect(self.okButton)

        self.tempImage = ImageInfo.img_bgr
    # Slider moves

    def changeR(self):
        # Get sliders value
        rVal = self.rSlider.value()

        # Display in lineedit
        self.rInput.setText(str(rVal))

        # Operation
        b, g, r = cv.split(self.tempImage)

        r = (r.astype("float32"))*((rVal+100)/100)
        r = np.clip(r, 0, 255).astype("uint8")

        self.img_bgr = cv.merge([b, g, r])

        # Converting to pixmap And assigning
        self.img_pixmap = ImageInfo.convert_BGR2Pixmap(self,
                                                       self.img_bgr)

        # Display in main window
        self.parent().imageMainWindowLabel.setPixmap(QtGui.QPixmap(self.img_pixmap))

    def changeB(self):
        # Get sliders value
        bVal = self.bSlider.value()

        # Display in lineedit
        self.bInput.setText(str(bVal))

        # Operation
        b, g, r = cv.split(self.tempImage)

        b = (b.astype("float32"))*((bVal+100)/100)
        b = np.clip(b, 0, 255).astype("uint8")

        self.img_bgr = cv.merge([b, g, r])

        # Converting to pixmap And assigning
        self.img_pixmap = ImageInfo.convert_BGR2Pixmap(self,
                                                       self.img_bgr)

        # Display in main window
        self.parent().imageMainWindowLabel.setPixmap(QtGui.QPixmap(self.img_pixmap))

    def changeG(self):
        # Get sliders value
        gVal = self.gSlider.value()

        # Display in lineedit
        self.gInout.setText(str(gVal))

        # Operation
        b, g, r = cv.split(self.tempImage)

        g = (g.astype("float32"))*((gVal+100)/100)
        g = np.clip(g, 0, 255).astype("uint8")

        self.img_bgr = cv.merge([b, g, r])

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
