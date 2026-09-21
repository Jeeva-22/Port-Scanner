import socket
import sys
from datetime import datetime

# Define our target
if len(sys.argv) == 2:
    # Translate hostname to IPv4
    target = socket.gethostbyname(sys.argv[1]) 
else:
    print("Invalid amount of arguments.")
    print("Syntax: python scanner.py <ip>")
    sys.exit()

# Add a pretty banner
print("-" * 50)
print(f"Scanning target: {target}")
print(f"Time started: {str(datetime.now())}")
print("-" * 50)

try:
    # Scan ports between 1 and 1024
    for port in range(1, 1025):
        # AF_INET is IPv4, SOCK_STREAM is TCP [cite: topic-1.1.8]
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1) # 1 second timeout [cite: topic-1.1.4]
        
        # connect_ex returns 0 if successful [cite: topic-1.1.8]
        result = s.connect_ex((target, port))
        if result == 0:
            print(f"Port {port} is open")
        s.close()

except KeyboardInterrupt:
    print("\nExiting program.")
    sys.exit()
except socket.gaierror:
    print("Hostname could not be resolved.")
    sys.exit()
except socket.error:
    print("Could not connect to server.")
    sys.exit()