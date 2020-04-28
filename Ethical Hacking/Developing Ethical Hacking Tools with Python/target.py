import nmap
import sys
from pprint import pprint
import time

# Compu: '192.168.0.106'
# Celu: '192.168.0.100'
nm_scan = nmap.PortScanner()
print('\nRunning...\n')
nm_scanner = nm_scan.scan(sys.argv[1], '80', arguments='-O')
pprint(nm_scanner)
try:
    host_is_up = "The host is: " +  nm_scanner['scan'][sys.argv[1]]['status']['state'] + "\n"
    host_mac = "The MAC of the devise is: " + nm_scanner['scan'][sys.argv[1]]['addresses']['mac'] + "\n"
    method_scan = "The method of scanning is: " + nm_scanner['scan'][sys.argv[1]]['tcp'][80]['reason'] + "\n"
    with open("%s.txt"%sys.argv[2], 'a+') as f:
        f.write(host_is_up + host_mac + method_scan)
        f.write("\nReport generated " + time.strftime("%d-%m-%Y   %H:%M:%S GMT\n\n\n", time.gmtime()))
except:
    print("Hubo un error")
finally:
    print("\nFinished...")
