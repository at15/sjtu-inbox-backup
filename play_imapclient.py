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

# Select the INBOX folder
inbox = server.select_folder('INBOX')
# FIXME: why not 'EXISTS'
print("%d messages in INBOX folder " % inbox[b'EXISTS'])
messages = server.search(['NOT', 'DELETED'])
print("%d messages that aren't deleted" % len(messages))
# messages is an array of message_id
print(type(messages[0]))  # <class 'int'>
# get the first message
first_message = messages[0]
# TODO: how to fetch the parsed body, contact and attachments
response = server.fetch([first_message], ["INTERNALDATE", "BODY", "RFC822", "ENVELOPE"])
# NOTE: the example in doc use iteritems() while py3 use items()
print(response)
for message_id, data in response.items():
    print("message ID: %d" % message_id)
    print(data[b"RFC822"])
    print(data[b"BODY"])
    print(data[b"ENVELOPE"])
    # TODO: show the string, it's now b'=?utf-8?B?6JGh6JCE572R56uZ6YKA6K+35Ye9?='
    print(data[b"ENVELOPE"].subject)

# Logout
print(server.logout())
