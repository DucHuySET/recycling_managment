import time
import serial
import random
async def readRs232():
    ser = serial.Serial(
        port='COM8',
        baudrate=9600,
        timeout=1,
        parity=serial.PARITY_ODD,
        stopbits=serial.STOPBITS_TWO,
        bytesize=serial.EIGHTBITS
    )

    ser.isOpen()
    # Reading the data from the serial port. This will be running in an infinite loop.
    for i in range(10):
        bytesToRead = ser.inWaiting()
        data = ser.read(bytesToRead)
        await time.sleep(2)
        print(data)
        dataStr = str(data).replace("b\'", "").replace("\'","")
        if dataStr != "":
            return dataStr

# def sendRs232():
#     serPort = serial.Serial(port= 'COM10')
#     while True:
#         data = random.randint(1, 200)
#         print(data)
#         serPort.write(str(data))
#         print('sent')
#         time.sleep(1)
# sendRs232()