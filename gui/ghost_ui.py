import os
from . import settings

from PyQt6 import QtCore, QtGui, QtWidgets

cwd = os.getcwd()
setting_file = settings.Ghost_settings()


class Ui_ghost_phisher(object):
    def setupUi(self, ghost_phisher):
        ghost_phisher.setObjectName("ghost_phisher")
        ghost_phisher.resize(960, 629)

        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap(f"{cwd}/gui/images/icon.png"),
            QtGui.QIcon.Mode.Normal,
            QtGui.QIcon.State.Off,
        )
        ghost_phisher.setWindowIcon(icon)

        self.centralwidget = QtWidgets.QWidget(ghost_phisher)
        self.centralwidget.setObjectName("centralwidget")

        self.verticalLayout_66 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_66.setObjectName("verticalLayout_66")

        self.ghost_phisher_version_label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setWeight(75)
        font.setBold(True)
        self.ghost_phisher_version_label.setFont(font)
        self.ghost_phisher_version_label.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignRight
            | QtCore.Qt.AlignmentFlag.AlignTrailing
            | QtCore.Qt.AlignmentFlag.AlignVCenter
        )
        self.ghost_phisher_version_label.setObjectName("ghost_phisher_version_label")
        self.verticalLayout_66.addWidget(self.ghost_phisher_version_label)

        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)

        font = QtGui.QFont()
        if setting_file.setting_exists("font-settings"):
            font.setPointSize(int(setting_file.read_last_settings("font-settings")))
        else:
            font.setPointSize(7)
            setting_file.create_settings("font-settings", 7)

        self.tabWidget.setFont(font)
        self.tabWidget.setStatusTip("")
        self.tabWidget.setObjectName("tabWidget")

        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")

        self.verticalLayout_36 = QtWidgets.QVBoxLayout(self.tab_5)
        self.verticalLayout_36.setObjectName("verticalLayout_36")

        self.groupBox_15 = QtWidgets.QGroupBox(self.tab_5)
        self.groupBox_15.setObjectName("groupBox_15")

        self.verticalLayout_35 = QtWidgets.QVBoxLayout(self.groupBox_15)
        self.verticalLayout_35.setObjectName("verticalLayout_35")

        self.verticalLayout_34 = QtWidgets.QVBoxLayout()
        self.verticalLayout_34.setObjectName("verticalLayout_34")

        self.horizontalLayout_40 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_40.setObjectName("horizontalLayout_40")

        self.access_point_label = QtWidgets.QLabel(self.groupBox_15)
        self.access_point_label.setObjectName("access_point_label")
        self.horizontalLayout_40.addWidget(self.access_point_label)

        self.channel_label = QtWidgets.QLabel(self.groupBox_15)
        self.channel_label.setObjectName("channel_label")
        self.horizontalLayout_40.addWidget(self.channel_label)

        self.ip_address_label = QtWidgets.QLabel(self.groupBox_15)
        self.ip_address_label.setObjectName("ip_address_label")
        self.horizontalLayout_40.addWidget(self.ip_address_label)

        self.main_mac_address_label = QtWidgets.QLabel(self.groupBox_15)
        self.main_mac_address_label.setObjectName("main_mac_address_label")
        self.horizontalLayout_40.addWidget(self.main_mac_address_label)

        self.verticalLayout_34.addLayout(self.horizontalLayout_40)

        self.access_runtime = QtWidgets.QLabel(self.groupBox_15)
        self.access_runtime.setObjectName("access_runtime")
        self.verticalLayout_34.addWidget(self.access_runtime)

        self.verticalLayout_35.addLayout(self.verticalLayout_34)
        self.verticalLayout_36.addWidget(self.groupBox_15)

        self.groupBox_14 = QtWidgets.QGroupBox(self.tab_5)
        self.groupBox_14.setObjectName("groupBox_14")

        self.verticalLayout_32 = QtWidgets.QVBoxLayout(self.groupBox_14)
        self.verticalLayout_32.setObjectName("verticalLayout_32")

        self.horizontalLayout_42 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_42.setObjectName("horizontalLayout_42")

        spacerItem = QtWidgets.QSpacerItem(
            213, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum
        )
        self.horizontalLayout_42.addItem(spacerItem)

        self.horizontalLayout_41 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_41.setObjectName("horizontalLayout_41")

        self.comboBox = QtWidgets.QComboBox(self.groupBox_14)
        self.comboBox.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Preferred,
            QtWidgets.QSizePolicy.Policy.Preferred,
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout_41.addWidget(self.comboBox)

        spacerItem1 = QtWidgets.QSpacerItem(
            11, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum
        )
        self.horizontalLayout_41.addItem(spacerItem1)

        self.refresh_button = QtWidgets.QPushButton(self.groupBox_14)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Fixed,
            QtWidgets.QSizePolicy.Policy.Preferred,
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.refresh_button.sizePolicy().hasHeightForWidth())
        self.refresh_button.setSizePolicy(sizePolicy)
        self.refresh_button.setObjectName("refresh_button")
        self.horizontalLayout_41.addWidget(self.refresh_button)

        self.horizontalLayout_42.addLayout(self.horizontalLayout_41)

        spacerItem2 = QtWidgets.QSpacerItem(
            183, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum
        )
        self.horizontalLayout_42.addItem(spacerItem2)

        self.verticalLayout_32.addLayout(self.horizontalLayout_42)

        spacerItem3 = QtWidgets.QSpacerItem(
            20, 11, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed
        )
        self.verticalLayout_32.addItem(spacerItem3)

        self.horizontalLayout_38 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_38.setObjectName("horizontalLayout_38")

        self.acess_interface = QtWidgets.QLabel(self.groupBox_14)
        self.acess_interface.setObjectName("acess_interface")
        self.horizontalLayout_38.addWidget(self.acess_interface)

        self.mac_address_label = QtWidgets.QLabel(self.groupBox_14)
        self.mac_address_label.setObjectName("mac_address_label")
        self.horizontalLayout_38.addWidget(self.mac_address_label)

        self.driver_label = QtWidgets.QLabel(self.groupBox_14)
        self.driver_label.setObjectName("driver_label")
        self.horizontalLayout_38.addWidget(self.driver_label)

        self.monitor_label = QtWidgets.QLabel(self.groupBox_14)
        self.monitor_label.setObjectName("monitor_label")
        self.horizontalLayout_38.addWidget(self.monitor_label)

        self.verticalLayout_32.addLayout(self.horizontalLayout_38)

        spacerItem4 = QtWidgets.QSpacerItem(
            20, 11, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed
        )
        self.verticalLayout_32.addItem(spacerItem4)

        self.horizontalLayout_39 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_39.setObjectName("horizontalLayout_39")

        self.monitor_button = QtWidgets.QPushButton(self.groupBox_14)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Minimum,
            QtWidgets.QSizePolicy.Policy.Preferred,
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.monitor_button.sizePolicy().hasHeightForWidth())
        self.monitor_button.setSizePolicy(sizePolicy)
        self.monitor_button.setObjectName("monitor_button")
        self.horizontalLayout_39.addWidget(self.monitor_button)

        spacerItem5 = QtWidgets.QSpacerItem(
            0, 18, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred
        )
        self.horizontalLayout_39.addItem(spacerItem5)

        self.verticalLayout_32.addLayout(self.horizontalLayout_39)

        spacerItem6 = QtWidgets.QSpacerItem(
            20, 11, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed
        )
        self.verticalLayout_32.addItem(spacerItem6)

        self.verticalLayout_36.addWidget(self.groupBox_14)

        self.groupBox_16 = QtWidgets.QGroupBox(self.tab_5)
        self.groupBox_16.setObjectName("groupBox_16")

        self.verticalLayout_33 = QtWidgets.QVBoxLayout(self.groupBox_16)
        self.verticalLayout_33.setObjectName("verticalLayout_33")

        self.horizontalLayout_37 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_37.setObjectName("horizontalLayout_37")

        self.verticalLayout_31 = QtWidgets.QVBoxLayout()
        self.verticalLayout_31.setObjectName("verticalLayout_31")

        self.horizontalLayout_35 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_35.setObjectName("horizontalLayout_35")

        self.verticalLayout_28 = QtWidgets.QVBoxLayout()
        self.verticalLayout_28.setObjectName("verticalLayout_28")

        self.label_36 = QtWidgets.QLabel(self.groupBox_16)
        self.label_36.setObjectName("label_36")
        self.verticalLayout_28.addWidget(self.label_36)

        self.label_37 = QtWidgets.QLabel(self.groupBox_16)
        self.label_37.setObjectName("label_37")
        self.verticalLayout_28.addWidget(self.label_37)

        self.horizontalLayout_35.addLayout(self.verticalLayout_28)

        self.verticalLayout_27 = QtWidgets.QVBoxLayout()
        self.verticalLayout_27.setObjectName("verticalLayout_27")

        self.access_name_edit = QtWidgets.QLineEdit(self.groupBox_16)
        self.access_name_edit.setObjectName("access_name_edit")
        self.verticalLayout_27.addWidget(self.access_name_edit)

        self.ip_address_label_2 = QtWidgets.QLineEdit(self.groupBox_16)
        self.ip_address_label_2.setObjectName("ip_address_label_2")
        self.verticalLayout_27.addWidget(self.ip_address_label_2)

        self.horizontalLayout_35.addLayout(self.verticalLayout_27)
        self.verticalLayout_31.addLayout(self.horizontalLayout_35)

        self.horizontalLayout_36 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_36.setObjectName("horizontalLayout_36")

        self.label_38 = QtWidgets.QLabel(self.groupBox_16)
        self.label_38.setObjectName("label_38")
        self.horizontalLayout_36.addWidget(self.label_38)

        self.channel_combo = QtWidgets.QComboBox(self.groupBox_16)
        self.channel_combo.setObjectName("channel_combo")
        self.horizontalLayout_36.addWidget(self.channel_combo)

        spacerItem7 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum
        )
        self.horizontalLayout_36.addItem(spacerItem7)

        self.verticalLayout_31.addLayout(self.horizontalLayout_36)
        self.horizontalLayout_37.addLayout(self.verticalLayout_31)

        spacerItem8 = QtWidgets.QSpacerItem(
            13, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum
        )
        self.horizontalLayout_37.addItem(spacerItem8)

        self.groupBox_18 = QtWidgets.QGroupBox(self.groupBox_16)
        self.groupBox_18.setObjectName("groupBox_18")

        self.horizontalLayout_32 = QtWidgets.QHBoxLayout(self.groupBox_18)
        self.horizontalLayout_32.setObjectName("horizontalLayout_32")

        self.horizontalLayout_34 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_34.setObjectName("horizontalLayout_34")

        self.rouge_radio = QtWidgets.QRadioButton(self.groupBox_18)
        self.rouge_radio.setChecked(True)
        self.rouge_radio.setObjectName("rouge_radio")
        self.horizontalLayout_34.addWidget(self.rouge_radio)

        spacerItem9 = QtWidgets.QSpacerItem(
            28, 11, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum
        )
        self.horizontalLayout_34.addItem(spacerItem9)

        self.wpa_radio = QtWidgets.QRadioButton(self.groupBox_18)
        self.wpa_radio.setObjectName("wpa_radio")
        self.horizontalLayout_34.addWidget(self.wpa_radio)

        spacerItem10 = QtWidgets.QSpacerItem(
            28, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum
        )
        self.horizontalLayout_34.addItem(spacerItem10)

        self.wep_radio = QtWidgets.QRadioButton(self.groupBox_18)
        self.wep_radio.setObjectName("wep_radio")
        self.horizontalLayout_34.addWidget(self.wep_radio)

        self.lineEdit = QtWidgets.QLineEdit(self.groupBox_18)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_34.addWidget(self.lineEdit)

        self.horizontalLayout_32.addLayout(self.horizontalLayout_34)
        self.horizontalLayout_37.addWidget(self.groupBox_18)

        self.verticalLayout_33.addLayout(self.horizontalLayout_37)
        self.verticalLayout_36.addWidget(self.groupBox_16)

        self.groupBox_17 = QtWidgets.QGroupBox(self.tab_5)
        self.groupBox_17.setObjectName("groupBox_17")

        self.verticalLayout_29 = QtWidgets.QVBoxLayout(self.groupBox_17)
        self.verticalLayout_29.setObjectName("verticalLayout_29")

        self.access_textbrowser = QtWidgets.QTextBrowser(self.groupBox_17)
        self.access_textbrowser.setObjectName("access_textbrowser")
        self.verticalLayout_29.addWidget(self.access_textbrowser)

        self.verticalLayout_36.addWidget(self.groupBox_17)

        self.verticalLayout_30 = QtWidgets.QVBoxLayout()
        self.verticalLayout_30.setObjectName("verticalLayout_30")

        self.access_connection_label = QtWidgets.QLabel(self.tab_5)
        self.access_connection_label.setObjectName("access_connection_label")
        self.verticalLayout_30.addWidget(self.access_connection_label)

        self.horizontalLayout_33 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_33.setObjectName("horizontalLayout_33")

        spacerItem11 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum
        )
        self.horizontalLayout_33.addItem(spacerItem11)

        self.access_start = QtWidgets.QPushButton(self.tab_5)
        self.access_start.setObjectName("access_start")
        self.horizontalLayout_33.addWidget(self.access_start)

        spacerItem12 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum
        )
        self.horizontalLayout_33.addItem(spacerItem12)

        self.access_stop = QtWidgets.QPushButton(self.tab_5)
        self.access_stop.setObjectName("access_stop")
        self.horizontalLayout_33.addWidget(self.access_stop)

        spacerItem13 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum
        )
        self.horizontalLayout_33.addItem(spacerItem13)

        self.verticalLayout_30.addLayout(self.horizontalLayout_33)
        self.verticalLayout_36.addLayout(self.verticalLayout_30)

        self.tabWidget.addTab(self.tab_5, "")

        self.dns_tab = QtWidgets.QWidget()
        self.dns_tab.setObjectName("dns_tab")

        self.verticalLayout_25 = QtWidgets.QVBoxLayout(self.dns_tab)
        self.verticalLayout_25.setObjectName("verticalLayout_25")

        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")

        self.groupBox = QtWidgets.QGroupBox(self.dns_tab)
        self.groupBox.setObjectName("groupBox")

        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")

        self.card_interface_combo = QtWidgets.QComboBox(self.groupBox)
        self.card_interface_combo.setObjectName("card_interface_combo")
        self.horizontalLayout_4.addWidget(self.card_interface_combo)

        spacerItem14 = QtWidgets.QSpacerItem(
            102, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum
        )
        self.horizontalLayout_4.addItem(spacerItem14)

        self.ip_address_combo = QtWidgets.QComboBox(self.groupBox)
        self.ip_address_combo.setObjectName("ip_address_combo")
        self.horizontalLayout_4.addWidget(self.ip_address_combo)

        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")

        self.current_card_label = QtWidgets.QLabel(self.groupBox)
        self.current_card_label.setObjectName("current_card_label")
        self.horizontalLayout_5.addWidget(self.current_card_label)

        spacerItem15 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum
        )
        self.horizontalLayout_5.addItem(spacerItem15)

        self.service_dns_run_label = QtWidgets.QLabel(self.groupBox)
        self.service_dns_run_label.setObjectName("service_dns_run_label")
        self.horizontalLayout_5.addWidget(self.service_dns_run_label)

        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")

        self.dns_port = QtWidgets.QLabel(self.groupBox)
        self.dns_port.setObjectName("dns_port")
        self.horizontalLayout_6.addWidget(self.dns_port)

        spacerItem16 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum
        )
        self.horizontalLayout_6.addItem(spacerItem16)

        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_6.addWidget(self.label_5)

        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.verticalLayout_5.addWidget(self.groupBox)

        self.groupBox_2 = QtWidgets.QGroupBox(self.dns_tab)
        self.groupBox_2.setObjectName("groupBox_2")

        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")

        self.resolveall_radio = QtWidgets.QRadioButton(self.groupBox_2)
        self.resolveall_radio.setChecked(True)
        self.resolveall_radio.setObjectName("resolveall_radio")
        self.verticalLayout_4.addWidget(self.resolveall_radio)

        self.dns_ip_address = QtWidgets.QLineEdit(self.groupBox_2)
        self.dns_ip_address.setText("")
        self.dns_ip_address.setObjectName("dns_ip_address")
        self.verticalLayout_4.addWidget(self.dns_ip_address)

        self.respond_domain_radio = QtWidgets.QRadioButton(self.groupBox_2)
        self.respond_domain_radio.setEnabled(True)
        self.respond_domain_radio.setObjectName("respond_domain_radio")
        self.verticalLayout_4.addWidget(self.respond_domain_radio)

        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")

        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_3.addWidget(self.label_6)

        self.domain_ip = QtWidgets.QLineEdit(self.groupBox_2)
        self.domain_ip.setObjectName("domain_ip")
        self.horizontalLayout_3.addWidget(self.domain_ip)

        spacerItem17 = QtWidgets.QSpacerItem(
            12, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum
        )
        self.horizontalLayout_3.addItem(spacerItem17)

        self.label_7 = QtWidgets.QLabel(self.groupBox_2)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_3.addWidget(self.label_7)

        self.domain_label = QtWidgets.QLineEdit(self.groupBox_2)
        self.domain_label.setObjectName("domain_label")
        self.horizontalLayout_3.addWidget(self.domain_label)

        self.verticalLayout_4.addLayout(self.horizontalLayout_3)

        self.domain_add_button = QtWidgets.QPushButton(self.groupBox_2)
        self.domain_add_button.setObjectName("domain_add_button")
        self.verticalLayout_4.addWidget(self.domain_add_button)

        self.verticalLayout_5.addWidget(self.groupBox_2)

        self.groupBox_3 = QtWidgets.QGroupBox(self.dns_tab)
        self.groupBox_3.setObjectName("groupBox_3")

        self.verticalLayout_24 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_24.setObjectName("verticalLayout_24")

        self.dns_textbrowser = QtWidgets.QTextBrowser(self.groupBox_3)
        self.dns_textbrowser.setObjectName("dns_textbrowser")
        self.verticalLayout_24.addWidget(self.dns_textbrowser)

        self.verticalLayout_5.addWidget(self.groupBox_3)

        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")

        self.dns_connection_label = QtWidgets.QLabel(self.dns_tab)
        self.dns_connection_label.setObjectName("dns_connection_label")
        self.verticalLayout.addWidget(self.dns_connection_label)

        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")

        spacerItem18 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum
        )
        self.horizontalLayout.addItem(spacerItem18)

        self.dns_start = QtWidgets.QPushButton(self.dns_tab)
        self.dns_start.setObjectName("dns_start")
        self.horizontalLayout.addWidget(self.dns_start)

        spacerItem19 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum
        )
        self.horizontalLayout.addItem(spacerItem19)

        self.dns_stop = QtWidgets.QPushButton(self.dns_tab)
        self.dns_stop.setObjectName("dns_stop")
        self.horizontalLayout.addWidget(self.dns_stop)

        spacerItem20 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum
        )
        self.horizontalLayout.addItem(spacerItem20)

        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_5.addLayout(self.verticalLayout)

        self.verticalLayout_25.addLayout(self.verticalLayout_5)
        self.tabWidget.addTab(self.dns_tab, "")

        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")

        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_16.setObjectName("verticalLayout_16")

        self.groupBox_4 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_4.setObjectName("groupBox_4")

        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.groupBox_4)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")

        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")

        self.label = QtWidgets.QLabel(self.groupBox_4)
        self.label.setObjectName("label")
        self.verticalLayout_6.addWidget(self.label)

        self.label_2 = QtWidgets.QLabel(self.groupBox_4)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_6.addWidget(self.label_2)

        self.label_3 = QtWidgets.QLabel(self.groupBox_4)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_6.addWidget(self.label_3)

        self.horizontalLayout_9.addLayout(self.verticalLayout_6)
        self.verticalLayout_16.addWidget(self.groupBox_4)

        self.groupBox_5 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_5.setObjectName("groupBox_5")

        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.groupBox_5)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")

        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")

        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")

        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")

        self.label_4 = QtWidgets.QLabel(self.groupBox_5)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_3.addWidget(self.label_4)

        self.label_9 = QtWidgets.QLabel(self.groupBox_5)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_3.addWidget(self.label_9)

        self.label_10 = QtWidgets.QLabel(self.groupBox_5)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_3.addWidget(self.label_10)

        self.horizontalLayout_8.addLayout(self.verticalLayout_3)

        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")

        self.start_ip = QtWidgets.QLineEdit(self.groupBox_5)
        self.start_ip.setObjectName("start_ip")
        self.verticalLayout_9.addWidget(self.start_ip)

        self.subnet_ip = QtWidgets.QLineEdit(self.groupBox_5)
        self.subnet_ip.setObjectName("subnet_ip")
        self.verticalLayout_9.addWidget(self.subnet_ip)

        self.fakedns_ip = QtWidgets.QLineEdit(self.groupBox_5)
        self.fakedns_ip.setObjectName("fakedns_ip")
        self.verticalLayout_9.addWidget(self.fakedns_ip)

        self.horizontalLayout_8.addLayout(self.verticalLayout_9)
        self.horizontalLayout_10.addLayout(self.horizontalLayout_8)

        spacerItem21 = QtWidgets.QSpacerItem(
            13, 78, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum
        )
        self.horizontalLayout_10.addItem(spacerItem21)

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")

        self.label_8 = QtWidgets.QLabel(self.groupBox_5)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_7.addWidget(self.label_8)

        self.label_12 = QtWidgets.QLabel(self.groupBox_5)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_7.addWidget(self.label_12)

        self.label_11 = QtWidgets.QLabel(self.groupBox_5)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_7.addWidget(self.label_11)

        self.horizontalLayout_2.addLayout(self.verticalLayout_7)

        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")

        self.stop_ip = QtWidgets.QLineEdit(self.groupBox_5)
        self.stop_ip.setObjectName("stop_ip")
        self.verticalLayout_8.addWidget(self.stop_ip)

        self.gateway_ip = QtWidgets.QLineEdit(self.groupBox_5)
        self.gateway_ip.setObjectName("gateway_ip")
        self.verticalLayout_8.addWidget(self.gateway_ip)

        self.alternatedns_ip = QtWidgets.QLineEdit(self.groupBox_5)
        self.alternatedns_ip.setObjectName("alternatedns_ip")
        self.verticalLayout_8.addWidget(self.alternatedns_ip)

        self.horizontalLayout_2.addLayout(self.verticalLayout_8)
        self.horizontalLayout_10.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_12.addLayout(self.horizontalLayout_10)

        self.verticalLayout_16.addWidget(self.groupBox_5)

        self.groupBox_6 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_6.setObjectName("groupBox_6")

        self.verticalLayout_23 = QtWidgets.QVBoxLayout(self.groupBox_6)
        self.verticalLayout_23.setObjectName("verticalLayout_23")

        self.dhcp_status = QtWidgets.QTextBrowser(self.groupBox_6)
        self.dhcp_status.setObjectName("dhcp_status")
        self.verticalLayout_23.addWidget(self.dhcp_status)

        self.verticalLayout_16.addWidget(self.groupBox_6)

        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")

        spacerItem22 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum
        )
        self.horizontalLayout_13.addItem(spacerItem22)

        self.dhcp_start = QtWidgets.QPushButton(self.tab_2)
        self.dhcp_start.setObjectName("dhcp_start")
        self.horizontalLayout_13.addWidget(self.dhcp_start)

        spacerItem23 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum
        )
        self.horizontalLayout_13.addItem(spacerItem23)

        self.dhcp_stop = QtWidgets.QPushButton(self.tab_2)
        self.dhcp_stop.setObjectName("dhcp_stop")
        self.horizontalLayout_13.addWidget(self.dhcp_stop)

        spacerItem24 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum
        )
        self.horizontalLayout_13.addItem(spacerItem24)

        self.verticalLayout_16.addLayout(self.horizontalLayout_13)
        self.tabWidget.addTab(self.tab_2, "")

        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")

        self.verticalLayout_17 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_17.setObjectName("verticalLayout_17")

        self.groupBox_7 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_7.setObjectName("groupBox_7")

        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.groupBox_7)
        self.verticalLayout_11.setObjectName("verticalLayout_11")

        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")

        self.http_interface_combo = QtWidgets.QComboBox(self.groupBox_7)
        self.http_interface_combo.setObjectName("http_interface_combo")
        self.horizontalLayout_7.addWidget(self.http_interface_combo)

        spacerItem25 = QtWidgets.QSpacerItem(
            102, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum
        )
        self.horizontalLayout_7.addItem(spacerItem25)

        self.http_ip_combo = QtWidgets.QComboBox(self.groupBox_7)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Preferred,
            QtWidgets.QSizePolicy.Policy.Preferred,
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(16)
        sizePolicy.setHeightForWidth(self.http_ip_combo.sizePolicy().hasHeightForWidth())
        self.http_ip_combo.setSizePolicy(sizePolicy)
        self.http_ip_combo.setObjectName("http_ip_combo")
        self.horizontalLayout_7.addWidget(self.http_ip_combo)

        self.verticalLayout_11.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")

        self.current_card_label_2 = QtWidgets.QLabel(self.groupBox_7)
        self.current_card_label_2.setObjectName("current_card_label_2")
        self.horizontalLayout_15.addWidget(self.current_card_label_2)

        spacerItem26 = QtWidgets.QSpacerItem(
            70, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum
        )
        self.horizontalLayout_15.addItem(spacerItem26)

        self.http_ip_label = QtWidgets.QLabel(self.groupBox_7)
        self.http_ip_label.setToolTip("")
        self.http_ip_label.setObjectName("http_ip_label")
        self.horizontalLayout_15.addWidget(self.http_ip_label)

        self.verticalLayout_11.addLayout(self.horizontalLayout_15)

        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")

        self.http_port_label = QtWidgets.QLabel(self.groupBox_7)
        self.http_port_label.setObjectName("http_port_label")
        self.horizontalLayout_16.addWidget(self.http_port_label)

        spacerItem27 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum
        )
        self.horizontalLayout_16.addItem(spacerItem27)

        self.label_13 = QtWidgets.QLabel(self.groupBox_7)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_16.addWidget(self.label_13)

        self.verticalLayout_11.addLayout(self.horizontalLayout_16)
        self.verticalLayout_17.addWidget(self.groupBox_7)

        self.groupBox_8 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_8.setObjectName("groupBox_8")

        self.verticalLayout_61 = QtWidgets.QVBoxLayout(self.groupBox_8)
        self.verticalLayout_61.setObjectName("verticalLayout_61")

        self.horizontalLayout_20 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")

        self.verticalLayout_43 = QtWidgets.QVBoxLayout()
        self.verticalLayout_43.setObjectName("verticalLayout_43")

        self.emulate_website_radio = QtWidgets.QRadioButton(self.groupBox_8)
        self.emulate_website_radio.setObjectName("emulate_website_radio")
        self.verticalLayout_43.addWidget(self.emulate_website_radio)

        self.select_website_radio = QtWidgets.QRadioButton(self.groupBox_8)
        self.select_website_radio.setChecked(True)
        self.select_website_radio.setObjectName("select_website_radio")
        self.verticalLayout_43.addWidget(self.select_website_radio)

        self.horizontalLayout_20.addLayout(self.verticalLayout_43)

        self.verticalLayout_15 = QtWidgets.QVBoxLayout()
        self.verticalLayout_15.setObjectName("verticalLayout_15")

        self.emulate_website_label = QtWidgets.QLineEdit(self.groupBox_8)
        self.emulate_website_label.setStatusTip("")
        self.emulate_website_label.setInputMask("")
        self.emulate_website_label.setText("")
        self.emulate_website_label.setEchoMode(QtWidgets.QLineEdit.EchoMode.Normal)
        self.emulate_website_label.setDragEnabled(False)
        self.emulate_website_label.setReadOnly(False)
        self.emulate_website_label.setObjectName("emulate_website_label")
        self.verticalLayout_15.addWidget(self.emulate_website_label)

        self.horizontalLayout_19 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")

        self.website_linedit = QtWidgets.QLineEdit(self.groupBox_8)
        self.website_linedit.setObjectName("website_linedit")
        self.horizontalLayout_19.addWidget(self.website_linedit)

        self.website_button = QtWidgets.QPushButton(self.groupBox_8)
        self.website_button.setObjectName("website_button")
        self.horizontalLayout_19.addWidget(self.website_button)

        self.verticalLayout_15.addLayout(self.horizontalLayout_19)
        self.horizontalLayout_20.addLayout(self.verticalLayout_15)

        self.verticalLayout_61.addLayout(self.horizontalLayout_20)

        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")

        self.label_25 = QtWidgets.QLabel(self.groupBox_8)
        self.label_25.setObjectName("label_25")
        self.horizontalLayout_11.addWidget(self.label_25)

        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox_8)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_11.addWidget(self.lineEdit_2)

        self.horizontalLayout_43 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_43.setObjectName("horizontalLayout_43")

        self.run_webpage_port_radio = QtWidgets.QCheckBox(self.groupBox_8)
        self.run_webpage_port_radio.setObjectName("run_webpage_port_radio")
        self.horizontalLayout_43.addWidget(self.run_webpage_port_radio)

        self.use_port_http = QtWidgets.QLineEdit(self.groupBox_8)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Fixed,
            QtWidgets.QSizePolicy.Policy.Fixed,
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.use_port_http.sizePolicy().hasHeightForWidth())
        self.use_port_http.setSizePolicy(sizePolicy)
        self.use_port_http.setObjectName("use_port_http")
        self.horizontalLayout_43.addWidget(self.use_port_http)

        self.label_14 = QtWidgets.QLabel(self.groupBox_8)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_43.addWidget(self.label_14)

        self.horizontalLayout_11.addLayout(self.horizontalLayout_43)
        self.verticalLayout_61.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_21 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")

        spacerItem28 = QtWidgets.QSpacerItem(
            0, 0, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum
        )
        self.horizontalLayout_21.addItem(spacerItem28)

        self.verticalLayout_61.addLayout(self.horizontalLayout_21)
        self.verticalLayout_17.addWidget(self.groupBox_8)

        self.groupBox_9 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_9.setObjectName("groupBox_9")

        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.groupBox_9)
        self.verticalLayout_14.setObjectName("verticalLayout_14")

        self.horizontalLayout_22 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")

        spacerItem29 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum
        )
        self.horizontalLayout_22.addItem(spacerItem29)

        self.capture_radio = QtWidgets.QRadioButton(self.groupBox_9)
        self.capture_radio.setChecked(True)
        self.capture_radio.setObjectName("capture_radio")
        self.horizontalLayout_22.addWidget(self.capture_radio)

        spacerItem30 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum
        )
        self.horizontalLayout_22.addItem(spacerItem30)

        self.hosting_radio = QtWidgets.QRadioButton(self.groupBox_9)
        self.hosting_radio.setObjectName("hosting_radio")
        self.horizontalLayout_22.addWidget(self.hosting_radio)

        spacerItem31 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum
        )
        self.horizontalLayout_22.addItem(spacerItem31)

        self.verticalLayout_14.addLayout(self.horizontalLayout_22)
        self.verticalLayout_17.addWidget(self.groupBox_9)

        self.groupBox_10 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_10.setToolTip("")
        self.groupBox_10.setStatusTip("")
        self.groupBox_10.setWhatsThis("")
        self.groupBox_10.setObjectName("groupBox_10")

        self.horizontalLayout_17 = QtWidgets.QHBoxLayout(self.groupBox_10)
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")

        self.status_textbrowser_http = QtWidgets.QTextBrowser(self.groupBox_10)
        self.status_textbrowser_http.setObjectName("status_textbrowser_http")
        self.horizontalLayout_17.addWidget(self.status_textbrowser_http)

        self.verticalLayout_17.addWidget(self.groupBox_10)

        self.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.verticalLayout_13.setObjectName("verticalLayout_13")

        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")

        self.http_captured_credential = QtWidgets.QLabel(self.tab)
        self.http_captured_credential.setObjectName("http_captured_credential")
        self.verticalLayout_12.addWidget(self.http_captured_credential)

        self.http_captured_credential_2 = QtWidgets.QLabel(self.tab)
        self.http_captured_credential_2.setObjectName("http_captured_credential_2")
        self.verticalLayout_12.addWidget(self.http_captured_credential_2)

        self.verticalLayout_13.addLayout(self.verticalLayout_12)

        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")

        spacerItem32 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum
        )
        self.horizontalLayout_18.addItem(spacerItem32)

        self.http_start = QtWidgets.QPushButton(self.tab)
        self.http_start.setObjectName("http_start")
        self.horizontalLayout_18.addWidget(self.http_start)

        spacerItem33 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum
        )
        self.horizontalLayout_18.addItem(spacerItem33)

        self.http_stop = QtWidgets.QPushButton(self.tab)
        self.http_stop.setObjectName("http_stop")
        self.horizontalLayout_18.addWidget(self.http_stop)

        spacerItem34 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum
        )
        self.horizontalLayout_18.addItem(spacerItem34)

        self.verticalLayout_13.addLayout(self.horizontalLayout_18)
        self.verticalLayout_17.addLayout(self.verticalLayout_13)

        self.tabWidget.addTab(self.tab, "")

        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")

        self.verticalLayout_48 = QtWidgets.QVBoxLayout(self.tab_6)
        self.verticalLayout_48.setObjectName("verticalLayout_48")

        self.groupBox_19 = QtWidgets.QGroupBox(self.tab_6)
        self.groupBox_19.setObjectName("groupBox_19")

        self.verticalLayout_37 = QtWidgets.QVBoxLayout(self.groupBox_19)
        self.verticalLayout_37.setObjectName("verticalLayout_37")

        self.verticalLayout_26 = QtWidgets.QVBoxLayout()
        self.verticalLayout_26.setObjectName("verticalLayout_26")

        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")

        self.spawn_http_interface_combo = QtWidgets.QComboBox(self.groupBox_19)
        self.spawn_http_interface_combo.setObjectName("spawn_http_interface_combo")
        self.horizontalLayout_14.addWidget(self.spawn_http_interface_combo)

        spacerItem35 = QtWidgets.QSpacerItem(
            102, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum
        )
        self.horizontalLayout_14.addItem(spacerItem35)

        self.spawn_ip_combo = QtWidgets.QComboBox(self.groupBox_19)
        self.spawn_ip_combo.setObjectName("spawn_ip_combo")
        self.horizontalLayout_14.addWidget(self.spawn_ip_combo)

        self.verticalLayout_26.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_29 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_29.setObjectName("horizontalLayout_29")

        spacerItem36 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum
        )
        self.horizontalLayout_29.addItem(spacerItem36)

        self.ghost_vul_combo = QtWidgets.QRadioButton(self.groupBox_19)
        self.ghost_vul_combo.setChecked(True)
        self.ghost_vul_combo.setObjectName("ghost_vul_combo")
        self.horizontalLayout_29.addWidget(self.ghost_vul_combo)

        spacerItem37 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum
        )
        self.horizontalLayout_29.addItem(spacerItem37)

        self.custom_vul_combo = QtWidgets.QRadioButton(self.groupBox_19)
        self.custom_vul_combo.setObjectName("custom_vul_combo")
        self.horizontalLayout_29.addWidget(self.custom_vul_combo)

        spacerItem38 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum
        )
        self.horizontalLayout_29.addItem(spacerItem38)

        self.verticalLayout_26.addLayout(self.horizontalLayout_29)
        self.verticalLayout_37.addLayout(self.verticalLayout_26)
        self.verticalLayout_48.addWidget(self.groupBox_19)

        self.spawn_http_setting_box = QtWidgets.QGroupBox(self.tab_6)
        self.spawn_http_setting_box.setObjectName("spawn_http_setting_box")

        self.verticalLayout_38 = QtWidgets.QVBoxLayout(self.spawn_http_setting_box)
        self.verticalLayout_38.setObjectName("verticalLayout_38")

        self.horizontalLayout_30 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_30.setObjectName("horizontalLayout_30")

        self.cookies_checkbox = QtWidgets.QCheckBox(self.spawn_http_setting_box)
        self.cookies_checkbox.setChecked(True)
        self.cookies_checkbox.setObjectName("cookies_checkbox")
        self.horizontalLayout_30.addWidget(self.cookies_checkbox)

        self.force_download_checkbox = QtWidgets.QCheckBox(self.spawn_http_setting_box)
        self.force_download_checkbox.setObjectName("force_download_checkbox")
        self.horizontalLayout_30.addWidget(self.force_download_checkbox)

        self.respond_to_all_radio = QtWidgets.QRadioButton(self.spawn_http_setting_box)
        self.respond_to_all_radio.setChecked(True)
        self.respond_to_all_radio.setObjectName("respond_to_all_radio")
        self.horizontalLayout_30.addWidget(self.respond_to_all_radio)

        self.respond_windows_radio = QtWidgets.QRadioButton(self.spawn_http_setting_box)
        self.respond_windows_radio.setObjectName("respond_windows_radio")
        self.horizontalLayout_30.addWidget(self.respond_windows_radio)

        self.respond_linux_radio = QtWidgets.QRadioButton(self.spawn_http_setting_box)
        self.respond_linux_radio.setObjectName("respond_linux_radio")
        self.horizontalLayout_30.addWidget(self.respond_linux_radio)

        self.verticalLayout_38.addLayout(self.horizontalLayout_30)

        self.horizontalLayout_31 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_31.setObjectName("horizontalLayout_31")

        self.label_29 = QtWidgets.QLabel(self.spawn_http_setting_box)
        self.label_29.setObjectName("label_29")
        self.horizontalLayout_31.addWidget(self.label_29)

        self.ghost_trap_http_edit = QtWidgets.QLineEdit(self.spawn_http_setting_box)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Fixed,
            QtWidgets.QSizePolicy.Policy.Fixed,
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ghost_trap_http_edit.sizePolicy().hasHeightForWidth())
        self.ghost_trap_http_edit.setSizePolicy(sizePolicy)
        self.ghost_trap_http_edit.setMaximumSize(QtCore.QSize(45, 20))
        self.ghost_trap_http_edit.setObjectName("ghost_trap_http_edit")
        self.horizontalLayout_31.addWidget(self.ghost_trap_http_edit)

        spacerItem39 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum
        )
        self.horizontalLayout_31.addItem(spacerItem39)

        self.custom_page_label = QtWidgets.QLabel(self.spawn_http_setting_box)
        self.custom_page_label.setObjectName("custom_page_label")
        self.horizontalLayout_31.addWidget(self.custom_page_label)

        self.custom_page_label_2 = QtWidgets.QLineEdit(self.spawn_http_setting_box)
        self.custom_page_label_2.setObjectName("custom_page_label_2")
        self.horizontalLayout_31.addWidget(self.custom_page_label_2)

        self.custom_page_button = QtWidgets.QPushButton(self.spawn_http_setting_box)
        self.custom_page_button.setObjectName("custom_page_button")
        self.horizontalLayout_31.addWidget(self.custom_page_button)

        self.verticalLayout_38.addLayout(self.horizontalLayout_31)
        self.verticalLayout_48.addWidget(self.spawn_http_setting_box)

        self.horizontalLayout_46 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_46.setObjectName("horizontalLayout_46")

        spacerItem40 = QtWidgets.QSpacerItem(
            60, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum
        )
        self.horizontalLayout_46.addItem(spacerItem40)

        self.metasploit_payload_radio = QtWidgets.QRadioButton(self.tab_6)
        self.metasploit_payload_radio.setChecked(True)
        self.metasploit_payload_radio.setObjectName("metasploit_payload_radio")
        self.horizontalLayout_46.addWidget(self.metasploit_payload_radio)

        spacerItem41 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum
        )
        self.horizontalLayout_46.addItem(spacerItem41)

        self.custom_payload_radio = QtWidgets.QRadioButton(self.tab_6)
        self.custom_payload_radio.setObjectName("custom_payload_radio")
        self.horizontalLayout_46.addWidget(self.custom_payload_radio)

        spacerItem42 = QtWidgets.QSpacerItem(
            60, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum
        )
        self.horizontalLayout_46.addItem(spacerItem42)

        self.verticalLayout_48.addLayout(self.horizontalLayout_46)

        self.metasploit_settings_box = QtWidgets.QGroupBox(self.tab_6)
        self.metasploit_settings_box.setObjectName("metasploit_settings_box")

        self.horizontalLayout_76 = QtWidgets.QHBoxLayout(self.metasploit_settings_box)
        self.horizontalLayout_76.setObjectName("horizontalLayout_76")

        self.horizontalLayout_51 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_51.setObjectName("horizontalLayout_51")

        self.horizontalLayout_50 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_50.setObjectName("horizontalLayout_50")

        self.verticalLayout_42 = QtWidgets.QVBoxLayout()
        self.verticalLayout_42.setObjectName("verticalLayout_42")

        self.label_30 = QtWidgets.QLabel(self.metasploit_settings_box)
        self.label_30.setObjectName("label_30")
        self.verticalLayout_42.addWidget(self.label_30)

        self.label_32 = QtWidgets.QLabel(self.metasploit_settings_box)
        self.label_32.setObjectName("label_32")
        self.verticalLayout_42.addWidget(self.label_32)

        self.horizontalLayout_50.addLayout(self.verticalLayout_42)

        self.verticalLayout_41 = QtWidgets.QVBoxLayout()
        self.verticalLayout_41.setObjectName("verticalLayout_41")

        self.windows_payload_combo = QtWidgets.QComboBox(self.metasploit_settings_box)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Fixed,
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.windows_payload_combo.sizePolicy().hasHeightForWidth())
        self.windows_payload_combo.setSizePolicy(sizePolicy)
        self.windows_payload_combo.setObjectName("windows_payload_combo")
        self.verticalLayout_41.addWidget(self.windows_payload_combo)

        self.horizontalLayout_49 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_49.setObjectName("horizontalLayout_49")

        self.encode_combo = QtWidgets.QComboBox(self.metasploit_settings_box)
        self.encode_combo.setObjectName("encode_combo")
        self.horizontalLayout_49.addWidget(self.encode_combo)

        self.label_33 = QtWidgets.QLabel(self.metasploit_settings_box)
        self.label_33.setObjectName("label_33")
        self.horizontalLayout_49.addWidget(self.label_33)

        self.comboBox_2 = QtWidgets.QComboBox(self.metasploit_settings_box)
        self.comboBox_2.setObjectName("comboBox_2")
        self.horizontalLayout_49.addWidget(self.comboBox_2)

        self.verticalLayout_41.addLayout(self.horizontalLayout_49)
        self.horizontalLayout_50.addLayout(self.verticalLayout_41)

        self.horizontalLayout_51.addLayout(self.horizontalLayout_50)

        spacerItem43 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum
        )
        self.horizontalLayout_51.addItem(spacerItem43)

        self.horizontalLayout_48 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_48.setObjectName("horizontalLayout_48")

        self.verticalLayout_40 = QtWidgets.QVBoxLayout()
        self.verticalLayout_40.setObjectName("verticalLayout_40")

        self.label_31 = QtWidgets.QLabel(self.metasploit_settings_box)
        self.label_31.setObjectName("label_31")
        self.verticalLayout_40.addWidget(self.label_31)

        self.label_34 = QtWidgets.QLabel(self.metasploit_settings_box)
        self.label_34.setObjectName("label_34")
        self.verticalLayout_40.addWidget(self.label_34)

        self.horizontalLayout_48.addLayout(self.verticalLayout_40)

        self.verticalLayout_39 = QtWidgets.QVBoxLayout()
        self.verticalLayout_39.setObjectName("verticalLayout_39")

        self.linux_payload_combo = QtWidgets.QComboBox(self.metasploit_settings_box)
        self.linux_payload_combo.setObjectName("linux_payload_combo")
        self.verticalLayout_39.addWidget(self.linux_payload_combo)

        self.horizontalLayout_47 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_47.setObjectName("horizontalLayout_47")

        self.port_setting_edit = QtWidgets.QLineEdit(self.metasploit_settings_box)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Fixed,
            QtWidgets.QSizePolicy.Policy.Fixed,
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.port_setting_edit.sizePolicy().hasHeightForWidth())
        self.port_setting_edit.setSizePolicy(sizePolicy)
        self.port_setting_edit.setMaximumSize(QtCore.QSize(45, 20))
        self.port_setting_edit.setText("")
        self.port_setting_edit.setObjectName("port_setting_edit")
        self.horizontalLayout_47.addWidget(self.port_setting_edit)

        self.label_35 = QtWidgets.QLabel(self.metasploit_settings_box)
        self.label_35.setObjectName("label_35")
        self.horizontalLayout_47.addWidget(self.label_35)

        self.ip_address_edit = QtWidgets.QLineEdit(self.metasploit_settings_box)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Expanding,
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ip_address_edit.sizePolicy().hasHeightForWidth())
        self.ip_address_edit.setSizePolicy(sizePolicy)
        self.ip_address_edit.setObjectName("ip_address_edit")
        self.horizontalLayout_47.addWidget(self.ip_address_edit)

        self.verticalLayout_39.addLayout(self.horizontalLayout_47)
        self.horizontalLayout_48.addLayout(self.verticalLayout_39)
        self.horizontalLayout_51.addLayout(self.horizontalLayout_48)

        self.horizontalLayout_76.addLayout(self.horizontalLayout_51)
        self.verticalLayout_48.addWidget(self.metasploit_settings_box)

        self.custom_payload_box = QtWidgets.QGroupBox(self.tab_6)
        self.custom_payload_box.setObjectName("custom_payload_box")

        self.verticalLayout_47 = QtWidgets.QVBoxLayout(self.custom_payload_box)
        self.verticalLayout_47.setObjectName("verticalLayout_47")

        self.horizontalLayout_52 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_52.setObjectName("horizontalLayout_52")

        self.verticalLayout_45 = QtWidgets.QVBoxLayout()
        self.verticalLayout_45.setObjectName("verticalLayout_45")

        self.windows_exec_checkbox = QtWidgets.QCheckBox(self.custom_payload_box)
        self.windows_exec_checkbox.setObjectName("windows_exec_checkbox")
        self.verticalLayout_45.addWidget(self.windows_exec_checkbox)

        self.linux_exec_checkbox = QtWidgets.QCheckBox(self.custom_payload_box)
        self.linux_exec_checkbox.setObjectName("linux_exec_checkbox")
        self.verticalLayout_45.addWidget(self.linux_exec_checkbox)

        self.horizontalLayout_52.addLayout(self.verticalLayout_45)

        self.verticalLayout_44 = QtWidgets.QVBoxLayout()
        self.verticalLayout_44.setObjectName("verticalLayout_44")

        self.windows_exec_edit = QtWidgets.QLineEdit(self.custom_payload_box)
        self.windows_exec_edit.setObjectName("windows_exec_edit")
        self.verticalLayout_44.addWidget(self.windows_exec_edit)

        self.linux_exec_edit = QtWidgets.QLineEdit(self.custom_payload_box)
        self.linux_exec_edit.setObjectName("linux_exec_edit")
        self.verticalLayout_44.addWidget(self.linux_exec_edit)

        self.horizontalLayout_52.addLayout(self.verticalLayout_44)

        self.verticalLayout_46 = QtWidgets.QVBoxLayout()
        self.verticalLayout_46.setObjectName("verticalLayout_46")

        self.windows_exec_button = QtWidgets.QPushButton(self.custom_payload_box)
        self.windows_exec_button.setObjectName("windows_exec_button")
        self.verticalLayout_46.addWidget(self.windows_exec_button)

        self.linux_exec_button = QtWidgets.QPushButton(self.custom_payload_box)
        self.linux_exec_button.setObjectName("linux_exec_button")
        self.verticalLayout_46.addWidget(self.linux_exec_button)

        self.horizontalLayout_52.addLayout(self.verticalLayout_46)
        self.verticalLayout_47.addLayout(self.horizontalLayout_52)

        self.verticalLayout_48.addWidget(self.custom_payload_box)

        self.horizontalLayout_57 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_57.setObjectName("horizontalLayout_57")

        spacerItem44 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum
        )
        self.horizontalLayout_57.addItem(spacerItem44)

        self.horizontalLayout_53 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_53.setObjectName("horizontalLayout_53")

        self.initlaize_led = QtWidgets.QLabel(self.tab_6)
        self.initlaize_led.setText("")
        self.initlaize_led.setPixmap(QtGui.QPixmap(f"{cwd}/gui/images/red_led.png"))
        self.initlaize_led.setObjectName("initlaize_led")
        self.horizontalLayout_53.addWidget(self.initlaize_led)

        self.nitialize_label = QtWidgets.QLabel(self.tab_6)
        self.nitialize_label.setEnabled(False)
        self.nitialize_label.setObjectName("nitialize_label")
        self.horizontalLayout_53.addWidget(self.nitialize_label)

        self.horizontalLayout_57.addLayout(self.horizontalLayout_53)

        spacerItem45 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum
        )
        self.horizontalLayout_57.addItem(spacerItem45)

        self.horizontalLayout_54 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_54.setObjectName("horizontalLayout_54")

        self.payload_led = QtWidgets.QLabel(self.tab_6)
        self.payload_led.setText("")
        self.payload_led.setPixmap(QtGui.QPixmap(f"{cwd}/gui/images/red_led.png"))
        self.payload_led.setObjectName("payload_led")
        self.horizontalLayout_54.addWidget(self.payload_led)

        self.setting_payload_label = QtWidgets.QLabel(self.tab_6)
        self.setting_payload_label.setEnabled(False)
        self.setting_payload_label.setObjectName("setting_payload_label")
        self.horizontalLayout_54.addWidget(self.setting_payload_label)

        self.horizontalLayout_57.addLayout(self.horizontalLayout_54)

        spacerItem46 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum
        )
        self.horizontalLayout_57.addItem(spacerItem46)

        self.horizontalLayout_55 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_55.setObjectName("horizontalLayout_55")

        self.cache_led = QtWidgets.QLabel(self.tab_6)
        self.cache_led.setText("")
        self.cache_led.setPixmap(QtGui.QPixmap(f"{cwd}/gui/images/red_led.png"))
        self.cache_led.setObjectName("cache_led")
        self.horizontalLayout_55.addWidget(self.cache_led)

        self.create_cache_label = QtWidgets.QLabel(self.tab_6)
        self.create_cache_label.setEnabled(False)
        self.create_cache_label.setObjectName("create_cache_label")
        self.horizontalLayout_55.addWidget(self.create_cache_label)

        self.horizontalLayout_57.addLayout(self.horizontalLayout_55)

        spacerItem47 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum
        )
        self.horizontalLayout_57.addItem(spacerItem47)

        self.horizontalLayout_56 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_56.setObjectName("horizontalLayout_56")

        self.start_http_led = QtWidgets.QLabel(self.tab_6)
        self.start_http_led.setText("")
        self.start_http_led.setPixmap(QtGui.QPixmap(f"{cwd}/gui/images/red_led.png"))
        self.start_http_led.setObjectName("start_http_led")
        self.horizontalLayout_56.addWidget(self.start_http_led)

        self.http_start_label = QtWidgets.QLabel(self.tab_6)
        self.http_start_label.setEnabled(False)
        self.http_start_label.setObjectName("http_start_label")
        self.horizontalLayout_56.addWidget(self.http_start_label)

        self.horizontalLayout_57.addLayout(self.horizontalLayout_56)

        spacerItem48 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum
        )
        self.horizontalLayout_57.addItem(spacerItem48)

        self.verticalLayout_48.addLayout(self.horizontalLayout_57)

        self.groupBox_20 = QtWidgets.QGroupBox(self.tab_6)
        self.groupBox_20.setObjectName("groupBox_20")

        self.verticalLayout_49 = QtWidgets.QVBoxLayout(self.groupBox_20)
        self.verticalLayout_49.setObjectName("verticalLayout_49")

        self.ghost_spawn_browser = QtWidgets.QTextBrowser(self.groupBox_20)
        self.ghost_spawn_browser.setObjectName("ghost_spawn_browser")
        self.verticalLayout_49.addWidget(self.ghost_spawn_browser)

        self.verticalLayout_48.addWidget(self.groupBox_20)

        self.horizontalLayout_58 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_58.setObjectName("horizontalLayout_58")

        spacerItem49 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum
        )
        self.horizontalLayout_58.addItem(spacerItem49)

        self.ghost_spawn_start = QtWidgets.QPushButton(self.tab_6)
        self.ghost_spawn_start.setObjectName("ghost_spawn_start")
        self.horizontalLayout_58.addWidget(self.ghost_spawn_start)

        spacerItem50 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum
        )
        self.horizontalLayout_58.addItem(spacerItem50)

        self.ghost_spawn_stop = QtWidgets.QPushButton(self.tab_6)
        self.ghost_spawn_stop.setObjectName("ghost_spawn_stop")
        self.horizontalLayout_58.addWidget(self.ghost_spawn_stop)

        spacerItem51 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum
        )
        self.horizontalLayout_58.addItem(spacerItem51)

        self.verticalLayout_48.addLayout(self.horizontalLayout_58)
        self.tabWidget.addTab(self.tab_6, "")

        self.tab_7 = QtWidgets.QWidget()
        self.tab_7.setObjectName("tab_7")

        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.tab_7)
        self.verticalLayout_10.setObjectName("verticalLayout_10")

        spacerItem52 = QtWidgets.QSpacerItem(
            20, 8, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed
        )
        self.verticalLayout_10.addItem(spacerItem52)

        self.horizontalLayout_77 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_77.setObjectName("horizontalLayout_77")

        self.verticalLayout_57 = QtWidgets.QVBoxLayout()
        self.verticalLayout_57.setObjectName("verticalLayout_57")

        self.verticalLayout_58 = QtWidgets.QVBoxLayout()
        self.verticalLayout_58.setObjectName("verticalLayout_58")

        self.label_44 = QtWidgets.QLabel(self.tab_7)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label_44.setFont(font)
        self.label_44.setObjectName("label_44")
        self.verticalLayout_58.addWidget(self.label_44)

        self.label_45 = QtWidgets.QLabel(self.tab_7)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label_45.setFont(font)
        self.label_45.setObjectName("label_45")
        self.verticalLayout_58.addWidget(self.label_45)

        self.verticalLayout_57.addLayout(self.verticalLayout_58)

        spacerItem53 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum
        )
        self.verticalLayout_57.addItem(spacerItem53)

        self.horizontalLayout_78 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_78.setObjectName("horizontalLayout_78")

        self.horizontalLayout_79 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_79.setObjectName("horizontalLayout_79")

        spacerItem54 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum
        )
        self.horizontalLayout_79.addItem(spacerItem54)

        self.verticalLayout_59 = QtWidgets.QVBoxLayout()
        self.verticalLayout_59.setObjectName("verticalLayout_59")

        self.combo_interface_2 = QtWidgets.QComboBox(self.tab_7)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Ignored,
            QtWidgets.QSizePolicy.Policy.Ignored,
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.combo_interface_2.sizePolicy().hasHeightForWidth())
        self.combo_interface_2.setSizePolicy(sizePolicy)

        font = QtGui.QFont()
        font.setPointSize(7)
        self.combo_interface_2.setFont(font)
        self.combo_interface_2.setObjectName("combo_interface_2")
        self.verticalLayout_59.addWidget(self.combo_interface_2)

        spacerItem55 = QtWidgets.QSpacerItem(
            177, 20,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum
        )
        self.verticalLayout_59.addItem(spacerItem55)
        self.horizontalLayout_79.addLayout(self.verticalLayout_59)

        self.verticalLayout_60 = QtWidgets.QVBoxLayout()
        self.verticalLayout_60.setObjectName("verticalLayout_60")

        self.refresh_button_3 = QtWidgets.QPushButton(self.tab_7)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Ignored,
            QtWidgets.QSizePolicy.Policy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.refresh_button_3.sizePolicy().hasHeightForWidth())
        self.refresh_button_3.setSizePolicy(sizePolicy)

        font = QtGui.QFont()
        font.setPointSize(7)
        self.refresh_button_3.setFont(font)

        icon1 = QtGui.QIcon()
        icon1.addPixmap(
            QtGui.QPixmap("G:/PNG-Refresh.png-256x256.png"),
            QtGui.QIcon.Mode.Normal,
            QtGui.QIcon.State.Off
        )
        self.refresh_button_3.setIcon(icon1)
        self.refresh_button_3.setIconSize(QtCore.QSize(22, 23))
        self.refresh_button_3.setObjectName("refresh_button_3")
        self.verticalLayout_60.addWidget(self.refresh_button_3)

        spacerItem56 = QtWidgets.QSpacerItem(
            82, 20,
            QtWidgets.QSizePolicy.Policy.Fixed,
            QtWidgets.QSizePolicy.Policy.Minimum
        )
        self.verticalLayout_60.addItem(spacerItem56)
        self.horizontalLayout_79.addLayout(self.verticalLayout_60)

        spacerItem57 = QtWidgets.QSpacerItem(
            40, 20,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum
        )
        self.horizontalLayout_79.addItem(spacerItem57)

        self.horizontalLayout_78.addLayout(self.horizontalLayout_79)
        self.verticalLayout_57.addLayout(self.horizontalLayout_78)
        self.horizontalLayout_77.addLayout(self.verticalLayout_57)
        self.verticalLayout_10.addLayout(self.horizontalLayout_77)

        self.horizontalLayout_80 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_80.setObjectName("horizontalLayout_80")

        self.verticalLayout_62 = QtWidgets.QVBoxLayout()
        self.verticalLayout_62.setObjectName("verticalLayout_62")
        self.horizontalLayout_80.addLayout(self.verticalLayout_62)
        self.verticalLayout_10.addLayout(self.horizontalLayout_80)

        self.horizontalLayout_85 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_85.setObjectName("horizontalLayout_85")

        spacerItem58 = QtWidgets.QSpacerItem(
            40, 20,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum
        )
        self.horizontalLayout_85.addItem(spacerItem58)

        self.horizontalLayout_86 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_86.setObjectName("horizontalLayout_86")

        self.horizontalLayout_87 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_87.setObjectName("horizontalLayout_87")

        self.horizontalLayout_88 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_88.setObjectName("horizontalLayout_88")

        self.monitor_interface_led_2 = QtWidgets.QLabel(self.tab_7)
        self.monitor_interface_led_2.setText("")
        self.monitor_interface_led_2.setPixmap(QtGui.QPixmap(f"{cwd}/gui/images/red_led.png"))
        self.monitor_interface_led_2.setObjectName("monitor_interface_led_2")
        self.horizontalLayout_88.addWidget(self.monitor_interface_led_2)

        self.monitor_interface_label_2 = QtWidgets.QLabel(self.tab_7)
        self.monitor_interface_label_2.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.monitor_interface_label_2.setFont(font)
        self.monitor_interface_label_2.setObjectName("monitor_interface_label_2")
        self.horizontalLayout_88.addWidget(self.monitor_interface_label_2)

        self.horizontalLayout_87.addLayout(self.horizontalLayout_88)
        self.horizontalLayout_86.addLayout(self.horizontalLayout_87)

        self.horizontalLayout_89 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_89.setObjectName("horizontalLayout_89")

        self.horizontalLayout_90 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_90.setObjectName("horizontalLayout_90")

        spacerItem59 = QtWidgets.QSpacerItem(
            40, 20,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum
        )
        self.horizontalLayout_90.addItem(spacerItem59)

        self.horizontalLayout_91 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_91.setObjectName("horizontalLayout_91")

        self.sniffing_status_led_2 = QtWidgets.QLabel(self.tab_7)
        self.sniffing_status_led_2.setText("")
        self.sniffing_status_led_2.setPixmap(QtGui.QPixmap(f"{cwd}/gui/images/red_led.png"))
        self.sniffing_status_led_2.setObjectName("sniffing_status_led_2")
        self.horizontalLayout_91.addWidget(self.sniffing_status_led_2)

        self.sniffing_status_label_2 = QtWidgets.QLabel(self.tab_7)
        self.sniffing_status_label_2.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.sniffing_status_label_2.setFont(font)
        self.sniffing_status_label_2.setObjectName("sniffing_status_label_2")
        self.horizontalLayout_91.addWidget(self.sniffing_status_label_2)

        self.horizontalLayout_90.addLayout(self.horizontalLayout_91)
        self.horizontalLayout_89.addLayout(self.horizontalLayout_90)

        self.horizontalLayout_92 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_92.setObjectName("horizontalLayout_92")

        spacerItem60 = QtWidgets.QSpacerItem(
            40, 20,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum
        )
        self.horizontalLayout_92.addItem(spacerItem60)

        self.horizontalLayout_93 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_93.setObjectName("horizontalLayout_93")

        self.cookie_detection_led_2 = QtWidgets.QLabel(self.tab_7)
        self.cookie_detection_led_2.setText("")
        self.cookie_detection_led_2.setPixmap(QtGui.QPixmap(f"{cwd}/gui/images/red_led.png"))
        self.cookie_detection_led_2.setObjectName("cookie_detection_led_2")
        self.horizontalLayout_93.addWidget(self.cookie_detection_led_2)

        self.cookie_detection_label_2 = QtWidgets.QLabel(self.tab_7)
        self.cookie_detection_label_2.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.cookie_detection_label_2.setFont(font)
        self.cookie_detection_label_2.setObjectName("cookie_detection_label_2")
        self.horizontalLayout_93.addWidget(self.cookie_detection_label_2)

        self.horizontalLayout_92.addLayout(self.horizontalLayout_93)
        self.horizontalLayout_89.addLayout(self.horizontalLayout_92)

        self.horizontalLayout_86.addLayout(self.horizontalLayout_89)
        self.horizontalLayout_85.addLayout(self.horizontalLayout_86)

        spacerItem61 = QtWidgets.QSpacerItem(
            40, 20,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum
        )
        self.horizontalLayout_85.addItem(spacerItem61)

        self.verticalLayout_10.addLayout(self.horizontalLayout_85)

        self.mitm_activated_label = QtWidgets.QLabel(self.tab_7)
        self.mitm_activated_label.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.mitm_activated_label.setFont(font)
        self.mitm_activated_label.setObjectName("mitm_activated_label")
        self.verticalLayout_10.addWidget(self.mitm_activated_label)

        self.horizontalLayout_84 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_84.setObjectName("horizontalLayout_84")

        spacerItem62 = QtWidgets.QSpacerItem(
            40, 20,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum
        )
        self.horizontalLayout_84.addItem(spacerItem62)

        self.ethernet_mode_radio_2 = QtWidgets.QRadioButton(self.tab_7)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.ethernet_mode_radio_2.setFont(font)
        self.ethernet_mode_radio_2.setChecked(True)
        self.ethernet_mode_radio_2.setObjectName("ethernet_mode_radio_2")
        self.horizontalLayout_84.addWidget(self.ethernet_mode_radio_2)

        spacerItem63 = QtWidgets.QSpacerItem(
            40, 20,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum
        )
        self.horizontalLayout_84.addItem(spacerItem63)

        self.passive_mode_radio_2 = QtWidgets.QRadioButton(self.tab_7)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.passive_mode_radio_2.setFont(font)
        self.passive_mode_radio_2.setObjectName("passive_mode_radio_2")
        self.horizontalLayout_84.addWidget(self.passive_mode_radio_2)

        spacerItem64 = QtWidgets.QSpacerItem(
            40, 20,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum
        )
        self.horizontalLayout_84.addItem(spacerItem64)

        self.verticalLayout_10.addLayout(self.horizontalLayout_84)

        self.groupBox_22 = QtWidgets.QGroupBox(self.tab_7)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_22.sizePolicy().hasHeightForWidth())
        self.groupBox_22.setSizePolicy(sizePolicy)

        font = QtGui.QFont()
        font.setPointSize(7)
        self.groupBox_22.setFont(font)
        self.groupBox_22.setTitle("")
        self.groupBox_22.setObjectName("groupBox_22")

        self.verticalLayout_63 = QtWidgets.QVBoxLayout(self.groupBox_22)
        self.verticalLayout_63.setObjectName("verticalLayout_63")

        self.horizontalLayout_81 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_81.setObjectName("horizontalLayout_81")

        self.label_46 = QtWidgets.QLabel(self.groupBox_22)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label_46.setFont(font)
        self.label_46.setObjectName("label_46")
        self.horizontalLayout_81.addWidget(self.label_46)

        self.horizontalLayout_82 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_82.setObjectName("horizontalLayout_82")

        self.wep_key_edit_2 = QtWidgets.QLineEdit(self.groupBox_22)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.wep_key_edit_2.setFont(font)
        self.wep_key_edit_2.setObjectName("wep_key_edit_2")
        self.horizontalLayout_82.addWidget(self.wep_key_edit_2)

        self.horizontalLayout_81.addLayout(self.horizontalLayout_82)
        self.verticalLayout_63.addLayout(self.horizontalLayout_81)

        spacerItem65 = QtWidgets.QSpacerItem(
            20, 6,
            QtWidgets.QSizePolicy.Policy.Minimum,
            QtWidgets.QSizePolicy.Policy.Fixed
        )
        self.verticalLayout_63.addItem(spacerItem65)
        self.verticalLayout_10.addWidget(self.groupBox_22)

        self.treeWidget = QtWidgets.QTreeWidget(self.tab_7)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.treeWidget.sizePolicy().hasHeightForWidth())
        self.treeWidget.setSizePolicy(sizePolicy)
        self.treeWidget.setObjectName("treeWidget")

        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        font = QtGui.QFont()
        font.setPointSize(10)

        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(
            QtGui.QPixmap("G:/SAVIOUR/Programming/Python/My Projects/Fern-Wifi-Cracker/Documents/Projects/SVN Projects/Fern-Wifi-Cracker/resources/green_led.png"),
            QtGui.QIcon.Mode.Normal,
            QtGui.QIcon.State.Off
        )
        item_1.setIcon(0, icon2)

        item_2 = QtWidgets.QTreeWidgetItem(item_1)

        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1.setIcon(0, icon2)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)

        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        font = QtGui.QFont()
        font.setPointSize(10)

        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1.setIcon(0, icon2)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)

        self.verticalLayout_10.addWidget(self.treeWidget)

        self.cookies_captured_label_2 = QtWidgets.QLabel(self.tab_7)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.cookies_captured_label_2.setFont(font)
        self.cookies_captured_label_2.setObjectName("cookies_captured_label_2")
        self.verticalLayout_10.addWidget(self.cookies_captured_label_2)

        self.horizontalLayout_83 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_83.setObjectName("horizontalLayout_83")

        self.start_sniffing_button_2 = QtWidgets.QPushButton(self.tab_7)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Minimum,
            QtWidgets.QSizePolicy.Policy.Ignored
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.start_sniffing_button_2.sizePolicy().hasHeightForWidth())
        self.start_sniffing_button_2.setSizePolicy(sizePolicy)

        font = QtGui.QFont()
        font.setPointSize(7)
        self.start_sniffing_button_2.setFont(font)
        self.start_sniffing_button_2.setObjectName("start_sniffing_button_2")
        self.horizontalLayout_83.addWidget(self.start_sniffing_button_2)

        self.verticalLayout_10.addLayout(self.horizontalLayout_83)

        self.horizontalLayout_94 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_94.setObjectName("horizontalLayout_94")

        spacerItem66 = QtWidgets.QSpacerItem(
            40, 20,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum
        )
        self.horizontalLayout_94.addItem(spacerItem66)

        self.start_sniffing_button_3 = QtWidgets.QPushButton(self.tab_7)
        self.start_sniffing_button_3.setObjectName("start_sniffing_button_3")
        self.horizontalLayout_94.addWidget(self.start_sniffing_button_3)

        spacerItem67 = QtWidgets.QSpacerItem(
            40, 20,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum
        )
        self.horizontalLayout_94.addItem(spacerItem67)

        self.stop_sniffing_button_3 = QtWidgets.QPushButton(self.tab_7)
        self.stop_sniffing_button_3.setObjectName("stop_sniffing_button_3")
        self.horizontalLayout_94.addWidget(self.stop_sniffing_button_3)

        spacerItem68 = QtWidgets.QSpacerItem(
            40, 20,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum
        )
        self.horizontalLayout_94.addItem(spacerItem68)

        self.verticalLayout_10.addLayout(self.horizontalLayout_94)

        self.tabWidget.addTab(self.tab_7, "")

        self.tab_8 = QtWidgets.QWidget()
        self.tab_8.setObjectName("tab_8")

        self.verticalLayout_51 = QtWidgets.QVBoxLayout(self.tab_8)
        self.verticalLayout_51.setObjectName("verticalLayout_51")

        spacerItem69 = QtWidgets.QSpacerItem(
            20, 8,
            QtWidgets.QSizePolicy.Policy.Minimum,
            QtWidgets.QSizePolicy.Policy.Fixed
        )
        self.verticalLayout_51.addItem(spacerItem69)

        self.label_39 = QtWidgets.QLabel(self.tab_8)
        self.label_39.setObjectName("label_39")
        self.verticalLayout_51.addWidget(self.label_39)

        spacerItem70 = QtWidgets.QSpacerItem(
            20, 10,
            QtWidgets.QSizePolicy.Policy.Minimum,
            QtWidgets.QSizePolicy.Policy.Fixed
        )
        self.verticalLayout_51.addItem(spacerItem70)

        self.horizontalLayout_95 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_95.setObjectName("horizontalLayout_95")

        self.horizontalLayout_96 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_96.setObjectName("horizontalLayout_96")

        spacerItem71 = QtWidgets.QSpacerItem(
            40, 20,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum
        )
        self.horizontalLayout_96.addItem(spacerItem71)

        self.verticalLayout_64 = QtWidgets.QVBoxLayout()
        self.verticalLayout_64.setObjectName("verticalLayout_64")

        self.combo_interface_3 = QtWidgets.QComboBox(self.tab_8)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Ignored,
            QtWidgets.QSizePolicy.Policy.Ignored
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.combo_interface_3.sizePolicy().hasHeightForWidth())
        self.combo_interface_3.setSizePolicy(sizePolicy)

        font = QtGui.QFont()
        font.setPointSize(7)
        self.combo_interface_3.setFont(font)
        self.combo_interface_3.setObjectName("combo_interface_3")
        self.verticalLayout_64.addWidget(self.combo_interface_3)

        spacerItem72 = QtWidgets.QSpacerItem(
            177, 20,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum
        )
        self.verticalLayout_64.addItem(spacerItem72)
        self.horizontalLayout_96.addLayout(self.verticalLayout_64)

        self.verticalLayout_65 = QtWidgets.QVBoxLayout()
        self.verticalLayout_65.setObjectName("verticalLayout_65")

        self.refresh_button_4 = QtWidgets.QPushButton(self.tab_8)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Ignored,
            QtWidgets.QSizePolicy.Policy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.refresh_button_4.sizePolicy().hasHeightForWidth())
        self.refresh_button_4.setSizePolicy(sizePolicy)

        font = QtGui.QFont()
        font.setPointSize(7)
        self.refresh_button_4.setFont(font)
        self.refresh_button_4.setIcon(icon1)
        self.refresh_button_4.setIconSize(QtCore.QSize(22, 23))
        self.refresh_button_4.setObjectName("refresh_button_4")
        self.verticalLayout_65.addWidget(self.refresh_button_4)

        spacerItem73 = QtWidgets.QSpacerItem(
            82, 20,
            QtWidgets.QSizePolicy.Policy.Fixed,
            QtWidgets.QSizePolicy.Policy.Minimum
        )
        self.verticalLayout_65.addItem(spacerItem73)

        self.horizontalLayout_96.addLayout(self.verticalLayout_65)

        spacerItem74 = QtWidgets.QSpacerItem(
            40, 20,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum
        )
        self.horizontalLayout_96.addItem(spacerItem74)

        self.horizontalLayout_95.addLayout(self.horizontalLayout_96)
        self.verticalLayout_51.addLayout(self.horizontalLayout_95)

        self.groupBox_23 = QtWidgets.QGroupBox(self.tab_8)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_23.sizePolicy().hasHeightForWidth())
        self.groupBox_23.setSizePolicy(sizePolicy)

        font = QtGui.QFont()
        font.setPointSize(7)
        self.groupBox_23.setFont(font)
        self.groupBox_23.setObjectName("groupBox_23")

        self.verticalLayout_67 = QtWidgets.QVBoxLayout(self.groupBox_23)
        self.verticalLayout_67.setObjectName("verticalLayout_67")

        self.horizontalLayout_98 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_98.setObjectName("horizontalLayout_98")

        self.label_47 = QtWidgets.QLabel(self.groupBox_23)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label_47.setFont(font)
        self.label_47.setObjectName("label_47")
        self.horizontalLayout_98.addWidget(self.label_47)

        self.horizontalLayout_99 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_99.setObjectName("horizontalLayout_99")

        self.wep_key_edit_3 = QtWidgets.QLineEdit(self.groupBox_23)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.wep_key_edit_3.setFont(font)
        self.wep_key_edit_3.setObjectName("wep_key_edit_3")
        self.horizontalLayout_99.addWidget(self.wep_key_edit_3)

        self.horizontalLayout_98.addLayout(self.horizontalLayout_99)
        self.verticalLayout_67.addLayout(self.horizontalLayout_98)

        self.verticalLayout_51.addWidget(self.groupBox_23)

        spacerItem75 = QtWidgets.QSpacerItem(
            20, 5,
            QtWidgets.QSizePolicy.Policy.Minimum,
            QtWidgets.QSizePolicy.Policy.Fixed
        )
        self.verticalLayout_51.addItem(spacerItem75)

        self.groupBox_24 = QtWidgets.QGroupBox(self.tab_8)
        self.groupBox_24.setObjectName("groupBox_24")

        self.horizontalLayout_60 = QtWidgets.QHBoxLayout(self.groupBox_24)
        self.horizontalLayout_60.setObjectName("horizontalLayout_60")

        self.horizontalLayout_59 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_59.setObjectName("horizontalLayout_59")

        spacerItem76 = QtWidgets.QSpacerItem(
            40, 20,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum
        )
        self.horizontalLayout_59.addItem(spacerItem76)

        self.poison_one_way_combo = QtWidgets.QRadioButton(self.groupBox_24)
        self.poison_one_way_combo.setChecked(True)
        self.poison_one_way_combo.setObjectName("poison_one_way_combo")
        self.horizontalLayout_59.addWidget(self.poison_one_way_combo)

        spacerItem77 = QtWidgets.QSpacerItem(
            40, 20,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum
        )
        self.horizontalLayout_59.addItem(spacerItem77)

        self.route_traffic_combo = QtWidgets.QRadioButton(self.groupBox_24)
        self.route_traffic_combo.setObjectName("route_traffic_combo")
        self.horizontalLayout_59.addWidget(self.route_traffic_combo)

        spacerItem78 = QtWidgets.QSpacerItem(
            40, 20,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum
        )
        self.horizontalLayout_59.addItem(spacerItem78)

        self.horizontalLayout_60.addLayout(self.horizontalLayout_59)
        self.verticalLayout_51.addWidget(self.groupBox_24)

        self.groupBox_21 = QtWidgets.QGroupBox(self.tab_8)
        self.groupBox_21.setObjectName("groupBox_21")

        self.verticalLayout_50 = QtWidgets.QVBoxLayout(self.groupBox_21)
        self.verticalLayout_50.setObjectName("verticalLayout_50")

        self.arp_poison_browser = QtWidgets.QTextBrowser(self.groupBox_21)
        self.arp_poison_browser.setObjectName("arp_poison_browser")
        self.verticalLayout_50.addWidget(self.arp_poison_browser)

        self.verticalLayout_51.addWidget(self.groupBox_21)

        self.label_40 = QtWidgets.QLabel(self.tab_8)
        self.label_40.setObjectName("label_40")
        self.verticalLayout_51.addWidget(self.label_40)

        self.horizontalLayout_97 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_97.setObjectName("horizontalLayout_97")

        spacerItem79 = QtWidgets.QSpacerItem(
            40, 20,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum
        )
        self.horizontalLayout_97.addItem(spacerItem79)

        self.start_arp_poison = QtWidgets.QPushButton(self.tab_8)
        self.start_arp_poison.setObjectName("start_arp_poison")
        self.horizontalLayout_97.addWidget(self.start_arp_poison)

        spacerItem80 = QtWidgets.QSpacerItem(
            40, 20,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum
        )
        self.horizontalLayout_97.addItem(spacerItem80)

        self.stop_arp_poison = QtWidgets.QPushButton(self.tab_8)
        self.stop_arp_poison.setObjectName("stop_arp_poison")
        self.horizontalLayout_97.addWidget(self.stop_arp_poison)

        spacerItem81 = QtWidgets.QSpacerItem(
            40, 20,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum
        )
        self.horizontalLayout_97.addItem(spacerItem81)

        self.verticalLayout_51.addLayout(self.horizontalLayout_97)

        self.tabWidget.addTab(self.tab_8, "")

        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")

        self.horizontalLayout_28 = QtWidgets.QHBoxLayout(self.tab_3)
        self.horizontalLayout_28.setObjectName("horizontalLayout_28")

        self.verticalLayout_22 = QtWidgets.QVBoxLayout()
        self.verticalLayout_22.setObjectName("verticalLayout_22")

        self.credential_table = QtWidgets.QTableWidget(self.tab_3)
        self.credential_table.setObjectName("credential_table")
        self.credential_table.setColumnCount(3)
        self.credential_table.setRowCount(0)

        item = QtWidgets.QTableWidgetItem()
        self.credential_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.credential_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.credential_table.setHorizontalHeaderItem(2, item)

        self.verticalLayout_22.addWidget(self.credential_table)

        spacerItem82 = QtWidgets.QSpacerItem(
            15, 6,
            QtWidgets.QSizePolicy.Policy.Minimum,
            QtWidgets.QSizePolicy.Policy.Fixed
        )
        self.verticalLayout_22.addItem(spacerItem82)

        self.horizontalLayout_26 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_26.setObjectName("horizontalLayout_26")

        spacerItem83 = QtWidgets.QSpacerItem(
            40, 20,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum
        )
        self.horizontalLayout_26.addItem(spacerItem83)

        self.savechanges_button = QtWidgets.QPushButton(self.tab_3)
        self.savechanges_button.setObjectName("savechanges_button")
        self.horizontalLayout_26.addWidget(self.savechanges_button)

        spacerItem84 = QtWidgets.QSpacerItem(
            40, 20,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum
        )
        self.horizontalLayout_26.addItem(spacerItem84)

        self.insert_button = QtWidgets.QPushButton(self.tab_3)
        self.insert_button.setObjectName("insert_button")
        self.horizontalLayout_26.addWidget(self.insert_button)

        spacerItem85 = QtWidgets.QSpacerItem(
            40, 20,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum
        )
        self.horizontalLayout_26.addItem(spacerItem85)

        self.delete_button = QtWidgets.QPushButton(self.tab_3)
        self.delete_button.setObjectName("delete_button")
        self.horizontalLayout_26.addWidget(self.delete_button)

        spacerItem86 = QtWidgets.QSpacerItem(
            40, 20,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum
        )
        self.horizontalLayout_26.addItem(spacerItem86)

        self.verticalLayout_22.addLayout(self.horizontalLayout_26)
        self.horizontalLayout_28.addLayout(self.verticalLayout_22)

        self.tabWidget.addTab(self.tab_3, "")

        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")

        self.horizontalLayout_27 = QtWidgets.QHBoxLayout(self.tab_4)
        self.horizontalLayout_27.setObjectName("horizontalLayout_27")

        self.verticalLayout_21 = QtWidgets.QVBoxLayout()
        self.verticalLayout_21.setObjectName("verticalLayout_21")

        self.groupBox_13 = QtWidgets.QGroupBox(self.tab_4)
        self.groupBox_13.setObjectName("groupBox_13")

        self.horizontalLayout_23 = QtWidgets.QHBoxLayout(self.groupBox_13)
        self.horizontalLayout_23.setObjectName("horizontalLayout_23")

        self.verticalLayout_20 = QtWidgets.QVBoxLayout()
        self.verticalLayout_20.setObjectName("verticalLayout_20")

        self.label_17 = QtWidgets.QLabel(self.groupBox_13)
        self.label_17.setObjectName("label_17")
        self.verticalLayout_20.addWidget(self.label_17)

        spacerItem87 = QtWidgets.QSpacerItem(
            23, 0,
            QtWidgets.QSizePolicy.Policy.Minimum,
            QtWidgets.QSizePolicy.Policy.Fixed
        )
        self.verticalLayout_20.addItem(spacerItem87)

        self.label_18 = QtWidgets.QLabel(self.groupBox_13)
        self.label_18.setObjectName("label_18")
        self.verticalLayout_20.addWidget(self.label_18)

        spacerItem88 = QtWidgets.QSpacerItem(
            20, 0,
            QtWidgets.QSizePolicy.Policy.Minimum,
            QtWidgets.QSizePolicy.Policy.Fixed
        )
        self.verticalLayout_20.addItem(spacerItem88)

        self.label_20 = QtWidgets.QLabel(self.groupBox_13)
        self.label_20.setObjectName("label_20")
        self.verticalLayout_20.addWidget(self.label_20)

        spacerItem89 = QtWidgets.QSpacerItem(
            20, 0,
            QtWidgets.QSizePolicy.Policy.Minimum,
            QtWidgets.QSizePolicy.Policy.Fixed
        )
        self.verticalLayout_20.addItem(spacerItem89)

        self.label_19 = QtWidgets.QLabel(self.groupBox_13)
        self.label_19.setObjectName("label_19")
        self.verticalLayout_20.addWidget(self.label_19)

        self.horizontalLayout_23.addLayout(self.verticalLayout_20)
        self.verticalLayout_21.addWidget(self.groupBox_13)

        self.groupBox_11 = QtWidgets.QGroupBox(self.tab_4)
        self.groupBox_11.setObjectName("groupBox_11")

        self.horizontalLayout_24 = QtWidgets.QHBoxLayout(self.groupBox_11)
        self.horizontalLayout_24.setObjectName("horizontalLayout_24")

        self.verticalLayout_18 = QtWidgets.QVBoxLayout()
        self.verticalLayout_18.setObjectName("verticalLayout_18")

        self.label_21 = QtWidgets.QLabel(self.groupBox_11)
        self.label_21.setObjectName("label_21")
        self.verticalLayout_18.addWidget(self.label_21)

        self.label_22 = QtWidgets.QLabel(self.groupBox_11)
        self.label_22.setObjectName("label_22")
        self.verticalLayout_18.addWidget(self.label_22)

        self.label_23 = QtWidgets.QLabel(self.groupBox_11)
        self.label_23.setObjectName("label_23")
        self.verticalLayout_18.addWidget(self.label_23)

        spacerItem90 = QtWidgets.QSpacerItem(
            20, 0,
            QtWidgets.QSizePolicy.Policy.Minimum,
            QtWidgets.QSizePolicy.Policy.Fixed
        )
        self.verticalLayout_18.addItem(spacerItem90)

        spacerItem91 = QtWidgets.QSpacerItem(
            20, 0,
            QtWidgets.QSizePolicy.Policy.Minimum,
            QtWidgets.QSizePolicy.Policy.Fixed
        )
        self.verticalLayout_18.addItem(spacerItem91)

        self.horizontalLayout_24.addLayout(self.verticalLayout_18)
        self.verticalLayout_21.addWidget(self.groupBox_11)

        self.groupBox_12 = QtWidgets.QGroupBox(self.tab_4)
        self.groupBox_12.setObjectName("groupBox_12")

        self.horizontalLayout_25 = QtWidgets.QHBoxLayout(self.groupBox_12)
        self.horizontalLayout_25.setObjectName("horizontalLayout_25")

        self.verticalLayout_19 = QtWidgets.QVBoxLayout()
        self.verticalLayout_19.setObjectName("verticalLayout_19")

        spacerItem92 = QtWidgets.QSpacerItem(
            20, 0,
            QtWidgets.QSizePolicy.Policy.Minimum,
            QtWidgets.QSizePolicy.Policy.Fixed
        )
        self.verticalLayout_19.addItem(spacerItem92)

        self.horizontalLayout_44 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_44.setObjectName("horizontalLayout_44")

        self.label_15 = QtWidgets.QLabel(self.groupBox_12)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_44.addWidget(self.label_15)

        spacerItem93 = QtWidgets.QSpacerItem(
            40, 20,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum
        )
        self.horizontalLayout_44.addItem(spacerItem93)

        self.label_26 = QtWidgets.QLabel(self.groupBox_12)
        self.label_26.setText("")
        self.label_26.setObjectName("label_26")
        self.horizontalLayout_44.addWidget(self.label_26)

        spacerItem94 = QtWidgets.QSpacerItem(
            300, 20,
            QtWidgets.QSizePolicy.Policy.Fixed,
            QtWidgets.QSizePolicy.Policy.Minimum
        )
        self.horizontalLayout_44.addItem(spacerItem94)

        self.verticalLayout_19.addLayout(self.horizontalLayout_44)

        self.horizontalLayout_45 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_45.setObjectName("horizontalLayout_45")

        self.label_27 = QtWidgets.QLabel(self.groupBox_12)
        self.label_27.setObjectName("label_27")
        self.horizontalLayout_45.addWidget(self.label_27)

        spacerItem95 = QtWidgets.QSpacerItem(
            40, 20,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum
        )
        self.horizontalLayout_45.addItem(spacerItem95)

        self.label_28 = QtWidgets.QLabel(self.groupBox_12)
        self.label_28.setText("")
        self.label_28.setObjectName("label_28")
        self.horizontalLayout_45.addWidget(self.label_28)

        spacerItem96 = QtWidgets.QSpacerItem(
            300, 20,
            QtWidgets.QSizePolicy.Policy.Fixed,
            QtWidgets.QSizePolicy.Policy.Minimum
        )
        self.horizontalLayout_45.addItem(spacerItem96)

        self.verticalLayout_19.addLayout(self.horizontalLayout_45)

        spacerItem97 = QtWidgets.QSpacerItem(
            20, 10,
            QtWidgets.QSizePolicy.Policy.Minimum,
            QtWidgets.QSizePolicy.Policy.Fixed
        )
        self.verticalLayout_19.addItem(spacerItem97)

        self.label_16 = QtWidgets.QLabel(self.groupBox_12)
        font = QtGui.QFont()
        font.setWeight(50)
        font.setBold(False)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.verticalLayout_19.addWidget(self.label_16)

        self.label_24 = QtWidgets.QLabel(self.groupBox_12)
        font = QtGui.QFont()
        font.setWeight(50)
        font.setBold(False)
        self.label_24.setFont(font)
        self.label_24.setText("")
        self.label_24.setObjectName("label_24")
        self.verticalLayout_19.addWidget(self.label_24)

        spacerItem98 = QtWidgets.QSpacerItem(
            24, 13,
            QtWidgets.QSizePolicy.Policy.Minimum,
            QtWidgets.QSizePolicy.Policy.Fixed
        )
        self.verticalLayout_19.addItem(spacerItem98)

        self.horizontalLayout_25.addLayout(self.verticalLayout_19)
        self.verticalLayout_21.addWidget(self.groupBox_12)

        self.horizontalLayout_27.addLayout(self.verticalLayout_21)
        self.tabWidget.addTab(self.tab_4, "")

        self.verticalLayout_66.addWidget(self.tabWidget)
        ghost_phisher.setCentralWidget(self.centralwidget)

        self.retranslateUi(ghost_phisher)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(ghost_phisher)

    def retranslateUi(self, ghost_phisher):
        _translate = QtCore.QCoreApplication.translate
    
        ghost_phisher.setWindowTitle(_translate("ghost_phisher", "Ghost Phisher"))
        self.ghost_phisher_version_label.setText(_translate("ghost_phisher", "V1.46"))
    
        self.groupBox_15.setTitle(_translate("ghost_phisher", "Access Point Details"))
        self.access_point_label.setText(_translate("ghost_phisher", "Acess Point Name:"))
        self.channel_label.setText(_translate("ghost_phisher", "Channel:"))
        self.ip_address_label.setText(_translate("ghost_phisher", "IP address:"))
        self.main_mac_address_label.setText(_translate("ghost_phisher", "Mac Address:"))
        self.access_runtime.setText(_translate("ghost_phisher", "Runtime:"))
    
        self.groupBox_14.setTitle(_translate("ghost_phisher", "Wireless Interface "))
        self.comboBox.setToolTip(_translate(
            "ghost_phisher",
            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
            "p, li { white-space: pre-wrap; }\n"
            "</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:7pt; font-weight:400; font-style:normal;\">\n"
            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Select the wireless interface card you would like to use</p>\n"
            "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p></body></html>"
        ))

        self.refresh_button.setToolTip(_translate(
            "ghost_phisher",
            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
            "p, li { white-space: pre-wrap; }\n"
            "</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:7pt; font-weight:400; font-style:normal;\">\n"
            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">click to refresh list of newly inserted interface cards</p></body></html>"
        ))
        self.refresh_button.setText(_translate("ghost_phisher", "   Refresh Card List  "))
        self.acess_interface.setText(_translate("ghost_phisher", "Current Interface:"))
        self.mac_address_label.setText(_translate("ghost_phisher", "Mac Address:"))
        self.driver_label.setText(_translate("ghost_phisher", "Driver:"))
        self.monitor_label.setText(_translate("ghost_phisher", "Monitor:"))
        self.monitor_button.setToolTip(_translate("ghost_phisher", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">click to place wirless card on monitor mode</p></body></html>"))
        self.monitor_button.setText(_translate("ghost_phisher", "Set Monitor"))
        self.groupBox_16.setTitle(_translate("ghost_phisher", "Access Point Settings"))
        self.label_36.setText(_translate("ghost_phisher", "SSID:"))
        self.label_37.setText(_translate("ghost_phisher", "IP Address:"))
        self.access_name_edit.setToolTip(_translate("ghost_phisher", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">input the name of the access point</p></body></html>"))
        self.ip_address_label_2.setToolTip(_translate("ghost_phisher", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">input an ip adress you would like to bind access point to e.g 192.168.0.1</p></body></html>"))
        self.label_38.setText(_translate("ghost_phisher", "Channel:     "))
        self.channel_combo.setToolTip(_translate("ghost_phisher", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">select the channel you would like the access point run (default is channel 1)</p></body></html>"))
        self.groupBox_18.setTitle(_translate("ghost_phisher", "Cryptography"))
        self.rouge_radio.setText(_translate("ghost_phisher", "None"))
        self.wpa_radio.setText(_translate("ghost_phisher", "WPA"))
        self.wep_radio.setText(_translate("ghost_phisher", "WEP"))
        self.groupBox_17.setTitle(_translate("ghost_phisher", "Status"))
        self.access_connection_label.setText(_translate("ghost_phisher", "Connections:"))
        self.access_start.setToolTip(_translate("ghost_phisher", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Start Wireless Access Point</p></body></html>"))
        self.access_start.setText(_translate("ghost_phisher", "Start"))
        self.access_stop.setToolTip(_translate("ghost_phisher", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Stop Wireless Access Point</p></body></html>"))
        self.access_stop.setText(_translate("ghost_phisher", "Stop"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("ghost_phisher", "Fake Access Point"))
        self.groupBox.setTitle(_translate("ghost_phisher", "DNS Interface Settings"))
        self.card_interface_combo.setToolTip(_translate("ghost_phisher", "select the network interface card you want to use"))
        self.ip_address_combo.setToolTip(_translate("ghost_phisher", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Select the IP address that you want the service to run on. (0.0.0.0 is recommended)</span></p></body></html>"))
        self.current_card_label.setText(_translate("ghost_phisher", "Current Interface:  eth0"))
        self.service_dns_run_label.setText(_translate("ghost_phisher", "Service running on:  192.168.0.1"))
        self.dns_port.setText(_translate("ghost_phisher", "UDP DNS Port: 53"))
        self.label_5.setText(_translate("ghost_phisher", "Protocol: UDP (User Datagram Protocol)"))
        self.groupBox_2.setTitle(_translate("ghost_phisher", "Query Responce Settings"))
        self.resolveall_radio.setText(_translate("ghost_phisher", "Resolve all queries to the following address (The currently selected IP address is recommended)"))
        self.dns_ip_address.setToolTip(_translate("ghost_phisher", "input the address you want all dns queries to resolve to"))
        self.dns_ip_address.setStatusTip(_translate("ghost_phisher", "rtrtr"))
        self.respond_domain_radio.setText(_translate("ghost_phisher", "Respond with Fake address only to the following website domains"))
        self.label_6.setText(_translate("ghost_phisher", "Address:"))
        self.domain_ip.setToolTip(_translate("ghost_phisher", "input the address you want websites added to resolve into "))
        self.label_7.setText(_translate("ghost_phisher", "Website:"))
        self.domain_label.setToolTip(_translate("ghost_phisher", "input a website address"))
        self.domain_add_button.setToolTip(_translate("ghost_phisher", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">click to map websites to the corresponding faked address</span></p></body></html>"))
        self.domain_add_button.setText(_translate("ghost_phisher", "Add"))
        self.groupBox_3.setTitle(_translate("ghost_phisher", "Status"))
        self.dns_connection_label.setText(_translate("ghost_phisher", "Connections:"))
        self.dns_start.setToolTip(_translate("ghost_phisher", "Start DNS Server"))
        self.dns_start.setText(_translate("ghost_phisher", "Start"))
        self.dns_stop.setToolTip(_translate("ghost_phisher", "Stop DNS Server"))
        self.dns_stop.setText(_translate("ghost_phisher", "Stop"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.dns_tab), _translate("ghost_phisher", "Fake DNS Server"))
        self.groupBox_4.setTitle(_translate("ghost_phisher", "DHCP Version Information"))
        self.label.setText(_translate("ghost_phisher", "<font color=green>Ghost DHCP Server</font>"))
        self.label_2.setText(_translate("ghost_phisher", "Default  Port:   67"))
        self.label_3.setText(_translate("ghost_phisher", "Protocol: UDP (User Datagram Protocol)"))
        self.groupBox_5.setTitle(_translate("ghost_phisher", "DHCP Settings"))
        self.label_4.setText(_translate("ghost_phisher", "Start:             "))
        self.label_9.setText(_translate("ghost_phisher", "Subnet mask: "))
        self.label_10.setText(_translate("ghost_phisher", "Fake DNS:     "))
        self.start_ip.setToolTip(_translate("ghost_phisher", "input the address you want leasing to start from e.g 192.168.0.1"))
        self.subnet_ip.setToolTip(_translate("ghost_phisher", "input the subnet mask 255.255.255.0"))
        self.fakedns_ip.setToolTip(_translate("ghost_phisher", "input the address of the started Fake DNS Server"))
        self.label_8.setText(_translate("ghost_phisher", "End:        "))
        self.label_12.setText(_translate("ghost_phisher", "Gateway: "))
        self.label_11.setText(_translate("ghost_phisher", "Alt DNS:   "))
        self.stop_ip.setToolTip(_translate("ghost_phisher", "input address you want leasing to stop e.g 192.168.0.254"))
        self.gateway_ip.setToolTip(_translate("ghost_phisher", "input the defaulf gateway address, routers address"))
        self.alternatedns_ip.setToolTip(_translate("ghost_phisher", "input an alternate ip address"))
        self.groupBox_6.setTitle(_translate("ghost_phisher", "Status"))
        self.dhcp_start.setToolTip(_translate("ghost_phisher", "Start DHCP Server"))
        self.dhcp_start.setText(_translate("ghost_phisher", "Start"))
        self.dhcp_stop.setToolTip(_translate("ghost_phisher", "Stop DHCP Server"))
        self.dhcp_stop.setText(_translate("ghost_phisher", "Stop"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("ghost_phisher", "Fake DHCP Server"))
        self.groupBox_7.setTitle(_translate("ghost_phisher", "HTTP Interface Settings"))
        self.http_interface_combo.setToolTip(_translate("ghost_phisher", "Select an interface card"))
        self.http_ip_combo.setToolTip(_translate("ghost_phisher", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Select the IP address that you want the service to run on</p></body></html>"))
        self.current_card_label_2.setText(_translate("ghost_phisher", "Current Interface:  eth0"))
        self.http_ip_label.setText(_translate("ghost_phisher", "Service running on:  192.168.0.1"))
        self.http_port_label.setText(_translate("ghost_phisher", "TCP Port: 80"))
        self.label_13.setText(_translate("ghost_phisher", "Protocol: HTTP (Hypertext Transfer Protocol)"))
        self.groupBox_8.setTitle(_translate("ghost_phisher", "Webpage Settings"))
        self.emulate_website_radio.setText(_translate("ghost_phisher", "Clone Website:"))
        self.select_website_radio.setText(_translate("ghost_phisher", "Select Webpage:"))
        self.emulate_website_label.setToolTip(_translate("ghost_phisher", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Input the web address of a website you want to clone  e.g http://www.foo-bar.com/</span></p></body></html>"))
        self.website_linedit.setToolTip(_translate("ghost_phisher", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Input the path to a webpage you want to host   e.g /usr/local/bin/index.html</span></p></body></html>"))
        self.website_button.setText(_translate("ghost_phisher", "Browse"))
        self.label_25.setText(_translate("ghost_phisher", "Real Website IP Address or Url:"))
        self.run_webpage_port_radio.setText(_translate("ghost_phisher", "Run Webpage on Port :"))
        self.use_port_http.setToolTip(_translate("ghost_phisher", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">input the port number of which you want the HTTP server to run on   e.g 80</span></p></body></html>"))
        self.label_14.setText(_translate("ghost_phisher", "( Default HTTP Server port is 80 ) "))
        self.groupBox_9.setTitle(_translate("ghost_phisher", " Service Mode"))
        self.capture_radio.setText(_translate("ghost_phisher", "Credential Capture Mode"))
        self.hosting_radio.setText(_translate("ghost_phisher", "Hosting  Mode"))
        self.groupBox_10.setTitle(_translate("ghost_phisher", "Status"))
        self.http_captured_credential.setText(_translate("ghost_phisher", "captured credentials:"))
        self.http_captured_credential_2.setText(_translate("ghost_phisher", "Please refer to the Harvested Credential Tab to view captured credentials"))
        self.http_start.setToolTip(_translate("ghost_phisher", "Start the HTTP Server"))
        self.http_start.setText(_translate("ghost_phisher", "Start"))
        self.http_stop.setToolTip(_translate("ghost_phisher", "Stop the HTTP Server"))
        self.http_stop.setText(_translate("ghost_phisher", "Stop"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("ghost_phisher", "Fake HTTP Server"))
        self.groupBox_19.setTitle(_translate("ghost_phisher", "Interface Settings"))
        self.spawn_http_interface_combo.setToolTip(_translate("ghost_phisher", "select the network interface card you want to use"))
        self.spawn_ip_combo.setToolTip(_translate("ghost_phisher", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Select the IP Address to want the service to run </span></p></body></html>"))
        self.ghost_vul_combo.setToolTip(_translate("ghost_phisher", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Use Ghost default vulnerability page display</p></body></html>"))
        self.ghost_vul_combo.setText(_translate("ghost_phisher", "Ghost Vulnerability Page"))
        self.custom_vul_combo.setToolTip(_translate("ghost_phisher", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Choose a custom vulnerability page to display to the victim</p></body></html>"))
        self.custom_vul_combo.setText(_translate("ghost_phisher", "Custom Vulnerability Page"))
        self.spawn_http_setting_box.setTitle(_translate("ghost_phisher", "HTTP Settings"))
        self.cookies_checkbox.setToolTip(_translate("ghost_phisher", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">This option only allows victims to progress after payload has been downloaded by their machines</p></body></html>"))
        self.cookies_checkbox.setText(_translate("ghost_phisher", "Save Cookies"))
        self.force_download_checkbox.setToolTip(_translate("ghost_phisher", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">This option forces user  into downloading payload upon connection</p></body></html>"))
        self.force_download_checkbox.setText(_translate("ghost_phisher", "Force Payload Download"))
        self.respond_to_all_radio.setToolTip(_translate("ghost_phisher", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">With this option, service will respond to all operating system types</p></body></html>"))
        self.respond_to_all_radio.setText(_translate("ghost_phisher", "Respond to all"))
        self.respond_windows_radio.setToolTip(_translate("ghost_phisher", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">With this option, service will respond only to windows machine</p></body></html>"))
        self.respond_windows_radio.setText(_translate("ghost_phisher", "Respond to Only Windows"))
        self.respond_linux_radio.setToolTip(_translate("ghost_phisher", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">With this option, service will respond only to Linux machines</p></body></html>"))
        self.respond_linux_radio.setText(_translate("ghost_phisher", "Respond to Only Linux"))
        self.label_29.setText(_translate("ghost_phisher", "HTTP Port:"))
        self.ghost_trap_http_edit.setToolTip(_translate("ghost_phisher", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Type the  HTTP port to be used for HTTP requests</p></body></html>"))
        self.ghost_trap_http_edit.setText(_translate("ghost_phisher", "80"))
        self.custom_page_label.setText(_translate("ghost_phisher", "Select Custom Page:"))
        self.custom_page_label_2.setToolTip(_translate("ghost_phisher", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Select custom vulnerability page</p></body></html>"))
        self.custom_page_button.setToolTip(_translate("ghost_phisher", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Browse and select page</p></body></html>"))
        self.custom_page_button.setText(_translate("ghost_phisher", "Browse"))
        self.metasploit_payload_radio.setToolTip(_translate("ghost_phisher", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Select to use metasploit payload attacks</p></body></html>"))
        self.metasploit_payload_radio.setText(_translate("ghost_phisher", "Metasploit Payload Attack"))
        self.custom_payload_radio.setToolTip(_translate("ghost_phisher", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Select to use custom payload attacks</p></body></html>"))
        self.custom_payload_radio.setText(_translate("ghost_phisher", "Custom Payload Attack"))
        self.metasploit_settings_box.setTitle(_translate("ghost_phisher", "Metasploit Payload Settings"))
        self.label_30.setText(_translate("ghost_phisher", "Select Windows Payload:"))
        self.label_32.setText(_translate("ghost_phisher", "Encode Type:"))
        self.windows_payload_combo.setToolTip(_translate("ghost_phisher", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Select from list of metasploits payloads for windows</p></body></html>"))
        self.encode_combo.setToolTip(_translate("ghost_phisher", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Choose encoder type</p></body></html>"))
        self.label_33.setText(_translate("ghost_phisher", "Encode Number:"))
        self.comboBox_2.setToolTip(_translate("ghost_phisher", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Choose number of times to encode executables</p></body></html>"))
        self.label_31.setText(_translate("ghost_phisher", "Select Linux Payload:"))
        self.label_34.setText(_translate("ghost_phisher", "Port Settings:"))
        self.linux_payload_combo.setToolTip(_translate("ghost_phisher", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Select from list of metasploits payloads for Linux</p></body></html>"))
        self.port_setting_edit.setToolTip(_translate("ghost_phisher", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">TCP port for metasploit to listen on</p></body></html>"))
        self.label_35.setText(_translate("ghost_phisher", "IP Address:"))
        self.ip_address_edit.setToolTip(_translate("ghost_phisher", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">IP Address for metasploit to listen on</p></body></html>"))
        self.custom_payload_box.setTitle(_translate("ghost_phisher", "Custom Payload Settings"))
        self.windows_exec_checkbox.setText(_translate("ghost_phisher", "Windows Executable:"))
        self.linux_exec_checkbox.setText(_translate("ghost_phisher", "Linux Executable:"))
        self.windows_exec_edit.setToolTip(_translate("ghost_phisher", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Select custom windows executable to be served</p></body></html>"))
        self.linux_exec_edit.setToolTip(_translate("ghost_phisher", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Select linux executable to be served</p></body></html>"))
        self.windows_exec_button.setText(_translate("ghost_phisher", "Browse"))
        self.linux_exec_button.setText(_translate("ghost_phisher", "Browse"))
        self.nitialize_label.setText(_translate("ghost_phisher", "Initializing"))
        self.setting_payload_label.setText(_translate("ghost_phisher", "Setting Payload"))
        self.create_cache_label.setText(_translate("ghost_phisher", "Creating Cache"))
        self.http_start_label.setText(_translate("ghost_phisher", "Starting HTTP"))
        self.groupBox_20.setTitle(_translate("ghost_phisher", "Status"))
        self.ghost_spawn_start.setToolTip(_translate("ghost_phisher", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Start GHOST Trap</p></body></html>"))
        self.ghost_spawn_start.setText(_translate("ghost_phisher", "Start"))
        self.ghost_spawn_stop.setToolTip(_translate("ghost_phisher", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Stop GHOST Trap</p></body></html>"))
        self.ghost_spawn_stop.setText(_translate("ghost_phisher", "Stop"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), _translate("ghost_phisher", "GHOST Trap"))
        self.label_44.setText(_translate("ghost_phisher", "Fern Cookie Hijacker is an Ethernet and WIFI based session Hijacking tool able to clone remote online web sessions by sniffing and capturing session cookie packets from remote hosts  by leveraging various"))
        self.label_45.setText(_translate("ghost_phisher", "internal MITM attacks with routing capabilities"))
        self.refresh_button_3.setText(_translate("ghost_phisher", "Refresh"))
        self.monitor_interface_label_2.setText(_translate("ghost_phisher", "Ethernet Mode"))
        self.sniffing_status_label_2.setText(_translate("ghost_phisher", "Sniffing Status"))
        self.cookie_detection_label_2.setText(_translate("ghost_phisher", "Cookie Detection Buffer"))
        self.mitm_activated_label.setText(_translate("ghost_phisher", "Internal MITM Engine Activated"))
        self.ethernet_mode_radio_2.setToolTip(_translate("ghost_phisher", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Use this option if you are currently connected to the ethernet gateway/access point</p></body></html>"))
        self.ethernet_mode_radio_2.setText(_translate("ghost_phisher", "Ethernet Mode"))
        self.passive_mode_radio_2.setToolTip(_translate("ghost_phisher", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Use this option if you are not connected to access point</p></body></html>"))
        self.passive_mode_radio_2.setText(_translate("ghost_phisher", "Passive Mode"))
        self.label_46.setText(_translate("ghost_phisher", "Gateway IP Address / Router IP Address:"))
        self.treeWidget.headerItem().setText(0, _translate("ghost_phisher", " "))
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        self.treeWidget.topLevelItem(0).setText(0, _translate("ghost_phisher", "192.168.0.1"))
        self.treeWidget.topLevelItem(0).child(0).setText(0, _translate("ghost_phisher", "www.google.com"))
        self.treeWidget.topLevelItem(0).child(0).child(0).setText(0, _translate("ghost_phisher", "HTTP response"))
        self.treeWidget.topLevelItem(0).child(1).setText(0, _translate("ghost_phisher", "www.twitter.com"))
        self.treeWidget.topLevelItem(0).child(1).child(0).setText(0, _translate("ghost_phisher", "HTTP over"))
        self.treeWidget.topLevelItem(1).setText(0, _translate("ghost_phisher", "198.178.23.1"))
        self.treeWidget.topLevelItem(1).child(0).setText(0, _translate("ghost_phisher", "www.gmail.com"))
        self.treeWidget.topLevelItem(1).child(0).child(0).setText(0, _translate("ghost_phisher", "respose server"))
        self.treeWidget.setSortingEnabled(__sortingEnabled)
        self.cookies_captured_label_2.setText(_translate("ghost_phisher", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; color:#008000;\">5 Cookies Captured</span></p></body></html>"))
        self.start_sniffing_button_2.setText(_translate("ghost_phisher", "   Start Sniffing   "))
        self.start_sniffing_button_3.setToolTip(_translate("ghost_phisher", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Start Session Hijacking</p></body></html>"))
        self.start_sniffing_button_3.setText(_translate("ghost_phisher", "Start"))
        self.stop_sniffing_button_3.setToolTip(_translate("ghost_phisher", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Stop Session Hijacking</p></body></html>"))
        self.stop_sniffing_button_3.setText(_translate("ghost_phisher", "Stop"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_7), _translate("ghost_phisher", "Session Hijacking"))
        self.label_39.setText(_translate("ghost_phisher", "Ghost ARP Cache Poisoning poisons the ARP cache of the Operating Systems in the subnet and redirect all traffic meant for the Target Address to itself:"))
        self.refresh_button_4.setText(_translate("ghost_phisher", "Refresh"))
        self.groupBox_23.setTitle(_translate("ghost_phisher", "Target Settings"))
        self.label_47.setText(_translate("ghost_phisher", "Target Address :"))
        self.groupBox_24.setTitle(_translate("ghost_phisher", "Options"))
        self.poison_one_way_combo.setToolTip(_translate("ghost_phisher", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Direct all traffic to Ghost without any redirection to target address</p></body></html>"))
        self.poison_one_way_combo.setText(_translate("ghost_phisher", "Poison One Way (DOS Attack)"))
        self.route_traffic_combo.setToolTip(_translate("ghost_phisher", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Redirect all traffic to Ghost with redirection to target address</p></body></html>"))
        self.route_traffic_combo.setText(_translate("ghost_phisher", "Redirect Traffic to Target Address (MITM Attack)"))
        self.groupBox_21.setTitle(_translate("ghost_phisher", "Status"))
        self.label_40.setText(_translate("ghost_phisher", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Note: </span>Please dont run this attack, along side Session Hijacking to avoid misdirection of network traffic</p></body></html>"))
        self.start_arp_poison.setToolTip(_translate("ghost_phisher", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Start ARP Poisoning</p></body></html>"))
        self.start_arp_poison.setText(_translate("ghost_phisher", "Start"))
        self.stop_arp_poison.setToolTip(_translate("ghost_phisher", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Stop ARP Poisoning</p></body></html>"))
        self.stop_arp_poison.setText(_translate("ghost_phisher", "Stop"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_8), _translate("ghost_phisher", "ARP Cache Poisoning"))
        self.credential_table.horizontalHeaderItem(0).setText(_translate("ghost_phisher", "Website"))
        self.credential_table.horizontalHeaderItem(1).setText(_translate("ghost_phisher", "Username"))
        self.credential_table.horizontalHeaderItem(2).setText(_translate("ghost_phisher", "Password"))
        self.savechanges_button.setText(_translate("ghost_phisher", "Save Changes"))
        self.insert_button.setText(_translate("ghost_phisher", "Insert"))
        self.delete_button.setText(_translate("ghost_phisher", "Delete"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("ghost_phisher", "Harvested Credentials"))
        self.groupBox_13.setTitle(_translate("ghost_phisher", "About Ghost Phisher"))
        self.label_17.setText(_translate("ghost_phisher", "Ghost Phisher is an application written in python that gives its user the power to control network"))
        self.label_18.setText(_translate("ghost_phisher", "services with an ultimate aim of harvesting information from a vulnerable network connection through"))
        self.label_20.setText(_translate("ghost_phisher", " various penetration attacks, the included network services could be used individually or collectively"))
        self.label_19.setText(_translate("ghost_phisher", " for different types of  attacks or run normal service queries."))
        self.groupBox_11.setTitle(_translate("ghost_phisher", "Disclaimer"))
        self.label_21.setText(_translate("ghost_phisher", "Use this program for testing your own network to see if they are vulnerable to the various "))
        self.label_22.setText(_translate("ghost_phisher", " attacks that could be perpetrated with this program.  DO NOT USE IT on networks of which "))
        self.label_23.setText(_translate("ghost_phisher", "you do not have permission to test."))
        self.groupBox_12.setTitle(_translate("ghost_phisher", "Authoring"))
        self.label_15.setText(_translate("ghost_phisher", "Written by:    Saviour Emmanuel Ekiko              savioboyz@rocketmail.com "))
        self.label_27.setText(_translate("ghost_phisher", "Contributor:  Kashif Iftikhar                               a10n3.s7r1k3r@gmail.com"))
        self.label_16.setText(_translate("ghost_phisher", "Special thanks to Chris Ondrovic,Lee Baird and others for their wonderful supports through my projects"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("ghost_phisher", "About"))

