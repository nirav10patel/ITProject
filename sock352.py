import binascii
import socket as syssock
import struct
import sys

# these functions are global to the class and
# define the UDP ports all messages are sent
# and received from

sock352PktHdrData = '!BBBBHHLLQQLL'
udpPortTx = 0   #this is the UDPportTX we get as input from client/server to the global init() function
udpPortRx = 0   #this is the UDPportTX we get as input from client/server to the global init() function
#here we declare that we are going to be using UDP
udpSock = syssock.socket(syssock.AF_INET, syssock.SOCK_DGRAM)   #this is the main socket we will be using with UDP
version = 0x1
flags
opt_ptr = 0x0
protocol = 0x0
header_len
checksum = 0x0
source_port = 0x0
dest_port = 0x0
sequence_no
ack_no
window = 0x0
payload_len

def init(UDPportTx,UDPportRx):   # initialize your UDP socket here
    udpPortRx = int(UDPportRx)
    if(UDPportTx == ''):
        udpPortTx = int(UDPportRx)
    else:
        udpPortTx = int(UDPportTx)

    #udpSock = syssock.socket(syssock.AF_INET, syssock.SOCK_DGRAM)
    udpSock.bind(('', udpPortRx))
    udpSock.settimeout(0.2);
    print("It worked")
    pass

class socket:
    def updateStruct():
        udpPkt_hdr_data = struct.Struct(sock352PktHdrData)
        return udpPkt_hdr_data.pack(version, flags, opt_ptr, protocol, header_len, checksum, source_port, dest_port, sequence_no, ack_no, window, payload_len)

    def __init__(self):  # fill in your code here
        return

    def bind(self,address):
        return

    def connect(self,address):  # fill in your code here
        return

    def listen(self,backlog):
        return

    def accept(self):
        (clientsocket, address) = (1,1)  # change this to your code
        return (clientsocket,address)

    def close(self):   # fill in your code here
        return

    def send(self,buffer):
        bytessent = 0     # fill in your code here
        return bytesent

    def recv(self,nbytes):
        bytesreceived = 0     # fill in your code here
        return bytesreceived
