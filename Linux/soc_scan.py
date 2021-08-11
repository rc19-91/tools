#!/usr/bin/env python3
import threading
import socket
import sys
import time
from queue import Queue

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

try:
    print_lock = threading.Lock()
    if len(sys.argv) !=2 :
        print ("Usage: soc_scan.py <host>")
        sys.exit(1)

    host = sys.argv[1]

    def scan(port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            con = s.connect((host, port))
            with print_lock:
                print('Port: ' + str(port) + bcolors.OKGREEN+' is open'+ bcolors.ENDC)
                con.close()
        except:
            pass
            #print('Port: ' + str(port) + bcolors.WARNING+' is close'+ bcolors.ENDC)

    def threader():
        while True:
            worker = q.get()
            scan(worker)
            q.task_done()

    q = Queue()

    for x in range(100):
        t = threading.Thread(target=threader)
        t.daemon = True
        t.start()

    #ports
    for worker in range(1, 65535):
        q.put(worker)

    q.join()

except KeyboardInterrupt:
        print("[X] Salida Forzada .....")
