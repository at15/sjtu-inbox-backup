# Use https://github.com/martinrusev/imbox as IMAP Client
from imbox import Imbox
import json

# Load user credentials from JSON
with open('config.json', 'r') as configFile:
    config = json.loads(configFile.read())
    print(config['name'])

# Open inbox
imbox = Imbox('mail.sjtu.edu.cn',
              username=config['name'],
              password=config['password'],
              ssl=True,
              ssl_context=None)

# Gets all messages
all_messages = imbox.messages()

for uid, message in all_messages:
    # FIXME: UnicodeDecodeError: 'utf-8' codec can't decode byte 0xc4 in position 1821: invalid continuation byte
    print(message)
