import os
from typing import List
import json
from config import *

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


class EmailAddress:
    def __init__(self, local_part: str, domain: str):
        self.local_part = local_part
        self.domain = domain

    def get(self)->str:
        return self.local_part + '@' + self.domain

    def __str__(self):
        return self.get()

class Outputter:
    def __init__(self, email_addresses: list):
        self.email_addresses = email_addresses

    def JSON(self):
        data = []
        for index, address in enumerate(self.email_addresses):
            item = {index: address.get()}
            data.append(item)

        return json.dumps(data)

    def ToTxt(self):
        pass

    def ToCSV(self):
        pass

    def Message(self) -> str:
        msg = f"{len(self.email_addresses)} e-mail address"
        if(len(self.email_addresses) > 1):
            msg += "es"
        
        return "Outputter has " + msg + "."

def generator():
    
    addresses = []

    for domain in domains:
        for lp in local_parts:
            mail = EmailAddress(lp, domain)
            addresses.append(mail)
    
    return addresses

if __name__ == '__main__':
    print("main called")

    addresses = generator()
    out = Outputter(addresses)

    print(out.JSON())
    print(out.Message())
