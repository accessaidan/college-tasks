import socket
from datetime import datetime

from threading import Thread, Lock
from queue import Queue

import colorama
from colorama import Fore

import pyfiglet

ascii_banner = pyfiglet.figlet_format("PORT SCANNER")
print(ascii_banner)

colorama.init()
GREEN = Fore.GREEN
BLUE = Fore.BLUE
GREY = Fore.LIGHTBLACK_EX
RESET = Fore.RESET

THREADS = 200
q = Queue()
print_lock = Lock()

START_PORT = 0
END_PORT = 1024
ports = [p for p in range(START_PORT, END_PORT)]

def port_scan(host, port):
    s = socket.socket()
    #s.settimeout(0.2)
    try:
        s.connect((host, port))
    except socket.error:
        with print_lock:
            print(f"{GREY}[!] {host}:{port} is closed {RESET}", end="\r")
    else:
        with print_lock:
            print(f"{GREEN}[+] {host}:{port} is open        {RESET}")
    finally:
        s.close()

def scan_thread():
    while True:
        port = q.get() # Get the port number from the queue
        port_scan(host, port) # Scan that port number
        q.task_done() # Indicate that a formerly enqueued task is complete

def main():
    for t in range(THREADS):
        t = Thread(target=scan_thread) # target is the callable object to be invoked by the run() method
        t.daemon = True # A daemon thread is a thread that dies whenever the main thread dies
        t.start() # Start the daemon thread’s activity
    for port in ports:
        q.put(port) # Put item into the queue
    q.join() # Blocks until all items in the queue have been gotten and processed
    
if __name__ == "__main__":
    
    host = input("[?] Enter the host: ")
    #port_range = input("[?] Enter port range: ")
    #start_port, end_port = port_range.split("-")

    print(f"{BLUE}[>] Scanning ports: {START_PORT}-{END_PORT} {RESET}")
    t1 = datetime.now()
    print(f"{BLUE}[>] Scanning started at: {t1} {RESET}") 
    
    main()

    t2 = datetime.now()
    total_time = t2 - t1
    print(f"{BLUE}[>] Scanning complete in: {total_time} {RESET}")