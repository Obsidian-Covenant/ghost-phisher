# gui/whats_new_ui.py

from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog: QtWidgets.QDialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(638, 324)

        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap("images/icon.png"),
            QtGui.QIcon.Mode.Normal,
            QtGui.QIcon.State.Off
        )
        Dialog.setWindowIcon(icon)

        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")

        self.webView = QtWidgets.QTextBrowser(Dialog)
        self.webView.setOpenExternalLinks(True)
        self.webView.setObjectName("webView")
        self.verticalLayout.addWidget(self.webView)

        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.whats_new_check = QtWidgets.QCheckBox(Dialog)
        self.whats_new_check.setObjectName("whats_new_check")
        self.horizontalLayout.addWidget(self.whats_new_check)

        spacerItem = QtWidgets.QSpacerItem(
            40, 20,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum
        )
        self.horizontalLayout.addItem(spacerItem)

        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _tr = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_tr("Dialog", "Whats New"))
        self.whats_new_check.setText(_tr("Dialog", "Dont show again until next update"))
