import pyshark 
from datetime import timedelta
import matplotlib.pyplot as plt

plt.rcParams["mathtext.fontset"] = 'cm'
plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['font.size'] = 13
plt.rcParams['axes.axisbelow'] = True
plt.rcParams['figure.autolayout'] = True
plt.rcParams['figure.dpi'] = 250

time_array = []
bytes_array = []

for files in ['Traces/bytesVideo.pcapng', 'Traces/bytesAudio.pcapng']:
    cap = pyshark.FileCapture(files)
    tot_bytes = 0

    ref = cap[0].sniff_time
    start = cap[0].sniff_time
    bytes = []
    time = []
    for packet in cap:
        tot_bytes += packet.__len__()
        if (packet.sniff_time - start) >= timedelta(seconds=1):
            bytes.append(tot_bytes)
            time.append((packet.sniff_time - ref).total_seconds())
            tot_bytes = 0
            start = packet.sniff_time

    time_array.append(time)
    bytes_array.append(bytes)

    print('\033[94mCapture processed: {}'.format(files))

for i in range(len(bytes_array)):
    bytes_array[i] = [b/1000 for b in bytes_array[i]] # Bytes to KBytes
plt.hlines(640, time_array[0][0], time_array[0][-1], color='lightsteelblue', linestyles='dashed', label='640 KBytes/s')
plt.hlines(20, time_array[1][0], time_array[1][-1], color='burlywood', linestyles='dashed', label='20 KBytes/s')
plt.plot(time_array[0], bytes_array[0], label='Appel Audio + Vidéo', color='cornflowerblue')
plt.plot(time_array[1], bytes_array[1], label='Appel Audio', color='peru')
plt.xlabel('Temps (s)')
plt.ylabel('Nombre de KBytes échangés')
plt.grid(color="lightgray")
plt.legend(loc="best")
plt.show()