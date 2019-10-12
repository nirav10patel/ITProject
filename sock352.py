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
udpSock    #this is the main socket we will be using with UDP

def init(UDPportTx,UDPportRx):   # initialize your UDP socket here
    #whenever you want to use globals in python, you have to declare the 'global' variables as shown below
    global udpPortTx, udpPortRx, udpSock
    udpPortRx = UDPportRx
    udpPortTx = UDPportTx
    #here we declare that we are going to be using UDP
    udpSock = syssock.socket(syssock.AF_INET, syssock.SOCK_DGRAM)
    udpSock.bind('', udpPortRx)
    pass

class socket:

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
