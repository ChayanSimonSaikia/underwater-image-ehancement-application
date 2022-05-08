from PySide2 import QtWidgets, QtGui, QtCore
from ImageInfo import ImageInfo
from UndoStack import UndoStack
from Tools.ui_adjustmentDialog import Ui_adjustment_dialog
import cv2 as cv


class AdjustmentTool(QtWidgets.QDialog, Ui_adjustment_dialog):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.setWindowFlag(QtCore.Qt.WindowCloseButtonHint, False)

        self.brightnessSlider.valueChanged.connect(self.changeVal)
        self.contrastSlider.valueChanged.connect(self.changeVal)
        self.cancelBtn.clicked.connect(self.closeWinow)
        self.okBtn.clicked.connect(self.okButton)

        self.tempImage = ImageInfo.img_bgr
    # Slider moves

    def changeVal(self):
        # Get sliders value
        brightnessVal = self.brightnessSlider.value()
        contrastVal = self.contrastSlider.value()

        # Display in lineedit
        self.brightnessInput.setText(str(brightnessVal))
        self.contrastInout.setText(str(contrastVal))

        self.img_bgr = cv.addWeighted(self.tempImage, (contrastVal+100)/100,
                                      self.tempImage, 0, brightnessVal)

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
        # Push to Undo stack
        UndoStack().push(self.img_bgr)
        # Assigning adjusted image to image_editing variable
        ImageInfo.img_bgr = self.img_bgr
        ImageInfo.img_pixmap = self.img_pixmap
        self.close()
