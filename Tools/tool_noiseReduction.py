from PySide2 import QtWidgets, QtGui, QtCore
import cv2
from ImageInfo import ImageInfo
import cv2 as cv
from Tools.helpers.UndoStack import UndoStack
from Tools.ui_noiseReductionDialog import Ui_noiseReduction_dialog


class NoiseReductionTool(QtWidgets.QDialog, Ui_noiseReduction_dialog):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.setWindowFlag(QtCore.Qt.WindowCloseButtonHint, False)

        # click events
        self.cancelBtn.clicked.connect(self.closeClicked)
        self.okBtn.clicked.connect(self.okClicked)
        self.IntensityInput.valueChanged.connect(self.applyNoiseReduction)

        self.tempImage = ImageInfo.img_bgr

    def applyNoiseReduction(self):
        value = self.IntensityInput.value()
        self.newImg = cv2.fastNlMeansDenoisingColored(
            self.tempImage, None, value, value, (2*value+1), (2*value+3))
        # converting to pixmap

        self.img_pixmap = ImageInfo.convert_BGR2Pixmap(
            self, self.newImg)

        self.parent().imageMainWindowLabel.setPixmap(
            QtGui.QPixmap(self.img_pixmap))

    def okClicked(self):
        # Push to Undo stack
        UndoStack().push(self.img_bgr)

        ImageInfo.img_bgr = self.self.newImg
        ImageInfo.img_pixmap = self.img_pixmap
        self.close()

    def closeClicked(self):
        # Converting to pixmap
        img_pixmap = ImageInfo.convert_BGR2Pixmap(self, self.tempImage)
        # Display in main window
        self.parent().imageMainWindowLabel.setPixmap(QtGui.QPixmap(img_pixmap))
        ImageInfo.img_pixmap = img_pixmap
        self.close()
