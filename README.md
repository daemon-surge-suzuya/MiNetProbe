# MiNetProbe
Welcome to MiNetProbe, an exclusive compilation of personally crafted networking scripts. 
Originally, this project included ICMP, UDP, and SYN flooder scripts, alongside an open port scanner. These scripts use raw sockets.

At its core, the MiNetProbe Project is designed to test network connectivity, measure network performance, 
and conduct basic network diagnostics. However, it's vital to underscore that the power wielded by MiNetProbe comes 
with the responsibility of ethical usage and proper authorization. Employ it conscientiously within controlled environments 
for legitimate and justifiable purposes. Remember, the misuse of this tool can have far-reaching legal and ethical repercussions.

# ICMP Packet Sender

- The ICMP packet sender utilizes raw sockets to send ICMP (ping) packets to the target IP address.
- Users can specify the number of packets they want to send in a continuous loop
- The payload size of the ICMP packets can be adjusted to test various packet sizes.

# UDP Packet Sender

- The UDP packet sender uses Datagram (UDP) sockets to send UDP packets to the target IP and port.
- Users can specify the number of packets they want to send in a continuous loop.
- The payload size of the UDP packets can be adjusted to test different data sizes.

# SYN Packet Sender

- The SYN packet sender uses raw sockets to send TCP SYN packets to the target IP and port.
- Users can specify the number of SYN packets they want to send in a continuous loop.
- SYN packets do not carry payloads, so there is no payload size adjustment.

# Open Port Scanner

- The Open Port Scanner script employs asynchronous connections to swiftly identify open ports on a target system
- Users can specify the range of ports to scan and receive insights into discovered services. 
- Equips you with the ability to identify the exact service running on each open port detected.

# Resource Management 

- Concurrent Socket Pooling: All scripts create a pool of sockets to optimize concurrent packet sending, enhancing performance.
- Socket Closure: Sockets are systematically closed after packet transmission, preventing resource leakage and ensuring efficient usage.
- Resource Allocation: Through efficient socket handling, the scripts maintain optimal resource allocation, minimizing potential bottlenecks.


