import subprocess


def main():
    batman = Computer('batman')
    print(batman.get_hostname())
    print(batman.ping())
    batman.set_hostname('hulkbuster')
    print(batman.get_hostname())


class Computer():
    def __init__(self, hostname, ipv4=None, mac_address=None, os=None, model=None ):
        self.hostname = hostname
        self.ipv4 = ipv4
        self.mac_address = mac_address 
        self.os = os
        self.model = model

    def get_hostname(self):
        return self.hostname

    def set_hostname(self, hostname):
        self.hostname = hostname

    def get_ipv4(self):
        return self.ipv4

    def set_ipv4(self, ipv4):
        self.ipv4 = ipv4
    
    def get_mac_address(self):
        return self.mac_address

    def set_mac_address(self, mac_address):
        self.mac_address = mac_address
    
    def get_os(self):
        return self.os

    def set_os(self, os):
        self.os = os 

    def get_model(self):
        return self.model

    def set_model(self, model):
        self.model = model

    def ping(self):
        if self.ipv4 is not None:
            return subprocess.run(['ping', '-c1', self.ipv4], stdout=subprocess.PIPE).stdout.decode().rstrip()
        return subprocess.run(['ping', '-c1', self.hostname], stdout=subprocess.PIPE).stdout.decode().rstrip() 

main()
