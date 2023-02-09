from scapy.all import *


def packet_callback(packet):
    if packet.haslayer(MODBUS):
        print(packet.show())


sniff(prn=packet_callback, filter='tcp port 502', iface='lo', store=0)
