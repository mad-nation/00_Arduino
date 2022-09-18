import time
import serial

arduionoData = serial.Serial('/dev/tty.usbserial-1420', 9600)
time.sleep(1)
while True:
    while(arduionoData.inWaiting==0):
        pass
    dataPacket = arduionoData.readline()
    dataPacket= str(dataPacket, 'utf-8')
    dataPacket = dataPacket.strip('\r\n')
    dataPacket = int(dataPacket)
    print(dataPacket)
    # if dataPacket > 10:
    #     print("> 10")
    # elif dataPacket < 10:
    #     print("< 10")
    # else:
    #     print("= 10")