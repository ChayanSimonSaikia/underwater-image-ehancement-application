# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'hueAndSatDialogSudDAi.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_hueAndSat_dialog(object):
    def setupUi(self, hueAndSat_dialog):
        if not hueAndSat_dialog.objectName():
            hueAndSat_dialog.setObjectName(u"hueAndSat_dialog")
        hueAndSat_dialog.resize(384, 300)
        self.frame = QFrame(hueAndSat_dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(9, 9, 361, 251))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.hueLabel = QLabel(self.frame)
        self.hueLabel.setObjectName(u"hueLabel")

        self.gridLayout.addWidget(self.hueLabel, 0, 0, 1, 1)

        self.satLabel = QLabel(self.frame)
        self.satLabel.setObjectName(u"satLabel")

        self.gridLayout.addWidget(self.satLabel, 1, 0, 1, 1)

        self.satSlider = QSlider(self.frame)
        self.satSlider.setObjectName(u"satSlider")
        self.satSlider.setMinimum(-100)
        self.satSlider.setMaximum(100)
        self.satSlider.setSingleStep(0)
        self.satSlider.setPageStep(1)
        self.satSlider.setValue(0)
        self.satSlider.setSliderPosition(0)
        self.satSlider.setOrientation(Qt.Horizontal)
        self.satSlider.setTickPosition(QSlider.NoTicks)
        self.satSlider.setTickInterval(0)

        self.gridLayout.addWidget(self.satSlider, 1, 1, 1, 1)

        self.hueSlider = QSlider(self.frame)
        self.hueSlider.setObjectName(u"hueSlider")
        self.hueSlider.setMinimum(0)
        self.hueSlider.setMaximum(500)
        self.hueSlider.setSingleStep(0)
        self.hueSlider.setPageStep(1)
        self.hueSlider.setValue(0)
        self.hueSlider.setSliderPosition(0)
        self.hueSlider.setOrientation(Qt.Horizontal)
        self.hueSlider.setTickPosition(QSlider.NoTicks)

        self.gridLayout.addWidget(self.hueSlider, 0, 1, 1, 1)

        self.hueInput = QLineEdit(self.frame)
        self.hueInput.setObjectName(u"hueInput")
        self.hueInput.setMaximumSize(QSize(30, 30))
        self.hueInput.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.hueInput, 0, 2, 1, 1)

        self.satInput = QLineEdit(self.frame)
        self.satInput.setObjectName(u"satInput")
        self.satInput.setMaximumSize(QSize(30, 30))
        self.satInput.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.satInput, 1, 2, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout)

        self.layoutWidget = QWidget(hueAndSat_dialog)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(200, 270, 158, 25))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.okBtn = QPushButton(self.layoutWidget)
        self.okBtn.setObjectName(u"okBtn")

        self.horizontalLayout.addWidget(self.okBtn)

        self.cancelBtn = QPushButton(self.layoutWidget)
        self.cancelBtn.setObjectName(u"cancelBtn")

        self.horizontalLayout.addWidget(self.cancelBtn)


        self.retranslateUi(hueAndSat_dialog)

        QMetaObject.connectSlotsByName(hueAndSat_dialog)
    # setupUi

    def retranslateUi(self, hueAndSat_dialog):
        hueAndSat_dialog.setWindowTitle(QCoreApplication.translate("hueAndSat_dialog", u"Hue And Saturation", None))
        self.hueLabel.setText(QCoreApplication.translate("hueAndSat_dialog", u"Hue", None))
        self.satLabel.setText(QCoreApplication.translate("hueAndSat_dialog", u"Sat", None))
        self.hueInput.setText(QCoreApplication.translate("hueAndSat_dialog", u"0", None))
        self.satInput.setText(QCoreApplication.translate("hueAndSat_dialog", u"0", None))
        self.okBtn.setText(QCoreApplication.translate("hueAndSat_dialog", u"Ok", None))
        self.cancelBtn.setText(QCoreApplication.translate("hueAndSat_dialog", u"Cancel", None))
    # retranslateUi

