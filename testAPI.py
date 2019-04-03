import subprocess
cmd = "curl -XGET -i -H 'accept-encoding: application/json' http://10.10.10.100:8000/api/search\?vertexType\=malware"
sub = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
sub.wait()
print sub.stdout.read()