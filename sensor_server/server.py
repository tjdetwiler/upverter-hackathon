import sys
import json
import socket
import threading


class ClientThread(threading.Thread):
    def __init__(self, server, conn, addr):
        super(ClientThread, self).__init__()
        self.server = server
        self.conn = conn
        self.addr = addr
        self._last_packets = []



    def read_json_packet(self):
        found = False
        depth = 1
        text = ['{']
        while not found:
            found = self.conn.recv(1) == '{'
        char = None
        while depth != 0:
            data = self.conn.recv(1)
            text.append(data)
            if data == '{':
                depth+=1
            elif data == '}':
                depth-=1
        return json.loads(''.join(text))
        
    def run(self):
        print("New client connected: %s" % (repr(self.addr)))
        # Do stuff
        try:
            while True:
                packet = self.read_json_packet()
                self._last_packets.append(packet)

                while len(self._last_packets) >= 100:
                    del(self._last_packets[0])

                print("Received Packet")
                print("%s" % (packet))
        finally:
            print("Client exiting: %s" % (repr(self.addr)))
            self.conn.close()

    def get_last_packet(self):
        return self._last_packets[-1]

    def get_last_packets(self):
        return self._last_packets


class SensorServer(threading.Thread):
    def __init__(self, host, port):
        super(SensorServer, self).__init__()
        self.host = host
        self.port = port
        self.clients = []

    def setup_socket(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print self.host
        print self.port
        sock.bind((self.host, self.port))
        sock.listen(1)
        return sock

    def accept(self, sock):
        while True:
            conn, addr = sock.accept()
            c = ClientThread(self, conn, addr)
            self.clients.append(c)
            c.start()

    def run(self):
        sock = self.setup_socket()
        self.accept(sock)
