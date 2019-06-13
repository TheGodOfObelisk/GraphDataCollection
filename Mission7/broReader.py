import subprocess

cmd = "awk '/^[^#]/ {print $1, $2, $3, $4, $5, $6, $7, $8}' host-info.log"
sub = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
str1 = sub.stdout.read()
sub.communicate()
str1 = str1.decode()
print str1