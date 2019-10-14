import binascii
import socket as syssock
import struct
import sys
import random

# these functions are global to the class and
# define the UDP ports all messages are sent
# and received from

sock352PktHdrData = '!BBBBHHLLQQLL'
udpPortTx = 0   #this is the UDPportTX we get as input from client/server to the global init() function
udpPortRx = 0   #this is the UDPportTX we get as input from client/server to the global init() function
#here we declare that we are going to be using UDP
udpSock = syssock.socket(syssock.AF_INET, syssock.SOCK_DGRAM)   #this is the main socket we will be using with UDP
version = 0x1
opt_ptr = 0x0
protocol = 0x0
checksum = 0x0
source_port = 0x0
dest_port = 0x0
window = 0x0
header_len = 40
seqNum = 0
recAddress = ""
deliveredData = ""

SOCK352_SYN = 0x01
SOCK352_FIN = 0x02
SOCK352_ACK = 0x04
SOCK352_RESET = 0x08
SOCK352_HAS_OPT = 0xA0

def init(UDPportTx,UDPportRx):   # initialize your UDP socket here
    udpPortRx = int(UDPportRx)
    if(UDPportTx == ''):
        udpPortTx = int(UDPportRx)
    else:
        udpPortTx = int(UDPportTx)
    #udpSock = syssock.socket(syssock.AF_INET, syssock.SOCK_DGRAM)
    udpSock.bind(('', udpPortRx))
    udpSock.settimeout(5);
    print("It worked")
    pass

class socket:
    def updateStruct(self, newFlags, newHeader_len, newSeqNo, newAckNo, newPayloadLen):
        global version, opt_ptr, protocol, checksum, source_port, dest_port, window, udpSock
        flags = newFlags
        header_len = newHeader_len
        sequence_no = newSeqNo
        ack_no = newAckNo
        payload_len = newPayloadLen
        udpPkt_hdr_data = struct.Struct(sock352PktHdrData)
        return udpPkt_hdr_data.pack(version, flags, opt_ptr, protocol, header_len, checksum, source_port, dest_port, sequence_no, ack_no, window, payload_len)

    def __init__(self):  # fill in your code here
        return

    def bind(self,address):
        return

    def connect(self,address):  # fill in your code here
        global udpSock, seqNum, header_len
        seqNum = int(random.randint(20, 100))
        data = self.updateStruct(SOCK352_SYN, header_len, seqNum, 0, 0)
        ackServer = -1;
        while True:
            print("CONNECTING")
            udpSock.sendto(data, (address[0], udpPortTx))
            #print("\tRequesting a new connection...%d bytes sent!" % (udpSock.sendto(data, (address[0], udpPortTx) ) ) )
            serverData = self.getData()
            ackServer = serverData[9]
            if ackServer == seqNum + 1:
                print("SUCCESSFUL CONNECT")
                break
            else:
                print("FAILED CONNECT TRYING AGAIN")
                print("ACK: " + str(ackServer) + " SEQ: " + str(seqNum))
        udpSock.connect((address[0], udpPortTx))
        seqNum = seqNum + 1
        return

    def listen(self,backlog):
        return

    def accept(self):
        #in this method, we must use the recvfrom(), its like the linnux call
        #that is how we know that an object of class sock352 somewhere has sent something
        global udpSock, udpPortRx, seqNum, header_len

        updatedStruct = ""
        while(True):
            updatedStruct = self.getData()
            if(updatedStruct[1] == SOCK352_SYN):
                seqNum = updatedStruct[8]
                break
        newSeqNum = int(random.randint(20, 100))
        struct = self.updateStruct(SOCK352_SYN + SOCK352_ACK, header_len, newSeqNum, seqNum+1, 8)
        udpSock.sendto(struct + "Accepted", recAddress)

        while(True):
            updatedStruct = self.getData()
            if(updatedStruct[1] == SOCK352_ACK):
                seqNum = updatedStruct[8]
                break
        #connection established, no they can communicate safely
        seqNum = seqNum+1
        print("Connection Established")
        (clientsocket, address) = (socket(), recAddress)  # change this to your code
        return (clientsocket,address)

    def getData(self):
        global udpSock, sock352PktHdrData, recAddress, deliveredData
        try:
            (message, sendAddress) = udpSock.recvfrom(4096)
        except syssock.timeout:
            print("No packets received")
            return[0,0,0,0,0,0,0,0,0,0,0,0]
        #(head, body) = (message[:40], message[40:])
        # head = message[:40]
        # body = message[40:]
        deliveredData = struct.unpack(sock352PktHdrData, head)
        if(head[1] == SOCK352_SYN):
            print("SYN")
            recAddress = sendAddress
            return deliveredData
        if(head[1] == SOCK352_SYN + SOCK352_ACK):
            print("SYN + ACK")
            recAddress = sendAddress
            return deliveredData

    def close(self):   # fill in your code here
        return

    def send(self,buffer):
        bytessent = 0     # fill in your code here
        return bytesent

    def recv(self,nbytes):
        bytesreceived = 0     # fill in your code here
        return bytesreceived
