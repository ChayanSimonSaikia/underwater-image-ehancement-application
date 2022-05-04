# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'adjustmentDialogcXpYNL.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_adjustment_dialog(object):
    def setupUi(self, adjustment_dialog):
        if not adjustment_dialog.objectName():
            adjustment_dialog.setObjectName(u"adjustment_dialog")
        adjustment_dialog.resize(384, 300)
        self.frame = QFrame(adjustment_dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(9, 9, 361, 251))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.brightnessLabel = QLabel(self.frame)
        self.brightnessLabel.setObjectName(u"brightnessLabel")

        self.gridLayout.addWidget(self.brightnessLabel, 0, 0, 1, 1)

        self.contrastLabel = QLabel(self.frame)
        self.contrastLabel.setObjectName(u"contrastLabel")

        self.gridLayout.addWidget(self.contrastLabel, 1, 0, 1, 1)

        self.contrastSlider = QSlider(self.frame)
        self.contrastSlider.setObjectName(u"contrastSlider")
        self.contrastSlider.setMinimum(-99)
        self.contrastSlider.setMaximum(99)
        self.contrastSlider.setSingleStep(1)
        self.contrastSlider.setPageStep(1)
        self.contrastSlider.setValue(0)
        self.contrastSlider.setSliderPosition(0)
        self.contrastSlider.setOrientation(Qt.Horizontal)
        self.contrastSlider.setTickPosition(QSlider.NoTicks)

        self.gridLayout.addWidget(self.contrastSlider, 1, 1, 1, 1)

        self.brightnessSlider = QSlider(self.frame)
        self.brightnessSlider.setObjectName(u"brightnessSlider")
        self.brightnessSlider.setMinimum(-99)
        self.brightnessSlider.setMaximum(99)
        self.brightnessSlider.setSingleStep(1)
        self.brightnessSlider.setPageStep(1)
        self.brightnessSlider.setValue(0)
        self.brightnessSlider.setSliderPosition(0)
        self.brightnessSlider.setOrientation(Qt.Horizontal)
        self.brightnessSlider.setTickPosition(QSlider.NoTicks)

        self.gridLayout.addWidget(self.brightnessSlider, 0, 1, 1, 1)

        self.brightnessInput = QLineEdit(self.frame)
        self.brightnessInput.setObjectName(u"brightnessInput")
        self.brightnessInput.setMaximumSize(QSize(30, 30))
        self.brightnessInput.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.brightnessInput, 0, 2, 1, 1)

        self.contrastInout = QLineEdit(self.frame)
        self.contrastInout.setObjectName(u"contrastInout")
        self.contrastInout.setMaximumSize(QSize(30, 30))
        self.contrastInout.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.contrastInout, 1, 2, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout)

        self.layoutWidget = QWidget(adjustment_dialog)
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


        self.retranslateUi(adjustment_dialog)

        QMetaObject.connectSlotsByName(adjustment_dialog)
    # setupUi

    def retranslateUi(self, adjustment_dialog):
        adjustment_dialog.setWindowTitle(QCoreApplication.translate("adjustment_dialog", u"Adjustment", None))
        self.brightnessLabel.setText(QCoreApplication.translate("adjustment_dialog", u"Brightness", None))
        self.contrastLabel.setText(QCoreApplication.translate("adjustment_dialog", u"Contrast", None))
        self.brightnessInput.setText(QCoreApplication.translate("adjustment_dialog", u"0", None))
        self.contrastInout.setText(QCoreApplication.translate("adjustment_dialog", u"0", None))
        self.okBtn.setText(QCoreApplication.translate("adjustment_dialog", u"Ok", None))
        self.cancelBtn.setText(QCoreApplication.translate("adjustment_dialog", u"Cancel", None))
    # retranslateUi

