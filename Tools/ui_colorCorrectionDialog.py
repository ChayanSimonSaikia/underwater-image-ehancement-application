# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'colorCorrectionDialogxSUMnb.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_colorCorrection_dialog(object):
    def setupUi(self, colorCorrection_dialog):
        if not colorCorrection_dialog.objectName():
            colorCorrection_dialog.setObjectName(u"colorCorrection_dialog")
        colorCorrection_dialog.resize(328, 158)
        font = QFont()
        font.setFamily(u"Roboto")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        colorCorrection_dialog.setFont(font)
        self.verticalLayout = QVBoxLayout(colorCorrection_dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(colorCorrection_dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gInout = QLineEdit(self.frame)
        self.gInout.setObjectName(u"gInout")
        self.gInout.setMaximumSize(QSize(30, 30))
        self.gInout.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.gInout, 1, 2, 1, 1)

        self.gLabel = QLabel(self.frame)
        self.gLabel.setObjectName(u"gLabel")

        self.gridLayout.addWidget(self.gLabel, 1, 0, 1, 1)

        self.gSlider = QSlider(self.frame)
        self.gSlider.setObjectName(u"gSlider")
        self.gSlider.setMinimum(-100)
        self.gSlider.setMaximum(100)
        self.gSlider.setSingleStep(1)
        self.gSlider.setPageStep(1)
        self.gSlider.setValue(0)
        self.gSlider.setSliderPosition(0)
        self.gSlider.setOrientation(Qt.Horizontal)
        self.gSlider.setTickPosition(QSlider.NoTicks)

        self.gridLayout.addWidget(self.gSlider, 1, 1, 1, 1)

        self.rSlider = QSlider(self.frame)
        self.rSlider.setObjectName(u"rSlider")
        self.rSlider.setMinimum(-100)
        self.rSlider.setMaximum(100)
        self.rSlider.setSingleStep(1)
        self.rSlider.setPageStep(1)
        self.rSlider.setValue(0)
        self.rSlider.setSliderPosition(0)
        self.rSlider.setOrientation(Qt.Horizontal)
        self.rSlider.setTickPosition(QSlider.NoTicks)

        self.gridLayout.addWidget(self.rSlider, 0, 1, 1, 1)

        self.rLabel = QLabel(self.frame)
        self.rLabel.setObjectName(u"rLabel")

        self.gridLayout.addWidget(self.rLabel, 0, 0, 1, 1)

        self.rInput = QLineEdit(self.frame)
        self.rInput.setObjectName(u"rInput")
        self.rInput.setMaximumSize(QSize(30, 30))
        self.rInput.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.rInput, 0, 2, 1, 1)

        self.bLabel = QLabel(self.frame)
        self.bLabel.setObjectName(u"bLabel")

        self.gridLayout.addWidget(self.bLabel, 2, 0, 1, 1)

        self.bSlider = QSlider(self.frame)
        self.bSlider.setObjectName(u"bSlider")
        self.bSlider.setMinimum(-100)
        self.bSlider.setMaximum(100)
        self.bSlider.setSingleStep(1)
        self.bSlider.setPageStep(1)
        self.bSlider.setValue(0)
        self.bSlider.setSliderPosition(0)
        self.bSlider.setOrientation(Qt.Horizontal)
        self.bSlider.setTickPosition(QSlider.NoTicks)

        self.gridLayout.addWidget(self.bSlider, 2, 1, 1, 1)

        self.bInput = QLineEdit(self.frame)
        self.bInput.setObjectName(u"bInput")
        self.bInput.setMaximumSize(QSize(30, 30))
        self.bInput.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.bInput, 2, 2, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout)


        self.verticalLayout.addWidget(self.frame)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.okBtn = QPushButton(colorCorrection_dialog)
        self.okBtn.setObjectName(u"okBtn")

        self.horizontalLayout.addWidget(self.okBtn)

        self.cancelBtn = QPushButton(colorCorrection_dialog)
        self.cancelBtn.setObjectName(u"cancelBtn")

        self.horizontalLayout.addWidget(self.cancelBtn)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(colorCorrection_dialog)

        QMetaObject.connectSlotsByName(colorCorrection_dialog)
    # setupUi

    def retranslateUi(self, colorCorrection_dialog):
        colorCorrection_dialog.setWindowTitle(QCoreApplication.translate("colorCorrection_dialog", u"Color Correction", None))
        self.gInout.setText(QCoreApplication.translate("colorCorrection_dialog", u"0", None))
        self.gLabel.setText(QCoreApplication.translate("colorCorrection_dialog", u"G", None))
        self.rLabel.setText(QCoreApplication.translate("colorCorrection_dialog", u"R", None))
        self.rInput.setText(QCoreApplication.translate("colorCorrection_dialog", u"0", None))
        self.bLabel.setText(QCoreApplication.translate("colorCorrection_dialog", u"B", None))
        self.bInput.setText(QCoreApplication.translate("colorCorrection_dialog", u"0", None))
        self.okBtn.setText(QCoreApplication.translate("colorCorrection_dialog", u"Ok", None))
        self.cancelBtn.setText(QCoreApplication.translate("colorCorrection_dialog", u"Cancel", None))
    # retranslateUi

