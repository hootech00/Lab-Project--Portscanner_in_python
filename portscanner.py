import pyfiglet
import socket
import subprocess
import sys
from datetime import datetime

#Blank your screen
subprocess.call('clear', shell=True)

#Ask for input
remoteServer = input("Enter a remote hostname or IP to scan: ")
remoteServerIP = socket.gethostbyname(remoteServer)

#Print a nice banner with information on which host we are about to scan
print("=" * 60)
print("Please wait, scaning remote host, remoteServerIP")
print("Please CTRL+C to cancel")
print("+" * 60)

#Check the date and the time the scan was started
t1 = datetime.now()

#Using the range function specify ports.
#Also we will do error handling

try:
    for port in range (1,5000):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((remoteServerIP, port))
        if result == 0:
            print("Port {}:     Open".format(port))
        sock.close()

except KeyboardInterrupt:
    print("You pressed Ctrl+C to end port scanning")
    sys.exit()

except socket.gaierror:
    print("Error - Could not resolve hostname.")
    sys.exit()

except socket.error:
    print("Error - Couldn't connect to server")
    sys.exit()
