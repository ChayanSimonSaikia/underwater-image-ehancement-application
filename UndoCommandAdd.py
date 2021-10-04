from PySide2 import QtWidgets, QtGui
from ImageInfo import ImageInfo


class UndoCommandAdd(QtWidgets.QUndoCommand):
    def __init__(self, image, imageLabel, img_bgr):
        super().__init__()
        self.image = image
        self.imageLabel = imageLabel
        self.img_bgr = img_bgr

    def undo(self):
        if isinstance(self.image, str):
            self.imageLabel.setPixmap(QtGui.QPixmap(self.image))
            ImageInfo.img_path = ''
        else:
            if self.image == None:
                self.imageLabel.setPixmap(QtGui.QPixmap(ImageInfo.img_path))
            else:
                self.imageLabel.setPixmap(QtGui.QPixmap(self.image))
                ImageInfo.img_bgr = self.img_bgr
                ImageInfo.img_pixmap = self.image
