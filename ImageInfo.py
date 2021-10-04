from PySide2 import QtGui


class ImageInfo:
    img_bgr_original = []
    img_path = ''
    img_bgr = []
    img_pixmap = None

    def convert_BGR2Pixmap(self, image):
        # Converting to pixmap
        height, width, channel = image.shape
        bytesPerLine = 3*width
        self.qImg = QtGui.QImage(
            image.data, width, height, bytesPerLine, QtGui.QImage.Format_RGB888).rgbSwapped()
        return self.qImg
