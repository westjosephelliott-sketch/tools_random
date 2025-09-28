#ai_recon_agent
import subprocess
import socket
import json

class Recon_Agent:
    def __init__(self, target):
        self.target = target
        self.report = {}
    def subdomains(self):
        result = subprocess.getoutput(f"subfinder -d {self.target}")
        self.report["subdomains"] = result.splitlines()
    def ports(self):
        scan = subprocess.getoutput(f"nmap -Pn -p- {self.target}")
        self.report["ports"] = scan
    def fingerprint(self):
        try:
            banner = socket.gethostbyname(self.target)
            self.report["fingerprint"] = banner
        except:
            self.report["fingerprint"] = "unresolved"

    def export(self):
        print(json.dumps(self.report, indent=2))
        


if __name__ == "__main__":
    agent = Recon_Agent("") #Enter target
    agent.subdomains()
    agent.ports()
    agent.fingerprint()
    agent.export()