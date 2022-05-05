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

        self.b, self.g, self.r = cv.split(ImageInfo.img_bgr)
        self.bNew, self.gNew, self.rNew = [[], [], []]
    # Slider moves

    def changeR(self):
        # Get sliders value
        rVal = self.rSlider.value()

        # Display in lineedit
        self.rInput.setText(str(rVal))

        # Operation
        r = (self.r.astype("float32"))*((rVal+100)/100)
        r = np.clip(r, 0, 255).astype("uint8")

        self.rNew = r

        if len(self.bNew) == 0 and len(self.gNew) == 0:
            self.img_bgr = cv.merge([self.b, self.g, r])
        elif len(self.bNew) == 0:
            self.img_bgr = cv.merge([self.b, self.gNew, r])
        elif len(self.gNew) == 0:
            self.img_bgr = cv.merge([self.bNew, self.g, r])
        else:
            self.img_bgr = cv.merge([self.bNew, self.gNew, r])

        self.displayImage()

    def changeB(self):
        # Get sliders value
        bVal = self.bSlider.value()

        # Display in lineedit
        self.bInput.setText(str(bVal))

        # Operation
        b = (self.b.astype("float32"))*((bVal+100)/100)
        b = np.clip(b, 0, 255).astype("uint8")

        self.bNew = b

        if len(self.rNew) == 0 and len(self.gNew) == 0:
            self.img_bgr = cv.merge([b, self.g, self.r])
        elif len(self.rNew) == 0:
            self.img_bgr = cv.merge([b, self.gNew, self.r])
        elif len(self.gNew) == 0:
            self.img_bgr = cv.merge([b, self.g, self.rNew])
        else:
            self.img_bgr = cv.merge([b, self.gNew, self.rNew])

        self.displayImage()

    def changeG(self):
        # Get sliders value
        gVal = self.gSlider.value()

        # Display in lineedit
        self.gInout.setText(str(gVal))

        # Operation
        g = (self.g.astype("float32"))*((gVal+100)/100)
        g = np.clip(g, 0, 255).astype("uint8")

        self.gNew = g

        if len(self.bNew) == 0 and len(self.rNew) == 0:
            self.img_bgr = cv.merge([self.b, g, self.r])
        elif len(self.bNew) == 0:
            self.img_bgr = cv.merge([self.b, g, self.rNew])
        elif len(self.rNew) == 0:
            self.img_bgr = cv.merge([self.bNew, g, self.r])
        else:
            self.img_bgr = cv.merge([self.bNew, g, self.rNew])

        self.displayImage()

    def displayImage(self):
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
