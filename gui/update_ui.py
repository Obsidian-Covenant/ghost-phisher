# gui/update_ui.py

from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog: QtWidgets.QDialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(422, 95)

        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")

        self.update_display_label = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        font.setWeight(75)
        font.setItalic(False)
        font.setBold(True)
        self.update_display_label.setFont(font)
        self.update_display_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.update_display_label.setObjectName("update_display_label")
        self.verticalLayout.addWidget(self.update_display_label)

        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.upgrade_button = QtWidgets.QPushButton(Dialog)
        self.upgrade_button.setObjectName("upgrade_button")
        self.verticalLayout.addWidget(self.upgrade_button)

        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _tr = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_tr("Dialog", "New Update is Available"))
        self.update_display_label.setText(_tr("Dialog", "Version 1.53 Available"))
        self.label_2.setText(_tr("Dialog", "To upgrade to the new version, please press the upgrade button "))
        self.upgrade_button.setText(_tr("Dialog", "Upgrade"))
