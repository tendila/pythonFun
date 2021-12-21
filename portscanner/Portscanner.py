import socket
from IPy import IP

class Portscan():
    banners = []
    open_ports = []
    
    def __init__(self, target, portnum):
        self.target = target
        self.port_num = portnum
        
    
    def scan(self):
        for port in range(1, int(self.port_num)):
            self.scan_port(port)
        
    def check_ip(self):
        try:
            IP(self.target)
            return(self.target)
        except ValueError:
            return socket.gethostbyname(self.target)
        
    def scan_port(self, port):
        try:
            converted_ip = self.check_ip()
            sock = socket.socket()
            sock.settimeout(0.5)
            sock.connect((converted_ip, port))
            self.open_ports.append(port)
            try:
                banner = sock.recv(1024).decode().strip('\n').strip('\r')
                print("Banner found on port " + port + " : " + banner)
                self.banners.append(banner)
            except: 
                self.banners.append(' ')
            sock.close()
        except:
            pass
    
            
            
    
        