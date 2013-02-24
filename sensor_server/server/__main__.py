import sys
import socket
import threading
import RPi.GPIO as GPIO


LISTEN_PORT = 5555
LISTEN_HOST = ''


class ClientThread(threading.Thread):
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
                depth += 1
            elif data == '}':
                depth -= 1
        return json.loads(''.join(text))

    def __init__(self, conn, addr):
        super(ClientThread, self).__init__()
        self.conn = conn
        self.addr = addr
        GPIO.setmode(GPIO.BOARD)

    def run(self):
        print("New client connected: %s" % (repr(self.addr)))
        # Do stuff
        try:
            command = self.read_json_packet()
            print("Data: %s" % (command))
            GPIO.setup(packet['IOPin'], GPIO.OUT)
            GPIO.output(packet['IOPin'], packet['State'])

        finally:
            print("Client exiting: %s" % (repr(self.addr)))
            self.conn.close()
            return


def setup_socket():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((LISTEN_HOST, LISTEN_PORT))
    sock.listen(1)
    return sock


def accept(sock):
    while True:
        conn, addr = sock.accept()
        ClientThread(conn,addr).start()


def main():
    sock = setup_socket()
    accept(sock)

if __name__ == '__main__':
    sys.exit(main())
