import socket
import sys
import argparse

def main():
    parser = argparse.ArgumentParser(description="Send to the Crackme")
    parser.add_argument('--port', dest="port", default="1337", help="Port to connect")
    parser.add_argument('--buf', dest="buf", default="0", help="Buffer to send")
    args = parser.parse_args()
    my_port = int(args.port, 10)
    print '[+] Connecting to port: ' + hex(my_port)
    key = args.buf
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('127.0.0.1', my_port))
        s.send(key)
        result = s.recv(512)
        if result is not None:
            print "[+] Response: " + result
        s.close()
    except socket.error:
        print "Could not connect to the socket. Is the crackme running?"
    
if __name__ == "__main__":
    sys.exit(main())
	