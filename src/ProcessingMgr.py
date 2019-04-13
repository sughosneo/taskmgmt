'''
    This script would actually be responsible to process each email row.
'''

import email
import csv
import pandas as pd

class ProcessingMgr:

    def __init__(self):
        pass

    def loadEmailCSV(self,fileName):

        try:


            with open(fileName,"r") as f:

                reader = csv.reader(f, delimiter="\t")

                for i,line in enumerate(reader):

                    if not (i ==0) and line:

                        #print('line[{}] = {}'.format(i, line[0]))

                        message = email.message_from_string(line[0])

                        if message :

                            subject = message.get("Subject") if message.get("Subject") else "NA"
                            to_email = message.get("To") if message.get("To") else "NA"
                            from_email = message.get("From") if message.get("From") else "NA"
                            cc_email = message.get("Cc") if message.get("Cc") else "NA"
                            bcc_email = message.get("Bcc") if message.get("Bcc") else "NA"
                            messageId = message.get("Message-ID") if message.get("Message-ID") else "NA"
                            payload = message.get_payload(decode=True) if message.get_payload(decode=True) else "NA"

                            messageDict = {'subject': subject,
                                    'to': to_email,
                                    'from': from_email,
                                    'cc': cc_email,
                                    'bcc': bcc_email,
                                    'message_id': messageId,
                                    'payload': payload}

                            yield messageDict


        except Exception as error:
            print("[Error]:", str(error))

# if __name__ == '__main__':
#
#     processMgr = ProcessingMgr()
#     message = processMgr.loadEmailCSV("D:\\projects\\taskmgmt\\data\\emails.csv")
#     print(message)