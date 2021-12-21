import Portscanner

targets_ip = input("[+] Enter target to scan for vulnerable open ports: ")
port_number = input("[+] Enter amount of port to scan (500 - first 500 ports)")
vul_file = input("[+] Enter the path to the file with vulnerable softwares :")
print('\n')


target = Portscanner.Portscan(targets_ip, port_number)
target.scan()

with open(vul_file, 'r') as file:
    count = 0
    for banner in target.banners:
        file.seek(0)
        for line in file.readlines():
            if line.strip() in banner:
                print('[!!] Vulnerable banner : "' + banner + '" on port ' + str(target.open_port))
            #else: print('Nop')
        count+= 1

print("[#] Total open ports (over the " + port_number + " scanned): " + str(len(target.banners)))

print(target.banners)