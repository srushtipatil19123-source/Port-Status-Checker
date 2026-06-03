import socket
host = input("Enter Host/IP Address: ").strip()
port = int(input("Enter Port Number: "))

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2)

    result = s.connect_ex((host, port))

    if result == 0:
        print(f"Port {port} is OPEN on {host}")
    else:
        print(f"Port {port} is CLOSED on {host}")

    s.close()

except socket.gaierror:
    print("Invalid Host/IP Address")
except ValueError:
    print("Please enter a valid port number")