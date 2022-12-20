from collections import Counter
import matplotlib.pyplot as plt
file = open("NASA_access_log_Jul95")
 
ip_addresses = []

try:
     for line  in file:
        ip_addresses.append(line.split(" ")[0])
except:
        print("uh-oh")


print(ip_addresses)

ip_adresses_counter = Counter(ip_addresses)


print(ip_adresses_counter.keys())
print(ip_adresses_counter.values())

plt.bar(ip_addresses.keys()), (ip_addresses.values())

plt.show()