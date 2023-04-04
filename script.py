import pyshark
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.size'] = 12
plt.rcParams['figure.autolayout'] = True
plt.rcParams['figure.dpi'] = 250
plt.rcParams['figure.figsize'] = 5, 4

mean = dict()
mean['ipv4'] = []
mean['ipv6'] = []

for capture in ['AppelSonNoVideo.pcapng', 'SonNoVidNotEduroam.pcapng', 'SonVideoNotEduroam.pcapng', 'Appel Son + Vidéo/AppelSonVideo.pcapng']:

    cap = pyshark.FileCapture(capture)
    ipv4 = 0.0
    ipv6 = 0.0
    tot = 0.0

    for packet in cap:
        if 'DNS' in packet:
            """
            ['id', 'flags', 'flags_response', 'flags_opcode', 'flags_truncated', 'flags_recdesired', 'flags_z', 'flags_checkdisable', 
            'count_queries', 'count_answers', 'count_auth_rr', 'count_add_rr', '', 'qry_name', 'qry_name_len', 'count_labels', 'qry_type', 
            'qry_class', 'resp_name', 'resp_type', 'rr_udp_payload_size', 'resp_ext_rcode', 'resp_edns0_version', 'resp_z', 'resp_z_do', 
            'resp_z_reserved', 'resp_len']
            """
            # packet.dns.qry_type --> IPv4 == 1, IPv6 == 28
            if packet.dns.qry_type == '1':
                ipv4 += 1.0
            elif packet.dns.qry_type == '28':
                ipv6 += 1.0
            tot += 1.0

    mean['ipv4'].append(ipv4 / tot)
    mean['ipv6'].append(ipv6 / tot)

    print('\033[94mCapture processed: {}'.format(capture))

mean_ipv4 = sum(mean['ipv4']) / len(mean['ipv4'])
mean_ipv6 = sum(mean['ipv6']) / len(mean['ipv6'])
std_ipv4 = np.std(mean['ipv4'])
std_ipv6 = np.std(mean['ipv6'])
plt.pie([mean_ipv4, mean_ipv6], labels=['IPv4', 'IPv6'], colors=['lightcoral', 'cornflowerblue'], autopct='%1.1f%%')
plt.text(0.7, -1.3, 'Ecart-type IPv4 : {:.3f}\nEcart-type IPv6 : {:.3f}'.format(std_ipv4, std_ipv6), fontsize=10)
plt.show()
