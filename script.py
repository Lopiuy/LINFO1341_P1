import pyshark
import pandas as pd
import matplotlib.pyplot as plt

cap = pyshark.FileCapture('AppelSonNoVideo.pcapng')

dns_types = []
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
            dns_types.append('IPv4')
        elif packet.dns.qry_type == '28':
            dns_types.append('IPv6')
        print(packet.dns.resp_z_do)

dns_df = pd.DataFrame({'type': dns_types})

dns_count = dns_df.groupby('type').size().reset_index(name='counts')

plt.pie(dns_count.counts, labels=dns_count.type, autopct='%1.1f%%')
plt.title('Types d\'adresses IP résolus par DNS')
plt.show()
