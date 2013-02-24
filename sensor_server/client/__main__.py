import os
import sys
import json
import socket
import serial
import time

SERVER_PORT = 5557
SERVER_HOST = 'hcf.io'

def connect(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))
    return sock

def make_json_packet(temp, humidity):
    obj = {}
    obj['host'] = os.uname()[1]
    sensors = {}
    obj['sensors'] = sensors
    sensors['Humidity'] = humidity
    sensors['Temperature'] = temp
    text = json.dumps(obj)
    print text
    return text

def read_json_packet(uart):
    found = False
    depth = 1
    text = ['{']
    while not found:
        found = uart.read(1) == '{'
    char = None
    while depth != 0:
        data = uart.read(1)
        text.append(data)
        if data == '{':
            depth += 1
        elif data == '}':
            depth -= 1
    return json.loads(''.join(text))

def sensor_loop(sock):
    ser = serial.Serial(
        port='/dev/ttyAMA0',
        baudrate=9600,
        timeout=1,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS
        )

    while True:
        packet = read_json_packet(ser)
        sock.sendall(make_json_packet(packet['Temperature'], packet['Humidity']))

def main():
    sock = connect(SERVER_HOST, SERVER_PORT)
    sensor_loop(sock)
    return 0

if __name__ == '__main__':
    sys.exit(main())
