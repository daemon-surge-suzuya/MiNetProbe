import socket
import asyncio
import time

async def scan_port(args):
    target, port = args
    try:
        reader, writer = await asyncio.open_connection(target, port)
        writer.close()
        await writer.wait_closed()
        return port
    except:
        return None

async def get_service_banner(result):
    port, target = result
    try:
        reader, writer = await asyncio.open_connection(target, port)
        banner = await reader.read(1024)
        return port, banner.decode('utf-8').strip()
    except:
        return port, "Unknown"

async def main():
    target = input("Enter the IP address or domain name you want to scan: ")
    start_port = int(input("Enter the starting port for scanning: "))
    end_port = int(input("Enter the ending port for scanning: "))

    print(f"Scanning ports on {target}...\n")

    open_ports = []
    target_ports = [(target, port) for port in range(start_port, end_port + 1)]
    batch_size = 100

    start_time = time.time()

    tasks = [scan_port(target_port) for target_port in target_ports]
    scan_results = await asyncio.gather(*tasks)

    open_ports = [result for result in scan_results if result is not None]

    tasks = [get_service_banner((port, target)) for port in open_ports]
    service_banners = await asyncio.gather(*tasks)

    end_time = time.time()

    print("\nScan complete!\n")

    if open_ports:
        print("Open ports discovered:")
        for port, banner in service_banners:
            print(f"Port {port} - Service: {banner}")
    else:
        print("No open ports found.")

    total_scan_time = end_time - start_time
    print(f"\nTotal scan time: {total_scan_time:.4f} seconds")

if __name__ == "__main__":
    asyncio.run(main())

