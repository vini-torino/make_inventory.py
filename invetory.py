import subprocess
from re import findall 

def main():
    batman = Computer('batman')
    print(batman.get_hostname())
    print(batman.is_up())
    batman.set_hostname('hulkbuster')
    print(batman.get_hostname())
    help(Computer)

class Computer():
    """The Computer class stores data related to network, operating and activy of a machine"""
    def __init__(self, hostname, ipv4=None, mac_address=None, os=None, model=None ):
        self.hostname = hostname
        self.ipv4 = ipv4
        self.mac_address = mac_address 
        self.os = os
        self.model = model

    def get_hostname(self):
        """Returns current hostname"""
        return self.hostname

    def set_hostname(self, hostname):
        """Sets new hostname"""
        self.hostname = hostname

    def get_ipv4(self):
        """Returns current ipv4"""
        return self.ipv4

    def set_ipv4(self, ipv4):
        """Sets new ipv4"""
        self.ipv4 = ipv4
    
    def get_mac_address(self):
        """Returns current mac_address"""
        return self.mac_address

    def set_mac_address(self, mac_address):
        """Sets fake mac address on top of macchanger utilily, may not work on all networks, and it is only implemented on Linux hosts"""
        self.mac_address = mac_address
    
    def get_os(self):
        """Returns Operating System"""
        return self.os

    def set_os(self, os):
        """Sets or Modifies current Operating System if necessary"""
        self.os = os 

    def get_model(self):
        """Returns current machine model""" 
        return self.model

    def set_model(self, model):
        """Sets or modifies current machine model if necessary"""
        self.model = model

    def is_up(self):
        """Test is a machine is up and running"""  
        if self.ipv4 is not None:
            output =  subprocess.run(['ping', '-c1', self.ipv4], stdout=subprocess.PIPE).stdout.decode().rstrip()
        else:
            output =  subprocess.run(['ping', '-c1', self.hostname], stdout=subprocess.PIPE).stdout.decode().rstrip() 
        array = findall('1 received, 0% packet loss', output)
        if array[0]:
            return True
        return False


main()
