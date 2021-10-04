import cv2 as cv
from Window import Window
from PySide2 import QtCore, QtWidgets, QtGui
from Tools.ui_adjustment import Ui_adjustment_dialog
from ImageInfo import ImageInfo


class ToolBar(Window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Adjustment Button clicked event
        self.adjustmentBtn.clicked.connect(self.adjustmentClicked)

    # Display adjustment Window
    def adjustmentClicked(self):
        adjustment_dialog = AdjustmentTool(self)
        adjustment_dialog.show()


class AdjustmentTool(QtWidgets.QDialog, Ui_adjustment_dialog):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        self.brightnessSlider.valueChanged.connect(self.changeVal)
        self.contrastSlider.valueChanged.connect(self.changeVal)
        self.cancelBtn.clicked.connect(self.closeWinow)
        self.okBtn.clicked.connect(self.okButton)

    # Slider moves
    def changeVal(self):
        # Get sliders value
        brightnessVal = self.brightnessSlider.value()
        contrastVal = self.contrastSlider.value()

        # Display in lineedit
        self.brightnessInput.setText(str(brightnessVal))
        self.contrastInout.setText(str(contrastVal))

        tempImage = ImageInfo.img_editing
        self.adjusted_img = cv.addWeighted(tempImage, (contrastVal+100)/100,
                                           tempImage, 0, brightnessVal)

        # Converting to pixmap
        height, width, channel = self.adjusted_img.shape
        bytesPerLine = 3*width
        self.qImage = QtGui.QImage(self.adjusted_img.data, width, height,
                                   bytesPerLine, QtGui.QImage.Format_RGB888).rgbSwapped()
        # Display in main window
        self.parent().imageMainWindowLabel.setPixmap(QtGui.QPixmap(self.qImage))

    def closeWinow(self):
        # Converting to pixmap
        height, width, channel = ImageInfo.img_editing.shape
        bytesPerLine = 3*width
        self.qImage2 = QtGui.QImage(ImageInfo.img_editing.data, width, height,
                                    bytesPerLine, QtGui.QImage.Format_RGB888).rgbSwapped()

        # Display in main window
        self.parent().imageMainWindowLabel.setPixmap(QtGui.QPixmap(self.qImage2))
        self.close()

    def okButton(self):
        # Assigning adjusted image to image_editing variable
        ImageInfo.img_editing = self.adjusted_img
        self.close()
