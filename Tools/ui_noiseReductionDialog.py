# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'noiseReductionDialogGhIGnq.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_noiseReduction_dialog(object):
    def setupUi(self, noiseReduction_dialog):
        if not noiseReduction_dialog.objectName():
            noiseReduction_dialog.setObjectName(u"noiseReduction_dialog")
        noiseReduction_dialog.resize(194, 92)
        self.horizontalLayout_2 = QHBoxLayout(noiseReduction_dialog)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(noiseReduction_dialog)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.IntensityInput = QSpinBox(noiseReduction_dialog)
        self.IntensityInput.setObjectName(u"IntensityInput")

        self.verticalLayout.addWidget(self.IntensityInput)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.okBtn = QPushButton(noiseReduction_dialog)
        self.okBtn.setObjectName(u"okBtn")

        self.horizontalLayout.addWidget(self.okBtn)

        self.cancelBtn = QPushButton(noiseReduction_dialog)
        self.cancelBtn.setObjectName(u"cancelBtn")

        self.horizontalLayout.addWidget(self.cancelBtn)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.horizontalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(noiseReduction_dialog)

        QMetaObject.connectSlotsByName(noiseReduction_dialog)
    # setupUi

    def retranslateUi(self, noiseReduction_dialog):
        noiseReduction_dialog.setWindowTitle(QCoreApplication.translate("noiseReduction_dialog", u"Noise Reduction", None))
        self.label.setText(QCoreApplication.translate("noiseReduction_dialog", u"Intensity", None))
        self.okBtn.setText(QCoreApplication.translate("noiseReduction_dialog", u"Ok", None))
        self.cancelBtn.setText(QCoreApplication.translate("noiseReduction_dialog", u"Cancel", None))
    # retranslateUi

