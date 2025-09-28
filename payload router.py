#Encrypted payload router with decoy injections.
import base64
import random
from cryptography.fernet import Fernet

class Payload_Router:
    def __init__(self, payload, decoys):
        self.key = Fernet.generate_key()
        self.fernet = Fernet(self.key)
        self.payload = payload
        self.decoys = decoys

    def encrypt(self):
        encrypted = self.fernet.encrypt(self.payload.encode())
        return encrypted

    def inject(self):
        stream = [self.fernet.encrypt(d.encode()) for d in self.decoys]
        stream.insert(random.randint(0, len(stream)), self.encrypt())
        return stream

    def export(self):
        for packet in self.inject():
            print(base64.b85encode(packet).decode())

        if __name__ == "__main__":
            router = Payload_Router("launch://core", ["ping://null", "echo://ghost", "trace://decoy"])
            router.export()