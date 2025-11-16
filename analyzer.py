from scapy.all import sniff

def packet_callback(packet):
    print("\n--- Packet Captured ---")
    if packet.haslayer('IP'):
        print(f"Source IP: {packet['IP'].src}")
        print(f"Destination IP: {packet['IP'].dst}")
    if packet.haslayer('TCP'):
        print("Protocol: TCP")
    elif packet.haslayer('UDP'):
        print("Protocol: UDP")
    elif packet.haslayer('ICMP'):
        print("Protocol: ICMP")

def start_sniffing():
    sniff(prn=packet_callback, store=False)
