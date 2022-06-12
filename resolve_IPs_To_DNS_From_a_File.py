import re
import dns.resolver


with open("ips.txt" , 'r') as f:
   ips = f.readlines()

 
pattern = re.compile("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}[^ \n]")
matches = [match[:12] for match in ips if pattern.findall(match)]
removetable = str.maketrans('', '', ':')
out_list = [s.translate(removetable) for s in matches]

try:
 for ip in out_list:
     for rdata in dns.resolver.resolve_address(ip):
         print (rdata.target)
except:
    pass