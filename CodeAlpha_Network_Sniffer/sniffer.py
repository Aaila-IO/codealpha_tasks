from scapy.all import sniff
from datetime import datetime

# Mapping protocol numbers to names
PROTOCOLS = {
    1: "ICMP",
    6: "TCP",
    17: "UDP"
}

def analyze_packet(packet):
    try:
        if packet.haslayer("IP"):
            src = packet["IP"].src
            dst = packet["IP"].dst
            proto_num = packet["IP"].proto
            proto = PROTOCOLS.get(proto_num, f"Unknown ({proto_num})")
            time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            print("\n========== PACKET ==========")
            print("Time:", time)
            print("Source IP:", src)
            print("Destination IP:", dst)
            print("Protocol:", proto)

            # Save output to file
            with open("packet_logs.txt", "a") as f:
                f.write(f"{time}  {src}  {dst}  {proto}\n")

            # Extract raw payload if available
            if packet.haslayer("Raw"):
                payload = packet["Raw"].load
                print("Payload:", payload)
            else:
                print("Payload: None")

    except Exception as e:
        print("Error analyzing packet:", e)

# Sniffing on your main interface (ens33)
sniff(prn=analyze_packet, store=False, iface="ens33")

