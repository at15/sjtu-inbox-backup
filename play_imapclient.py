from __future__ import unicode_literals
import json
from imapclient import IMAPClient

# Load user credentials from JSON
with open('config.json', 'r') as configFile:
    config = json.loads(configFile.read())

# Login
HOST = 'mail.sjtu.edu.cn'
USERNAME = config['name']
PASSWORD = config['password']
# FIXME: got OpenSSL.Error if enabled, however imbox seems to work fine with ssl
ssl = False

server = IMAPClient(HOST, use_uid=True, ssl=ssl)
server.login(USERNAME, PASSWORD)

# List all the folders
folders = server.list_folders()
# print(folders)
for folder in folders:
    print(folder)

inbox = server.select_folder('INBOX')
for k in inbox:
    print(k)
    print(inbox[k])

# FIXME: why not 'EXISTS'
print("%d messages in INBOX folder " % inbox[b'EXISTS'])

messages = server.search(['NOT', 'DELETED'])
print("%d messages that aren't deleted" % len(messages))

# messages is an array of message_id
print(type(messages[0]))  # <class 'int'>
for message in messages:
    print(message)

# get the first message
first_message = messages[0]
# TODO: how to fetch the parsed body, contact and attachments
response = server.fetch([first_message], ['RFC822'])

# NOTE: the example in doc use iteritems() while py3 use items()
for message_id, data in response.items():
    print(message_id)
    print(data)

print(server.logout())
