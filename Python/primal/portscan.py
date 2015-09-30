import os, socket, sys

ip = sys.argv[1]
startPort = sys.argv[2]
endPort = sys.argv[3]

s = socket.socket()

for port in range(int(startPort), int(endPort)):
    try:
        print "[+] Attempting to connect to " + str(ip) + ":" + str(port)
        s.connect((str(ip), port))
        s.send("GET \n")
        banner = s.recv(1024)
        if banner:
            print "[+] Port " + str(port) + " open: " + str(banner)
        s.close()
    except: pass
