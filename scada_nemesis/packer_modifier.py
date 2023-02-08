from scapy.layers.inet import IP, UDP
from scapy.layers.modbus import MODBUS

# create a Modbus packet
ip = IP(src='127.0.0.1', dst='127.0.0.1')
udp = UDP(sport=502, dport=502)
modbus = MODBUS(function_code=3, unit=1, data=b'\x00\x01\x00\x02')
packet = ip/udp/modbus

# alter the packet
modbus.data = b'\x00\x02\x00\x04'

# send the altered packet
send(packet)
