file = open("NASA_access_log_Jul95")
 
ip_addresses = []

try:
     for line  in file:
        ip_addresses.append(line.split(" ")[0])
except:
        print("uh-oh")


print(ip_addresses)