# gui/font_settings.py

#######################################################
#           GHOST PHISHER FONT SETTINGS               #
#######################################################

import os

from PyQt6 import QtCore, QtGui, QtWidgets

from .settings import *

cwd = os.getcwd()
settings_object = Ghost_settings()


class Ui_font_settings(object):
    def setupUi(self, font_settings: QtWidgets.QDialog):
        font_settings.setObjectName("font_settings")
        font_settings.resize(318, 121)

        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap(f"{cwd}/gui/images/icon.png"),
            QtGui.QIcon.Mode.Normal,
            QtGui.QIcon.State.Off,
        )
        font_settings.setWindowIcon(icon)

        self.layoutWidget = QtWidgets.QWidget(parent=font_settings)
        self.layoutWidget.setGeometry(QtCore.QRect(9, 9, 300, 25))
        self.layoutWidget.setObjectName("layoutWidget")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.label = QtWidgets.QLabel(parent=self.layoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)

        spacerItem = QtWidgets.QSpacerItem(
            20, 18, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding
        )
        self.verticalLayout.addItem(spacerItem)

        self.layoutWidget1 = QtWidgets.QWidget(parent=font_settings)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 70, 300, 38))
        self.layoutWidget1.setObjectName("layoutWidget1")

        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        spacerItem1 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum
        )
        self.horizontalLayout.addItem(spacerItem1)

        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        spacerItem2 = QtWidgets.QSpacerItem(
            20, 18, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding
        )
        self.verticalLayout_2.addItem(spacerItem2)

        self.buttonBox = QtWidgets.QDialogButtonBox(parent=self.layoutWidget1)
        self.buttonBox.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(
            QtWidgets.QDialogButtonBox.StandardButton.Cancel
            | QtWidgets.QDialogButtonBox.StandardButton.Ok
        )
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_2.addWidget(self.buttonBox)

        self.horizontalLayout.addLayout(self.verticalLayout_2)

        spacerItem3 = QtWidgets.QSpacerItem(
            48, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum
        )
        self.horizontalLayout.addItem(spacerItem3)

        self.layoutWidget2 = QtWidgets.QWidget(parent=font_settings)
        self.layoutWidget2.setGeometry(QtCore.QRect(9, 40, 301, 22))
        self.layoutWidget2.setObjectName("layoutWidget2")

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        self.label_2 = QtWidgets.QLabel(parent=self.layoutWidget2)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)

        self.font_combo = QtWidgets.QComboBox(parent=self.layoutWidget2)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed
        )
        self.font_combo.setSizePolicy(sizePolicy)
        self.font_combo.setObjectName("font_combo")
        self.horizontalLayout_2.addWidget(self.font_combo)

        self.retranslateUi(font_settings)

        # Modern signal connections
        self.buttonBox.accepted.connect(font_settings.accept)
        self.buttonBox.rejected.connect(font_settings.reject)

        QtCore.QMetaObject.connectSlotsByName(font_settings)

    def retranslateUi(self, font_settings):
        _tr = QtCore.QCoreApplication.translate
        font_settings.setWindowTitle(_tr("font_settings", "Ghost Font Settings"))
        self.label.setText(_tr("font_settings", "Current font:"))
        self.label_2.setText(_tr("font_settings", "Font:"))


class font_settings(QtWidgets.QDialog, Ui_font_settings):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        current = settings_object.read_last_settings("font-settings")
        self.label.setText(
            f"Current font:<font color=green><b>\t {current}</b></font>"
        )

        font_numbers = [str(i) for i in range(1, 21)]
        self.font_combo.addItems(font_numbers)

        self.buttonBox.accepted.connect(self.set_font)

    def set_font(self):
        """Writes font settings to last_setting"""
        prefered_font = self.font_combo.currentText()
        settings_object.create_settings("font-settings", prefered_font)
        settings_object.close_setting_file()
        self.close()

        QtWidgets.QMessageBox.information(
            self, "Font Changes", "Please restart application to apply changes"
        )
