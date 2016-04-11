#!/usr/bin/python
# -*- coding: utf-8 -*-

import serial


def open_serial(port, baud, timeout):
    ser = serial.Serial(port=port, baudrate=baud, timeout=timeout)
    if ser.isOpen():
        return ser
    else:
        print 'SERIAL ERROR'


def close(ser):
    ser.close()


def write_data(ser, data):
    ser.write(data)


def read_data(ser, size=1):
    return ser.read(size)


def to_hex(val):
    return chr(val)


def decode_data(data):
    res = ''
    for d in data:
        res += hex(ord(d)) + ' '

    return res

def checksum(*args):
    #print hex( 0xFF & ~( sum(args)))
    return hex( 0xFF & ~( sum(args))) 

if __name__ == '__main__':

    # we open the port
    serial_port = open_serial('/dev/ttyUSB0', 1000000, timeout=0.1)

    # we create the packet for a LED ON command
    # two start bytes
    data_start = 0xff

    # id of the motor (here 1), you need to change
    data_id = 0x01

    # lenght of the packet
    data_lenght = 0x04

    # instruction write= 0x03
    data_instruction = 0x03
    # instruction parameters
    data_param1 = 0x19  # LED address=0x19
    data_param2 = 0x01  # write 0x01

    print "Test en cours..."
    compteur = 0
    for i in range(0, 253):
        data_id = i
        data_checksum = checksum(data_id, data_lenght, data_instruction, data_param1, data_param2)
        data = to_hex(data_start) + to_hex(data_start) + to_hex(data_id) + to_hex(data_lenght) + \
        to_hex(data_instruction) + to_hex(data_param1) + to_hex(int(data_checksum, 16))
        #print data
        # print decode_data(data)
        write_data(serial_port, data)
        datas = read_data(serial_port, 6)
        if datas:
            print "ID decouvert : ",i
            print decode_data(datas),"\n"
            compteur += 1
            if compteur == 3: 
                break
    print "Test terminé"
