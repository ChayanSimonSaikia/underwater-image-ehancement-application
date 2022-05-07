from PySide2 import QtWidgets, QtGui, QtCore
from ImageInfo import ImageInfo
from Tools.ui_resize import Ui_Resize
import imutils
import cv2 as cv


class resizeTool(QtWidgets.QDialog, Ui_Resize):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.setWindowFlag(QtCore.Qt.WindowCloseButtonHint, False)
        # Image width and height set
        self.widthVal.setValue(ImageInfo.img_bgr.shape[1])
        self.heightVal.setValue(ImageInfo.img_bgr.shape[0])
        # click events
        self.cancelBtn.clicked.connect(self.closeClicked)
        self.okBtn.clicked.connect(self.okClicked)
        self.widthVal.valueChanged.connect(self.widthValChanged)
        self.heightVal.valueChanged.connect(self.heightValChanged)
        self.lockCheck_2.setChecked(True)
        # bACKUP iMAGE
        self.tempImage = ImageInfo.img_bgr

    def heightValChanged(self):
        # lock is true or false
        if self.lockCheck_2.checkState():
            # Checks given width is lower than the original image if true apply INTER_AREA else INTER_CUBIC
            if self.heightVal.value() < ImageInfo.img_bgr.shape[0]:
                self.img_resized = imutils.resize(
                    ImageInfo.img_bgr, height=self.heightVal.value(), inter=cv.INTER_AREA)
            else:
                self.img_resized = imutils.resize(
                    ImageInfo.img_bgr, height=self.heightVal.value(), inter=cv.INTER_CUBIC)
            # Show width new value
            self.widthVal.valueChanged.disconnect(self.widthValChanged)
            self.widthVal.setValue(self.img_resized.shape[1])
            self.widthVal.valueChanged.connect(self.widthValChanged)
            # converting to pixmap
            self.img_resized_pixmap = ImageInfo.convert_BGR2Pixmap(
                self, self.img_resized)
            self.parent().imageMainWindowLabel.setPixmap(
                QtGui.QPixmap(self.img_resized_pixmap))

        else:
            self.lockUnchecked()

    def widthValChanged(self):
        # lock is treu or false
        if self.lockCheck_2.checkState():
            if self.widthVal.value() < ImageInfo.img_bgr.shape[1]:
                self.img_resized = imutils.resize(
                    ImageInfo.img_bgr, width=self.widthVal.value(), inter=cv.INTER_AREA)
            else:
                self.img_resized = imutils.resize(
                    ImageInfo.img_bgr, width=self.widthVal.value(), inter=cv.INTER_CUBIC)
            # Show height new value
            self.heightVal.valueChanged.disconnect(self.heightValChanged)
            self.heightVal.setValue(self.img_resized.shape[0])
            self.heightVal.valueChanged.connect(self.heightValChanged)
            # converting to pixmap
            self.img_resized_pixmap = ImageInfo.convert_BGR2Pixmap(
                self, self.img_resized)
            self.parent().imageMainWindowLabel.setPixmap(
                QtGui.QPixmap(self.img_resized_pixmap))

        else:
            self.lockUnchecked()

    def okClicked(self):
        ImageInfo.img_bgr = self.img_resized
        ImageInfo.img_pixmap = self.img_resized_pixmap
        self.close()

    def closeClicked(self):
        # Converting to pixmap
        img_pixmap = ImageInfo.convert_BGR2Pixmap(self, self.tempImage)
        # Display in main window
        self.parent().imageMainWindowLabel.setPixmap(QtGui.QPixmap(img_pixmap))
        ImageInfo.img_pixmap = img_pixmap
        self.close()

    def lockUnchecked(self):
        # Checks given width or height is lower than the original image if true apply INTER_AREA else INTER_CUBIC
        if self.widthVal.value() < ImageInfo.img_bgr.shape[1] or self.heightVal.value() < ImageInfo.img_bgr.shape[0]:
            self.img_resized = cv.resize(
                ImageInfo.img_bgr, (self.widthVal.value(), self.heightVal.value()), interpolation=cv.INTER_AREA)
            self.img_resized_pixmap = ImageInfo.convert_BGR2Pixmap(
                self, self.img_resized)
            self.parent().imageMainWindowLabel.setPixmap(
                QtGui.QPixmap(self.img_resized_pixmap))
        else:
            # Greater than original image width or height Apply INTER_CUBIC
            self.img_resized = cv.resize(
                ImageInfo.img_bgr, (self.widthVal.value(), self.heightVal.value()), interpolation=cv.INTER_CUBIC)
            self.img_resized_pixmap = ImageInfo.convert_BGR2Pixmap(
                self, self.img_resized)
            self.parent().imageMainWindowLabel.setPixmap(
                QtGui.QPixmap(self.img_resized_pixmap))
