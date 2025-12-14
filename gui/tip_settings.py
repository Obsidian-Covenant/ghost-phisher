# gui/tip_settings.py

#######################################################
#           GHOST PHISHER TIPS                        #
#######################################################
import os

from . import settings

from PyQt6 import QtCore, QtGui, QtWidgets

cwd = os.getcwd()


class Ui_tip(object):
    def setupUi(self, tip: QtWidgets.QDialog):
        tip.setObjectName("tip")
        tip.resize(499, 131)

        self.horizontalLayout = QtWidgets.QHBoxLayout(tip)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        self.label = QtWidgets.QLabel(tip)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(f"{cwd}/gui/images/tip.png"))
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)

        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")

        self.label_2 = QtWidgets.QLabel(tip)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)

        self.label_3 = QtWidgets.QLabel(tip)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)

        self.label_4 = QtWidgets.QLabel(tip)
        font = QtGui.QFont()
        font.setUnderline(True)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        # Optional but handy: make the link clickable in Qt6
        self.label_4.setOpenExternalLinks(True)
        self.verticalLayout.addWidget(self.label_4)

        self.label_5 = QtWidgets.QLabel(tip)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)

        spacerItem = QtWidgets.QSpacerItem(
            20, 8,
            QtWidgets.QSizePolicy.Policy.Minimum,
            QtWidgets.QSizePolicy.Policy.Fixed
        )
        self.verticalLayout.addItem(spacerItem)

        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.checkBox = QtWidgets.QCheckBox(tip)
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout_2.addWidget(self.checkBox)

        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.horizontalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(tip)
        QtCore.QMetaObject.connectSlotsByName(tip)

    def retranslateUi(self, tip):
        _tr = QtCore.QCoreApplication.translate
        tip.setWindowTitle(_tr("tip", "Ghost Phisher Tips"))
        self.label_2.setText(_tr(
            "tip",
            "Press the F2 Key from the keyboard to get font settings, if you have problems with"
        ))
        self.label_3.setText(_tr(
            "tip",
            "understanding how to use this application then visit:"
        ))
        self.label_4.setText(_tr(
            "tip",
            "<a href=\"https://code.google.com/p/ghost-phisher/\">https://code.google.com/p/ghost-phisher</a> "
        ))
        self.label_5.setText(_tr(
            "tip",
            "for a video tutorial on how to use the application."
        ))
        self.checkBox.setText(_tr("tip", "Dont show this message again"))


class tip_settings(QtWidgets.QDialog, Ui_tip):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.settings_object = settings.Ghost_settings()

        # New-style signal
        self.checkBox.clicked.connect(self.set_tip)

    def set_tip(self):
        if self.checkBox.isChecked():
            self.settings_object.create_settings("tip-settings", "0")
        else:
            self.settings_object.create_settings("tip-settings", "1")
