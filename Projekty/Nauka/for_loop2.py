import socket
import ipaddress


def is_port_open(ip: str,port: int) -> bool:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(2)
    result = sock.connect_ex((ip,port))
    return result == 0

ports = [
    80,
    443
]

for ip in ipaddress.ip_network('192.168.178.0/24'):
    print(f'sprawdzam adress ip {ip}')
    for port in ports:
        if is_port_open(str(ip),port):
            print(f'adress ip {ip} ma otwarty {port}')
