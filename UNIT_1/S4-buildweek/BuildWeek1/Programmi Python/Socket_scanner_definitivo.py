import socket
import struct

# RAW SOCKET in modalità promiscua
# AF_PACKET = livello Ethernet (solo Linux)
# SOCK_RAW = pacchetti grezzi
# ntohs(3) = protocollo "tutti i protocolli"
sniffer = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))

print("Sniffer attivo in modalità promiscua...\n")

while True:
    raw_data, addr = sniffer.recvfrom(65535)

    # Header Ethernet: 14 byte
    dest_mac, src_mac, proto = struct.unpack('!6s6sH', raw_data[:14])

    # Conversione MAC in formato leggibile
    dest_mac = ':'.join('%02x' % b for b in dest_mac)
    src_mac = ':'.join('%02x' % b for b in src_mac)

    print(f"Pacchetto catturato:")
    print(f"  MAC sorgente:      {src_mac}")
    print(f"  MAC destinazione:  {dest_mac}")
    print(f"  Protocollo:        {hex(proto)}")
    print(f"  Lunghezza:         {len(raw_data)} bytes\n")