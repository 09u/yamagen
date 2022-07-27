import os
from typing import List
import json
import csv
from src.yamagen.config import DOMAINS, LOCAL_PARTS, CONFIG_OUTPUT


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
        # mode). It can be None, '', '\n', '\r', and '\r\n'.
        file_name = CONFIG_OUTPUT['direction'] + '/' + CONFIG_OUTPUT['file-name']+'.csv' 
        file_to_output = open(file_name,'w',newline='')
        csv_writer = csv.writer(file_to_output,delimiter=',')
        csv_writer.writerow(['index','domain','email-address'])

        for index, address in enumerate(self.email_addresses):
            csv_writer.writerow([index, address.domain, address.get()])

        file_to_output.close()

    def Message(self) -> str:
        msg = f"{len(self.email_addresses)} e-mail address"
        if(len(self.email_addresses) > 1):
            msg += "es"
        
        return "Outputter has " + msg + "."


class yamagen:
    def __init__(self):
        self.name = ""

    def generator(self):
        
        addresses = []

        for domain in DOMAINS:
            for lp in LOCAL_PARTS:
                mail = EmailAddress(lp, domain)
                addresses.append(mail)
        
        return addresses


if __name__ == '__main__':
    print("main called")
    yamagen = yamagen()

    addresses = yamagen.generator()
    out = Outputter(addresses)
    out.ToCSV()
    print(out.JSON())
    print(out.Message())
