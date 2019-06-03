import subprocess
import json

cmd = "tshark -T json -r DESKTOP-AK8ARRP_20190603_144850.pcapng"
sub = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
str1 = sub.stdout.read()
sub.communicate()
str1 = str1.decode()
print type(str1)
with open('test.txt', 'w') as f:
    f.write(str1)
f.close()