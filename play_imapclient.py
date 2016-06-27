from __future__ import unicode_literals
import json
from imapclient import IMAPClient

# Load user credentials from JSON
with open('config.json', 'r') as configFile:
    config = json.loads(configFile.read())

HOST = 'mail.sjtu.edu.cn'
USERNAME = config['name']
PASSWORD = config['password']
# FIXME: got OpenSSL.Error if enabled, however imbox seems to work fine with ssl
ssl = False

server = IMAPClient(HOST, use_uid=True, ssl=ssl)
server.login(USERNAME, PASSWORD)

folders = server.list_folders()
# print(folders)
for folder in folders:
    print(folder)

inbox = server.select_folder('INBOX')
for k in inbox:
    print(k)
    print(inbox[k])

# FIXME: why no 'EXISTS'
print(inbox[b'EXISTS'])
