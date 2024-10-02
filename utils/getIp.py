import socket

def get_ipv4_address():
    hostname = socket.gethostname()  # Get the hostname of the machine
    ipv4_address = socket.gethostbyname(hostname)  # Get the IPv4 address using the hostname
    return ipv4_address