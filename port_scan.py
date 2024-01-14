#!/usr/bin/python3

import socket
import sys
import time
import datetime
import argparse
import os
import re
from ping3 import ping

common_ports = {
    '21': 'FTP',
    '22': 'SSH',
    '23': 'TELNET',
    '25': 'SMTP',
    '53': 'DNS',
    '80': 'HTTP',
    '110': 'POP3',
    '139': 'NETBIOS-SSN',
    '143': 'IMAP',
    '443': 'HTTPS',
    '445': 'NETBIOS-SMB',
    '587': 'STMP SSL',
    '995': 'POP3-SSL',
    '993': 'IMAP-SSL',
    '1701': 'L2TP',
    '3306': 'MYSQL',
    '3389': 'RDP',
    '5800': 'VNC-5800',
    '5900': 'VNC-5900',
    '6969': 'Torrent',
    '8080': 'HTTP Proxy',
    '8443': 'PLESK',
    '9443': 'QVPN',
    '10000': 'VIRTUALMIN/WEBMIN'
}

def check_port(host, port, result=1):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # udp protocal socket.SOCK_DGRAM, tcp protocal socket.SOCK_STREAM
        sock.settimeout(0.5)
        r = sock.connect_ex((host, port))
        if r == 0:
            result = r
        sock.close()
    except Exception as e:
        pass

    return result

def get_service(port):
    port = str(port)
    if port in common_ports:
        return common_ports[port]
    else:
        return "Unknown service"

flag = 0
os.system('clear')

line = "+" * 80
desc = line + '''\nA Simple port scanner that works!! (c) digitz.org
    Example usage: python port_scanner.py 192.168.1.1 1 1000
    The above example will scan the host '192.168.1.1' from port 1 to 1000
    To scan most common ports, use: python port_scanner.py 192.168.1.1\n''' + line + "\n"

parser = argparse.ArgumentParser(description=desc, formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument('host', metavar='H', help='IPv4 address you want to scan')
parser.add_argument('startport', metavar='P1', nargs='?', help='Start scanning from this port')
parser.add_argument('endport', metavar='P2', nargs='?', help='Scan until this port')
args = parser.parse_args()

ipv4_pattern = re.compile(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$')
if not ipv4_pattern.match(args.host):
    print("Error: Invalid IPv4 address.")
    sys.exit(1)

try:
    ip = args.host
except ValueError:
    print("Error: Invalid IPv4 address.")
    sys.exit(1)

if args.startport and args.endport:
    start_port = int(args.startport)
    end_port = int(args.endport)
else:
    flag = 1

starting_time = time.time()
print("+" * 40)
print("\tSimple Port Scanner..!!!")
print("+" * 40)
print("Scanning started at %s" % (time.strftime("%I:%M:%S %p")))

hosts = [ip]

if flag:
    print("Scanning for most common ports on %s" % ip)
else:
    print("Scanning %s from port %s - %s: " % (ip, start_port, end_port))

print("")

for host in hosts:
    try:
        host = str(host)
        ping_result = ping(host)
        if ping_result:
            print("\r" + "=" * 40)
            print("Scan host %s" % (host))
            print("Connecting to Port: ", end="")

            open_ports = []
            if flag:
                for p in sorted(common_ports):
                    sys.stdout.flush()
                    p = int(p)
                    print(p, end="")
                    response = check_port(host, p)
                    if response == 0:
                        open_ports.append(p)
                    sys.stdout.write('\b' * len(str(p)))
            else:
                for p in range(start_port, end_port + 1):
                    sys.stdout.flush()
                    print(p, end="")
                    response = check_port(host, p)
                    if response == 0:
                        open_ports.append(p)
                    if not p == end_port:
                        sys.stdout.write('\b' * len(str(p)))

            print("")

            if open_ports:
                print("Open Ports: ")
                for i in sorted(open_ports):
                    service = get_service(i)
                    print("\t%s %s: Open" % (i, service))
            else:
                print("Sorry, No open ports found.!!")

    except KeyboardInterrupt:
        print("You pressed Ctrl+C. Exiting ")
        sys.exit(1)

print("\nScanning completed at %s" % (time.strftime("%I:%M:%S %p")))
ending_time = time.time()
total_time = round(ending_time - starting_time, 1)

if total_time <= 60.0:
    print("Scan Took %s seconds" % (total_time))
else:
    total_time = round(total_time / 60, 1)
    print("Scan Took %s mins" % (total_time))
