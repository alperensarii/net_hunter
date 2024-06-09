import scapy.all as scapy
import optparse


# 1. aşama arp request oluşturmak
# 2. aşama broadcast yapmak
# 4. aşama cevabı işlemek

def range_input():
    parse_object = optparse.OptionParser()
    parse_object.add_option("-i","--ipaddress",dest="ipaddress",help="Enter IP Address")
    (user_input,arguments) = parse_object.parse_args()

    if not user_input.ipaddress:
        print("Please enter an IP Address")

    return user_input

def scan_my_network(ip):
    arp_request_packet = scapy.ARP(pdst=ip)
    # scapy.ls(scapy.ARP()) bilgi almak için ls kullanıyoruz
    broadcast_packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    combined_packet = broadcast_packet / arp_request_packet
    (answered_list, unanswered_list) = scapy.srp(combined_packet, timeout=1)
    answered_list.summary()

user_ip_address = range_input()
scan_my_network(user_ip_address.ip_address)