# Starter code for assignment 3 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Sona Keshishyan
# sonak1@uci.edu
# 94639158

import socket
import json
import Profile
import part1_protocol
import ds_messenger

port = 3021
server = "168.235.86.101"
all_msg1 = []
new_msg1 = []

class DirectMessage:
  def __init__(self):
    self.recipient = None
    self.message = None
    self.timestamp = None

class DirectMessenger:
  def __init__(self, dsuserver=None, username=None, password=None):
    self.token = None
		
  def send(self, message:str, recipient:str) -> bool:
    # returns true if message successfully sent, false if send failed.
    self.recipient = recipient
    self.message = message
    self.timestamp = Profile.time.time()
    direct_msg = '{"token": "31292afb-8505-4421-b112-e18bc0938642", "directmessage": {"entry":"' + self.message + '", "recipient": "' + self.recipient + '", "timestamp": "' + str(self.timestamp) + '"}}' # posts user's desired message
    send.write(direct_msg + '\r\n')
    send.flush() #cant leave anything behind 
    respo = recv.readline()
    
		
  def retrieve_new(self) -> list:
    # returns a list of DirectMessage objects containing all new messages
    new_msg = '{"token": "31292afb-8505-4421-b112-e18bc0938642", "directmessage": "new" }'
    send.write(new_msg + '\r\n')
    send.flush() #cant leave anything behind 
    respo = recv.readline()
    new_msg1.append(respo)
    
    return new_msg1

  def retrieve_all(self) -> list:
    # returns a list of DirectMessage objects containing all messages
    all_msg = '{"token": "31292afb-8505-4421-b112-e18bc0938642", "directmessage": "all" }'
    send.write(all_msg + '\r\n')
    send.flush() #cant leave anything behind 
    respo = recv.readline()
    all_msg1.append(respo)
    
    return all_msg1


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client: # opening socket stream
    client.connect((server, port)) # connects to server and port passed to send function
    
    send = client.makefile('w') # to send
    recv = client.makefile('r') # to receive responses

    print('client connected to', server,'on', port) # confirmation to user

    while True:
      json_msg = '{"join": {"username": "unittestwork" ,"password": "hellowrodl1223", "token": ""}}' 
        
      send.write(json_msg + '\r\n')
      send.flush() #cant leave anything behind 

      respo = recv.readline()
      print(respo)

      #new_token = part1_protocol.extract_json(respo)[0] # grabs token from join response

      print(DirectMessenger.retrieve_all(DirectMessenger))
      print(DirectMessenger.retrieve_new(DirectMessenger))

      break