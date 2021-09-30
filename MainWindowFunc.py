from PySide2 import QtWidgets, QtGui
import cv2 as cv
from MainWindowUi import Ui_MainWindow


class MainWindowFunc(QtWidgets.QMainWindow, Ui_MainWindow):
    saved, image_path = False, ''

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        # Open Image action
        self.actionOpen.triggered.connect(self.openAndDisplayImage)
        # Save As Image action
        self.actionSaveAs.triggered.connect(self.saveAs)
        # Save Image action
        self.actionSave.triggered.connect(self.save)
        # Exit action
        self.actionExit.triggered.connect(self.exit)

    """ FILE ACTION """
    # Open Image Method

    def openAndDisplayImage(self):
        # Opening Dialog Box for Browsing a image
        self.image_path, type = QtWidgets.QFileDialog().getOpenFileName(
            self, "Open Image", "F:\Laptop\KU Related\Major Project\Image_editor\Photos", "JPG Image Only (*.jpg)")

        # Enable all functions after opening the image
        if self.image_path == '':
            pass
        else:
            # Displaying image
            self.imageMainWindowLabel.setPixmap(QtGui.QPixmap(self.image_path))

            # Loading Image In OpenCV
            self.img_original = cv.imread(self.image_path)
            self.img_editing = self.img_original

            self.actionSave.setDisabled(False)
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

    # Save Action Method

    def save(self):
        if self.saved:
            cv.imwrite(self.save_img_path, self.img_editing)
        else:
            self.saveAs()

    # Save As Action Method
    def saveAs(self):
        self.save_img_path, type = QtWidgets.QFileDialog.getSaveFileName(
            self, 'Save Image', 'C:\\', 'JPG Only (*.jpg)')

        if self.save_img_path == '':
            pass
        else:
            cv.imwrite(self.save_img_path, self.img_editing)
            self.saved = True
    # Exit Action method

    def exit(self):
        # If no image found
        if self.image_path == '':
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


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MainWindowFunc()
    widget.show()

    app.exec_()
