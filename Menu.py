from Window import Window
from PySide2 import QtWidgets, QtGui
import cv2 as cv
from ImageInfo import ImageInfo
import imutils
""" FILE ACTION """


class File(Window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Image Saved Or Not
        self.saved = False
        # Open Image action
        self.actionOpen.triggered.connect(self.openAndDisplayImage)
        # Save As Image action
        self.actionSaveAs.triggered.connect(self.saveAs)
        # Save Image action
        self.actionSave.triggered.connect(self.save)
        # Clear all action
        self.actionClear_All_Changes_2.triggered.connect(self.clearAllChanges)
        # Exit action
        self.actionExit.triggered.connect(self.exit)

    # Open Image Method

    def openAndDisplayImage(self):
        # Opening Dialog Box for Browsing a image
        self.image, type = QtWidgets.QFileDialog().getOpenFileName(
            self, "Open Image", "F:\Laptop\KU Related\Testing\Methods - Copy\samples", "JPG Image Only (*.jpg)")
        # Enable all functions after opening the image
        if self.image != '':
            self.img_path = ImageInfo.img_path = self.image
            # Loading Image In OpenCV
            self.img_bgr = ImageInfo.img_bgr_original = ImageInfo.img_bgr = imutils.resize(cv.imread(
                ImageInfo.img_path), height=700, inter=cv.INTER_CUBIC)
            # Converting to pixmap And assigning
            self.img_pixmap = ImageInfo.convert_BGR2Pixmap(self,
                                                           self.img_bgr)

            # Displaying image
            self.imageMainWindowLabel.setPixmap(
                QtGui.QPixmap(self.img_pixmap))
            # TO activate all desabled buttons
            self.ActivateAllFunctions()
            # push to UndoStack

    # Save Action Method

    def save(self):
        if self.saved:
            cv.imwrite(self.save_img_path, self.img_bgr)
        else:
            self.saveAs()

    # Save As Action Method
    def saveAs(self):
        self.save_img_path, type = QtWidgets.QFileDialog.getSaveFileName(
            self, 'Save Image', 'C:\\', 'JPG Only (*.jpg)')

        if self.save_img_path == '':
            pass
        else:
            cv.imwrite(self.save_img_path, self.img_bgr)
            self.saved = True
    # Exit Action method

    def exit(self):
        # If no image found
        if ImageInfo.img_path == '':
            self.close()
        else:
            # If image found
            if self.saved:
                self.close()
            else:
                self.imageNotSavedMsg()
    # Show message if the image has not been saved

    def imageNotSavedMsg(self):
        msg = QtWidgets.QMessageBox()
        ans = msg.question(self, "Save Image",
                           "Image has not been saved.\nAre you sure that you want exit ? ", msg.Close | msg.Save | msg.Cancel)

        if ans == msg.Save:
            self.saveAs()
        elif ans == msg.Close:
            self.close()
        else:
            pass

    def clearAllChanges(self):
        new_img = ImageInfo.convert_BGR2Pixmap(
            self, ImageInfo.img_bgr_original)
        self.imageMainWindowLabel.setPixmap(QtGui.QPixmap(new_img))
        ImageInfo.img_bgr = ImageInfo.img_bgr_original
        ImageInfo.img_pixmap = new_img
    # TO activate all desabled buttons

    def ActivateAllFunctions(self):
        self.actionSave.setDisabled(False)
        self.actionExit.setDisabled(False)
        self.actionSaveAs.setDisabled(False)
        self.menuImage_2.setDisabled(False)
        self.menuTools.setDisabled(False)
        self.adjustmentBtn.setDisabled(False)
        self.HueSatBtn.setDisabled(False)
        self.cropBtn.setDisabled(False)
        self.TextBtn.setDisabled(False)
        self.resizeBtn.setDisabled(False)
        self.magicToolBtn.setDisabled(False)
        self.colorPickerBtn.setDisabled(False)
        self.colorCorrectionBtn.setDisabled(False)
        self.toolsPanel.setCursor(QtGui.QCursor(QtGui.Qt.ArrowCursor))
