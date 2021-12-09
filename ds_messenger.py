# Starter code for assignment 3 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Sona Keshishyan
# sonak1@uci.edu
# 94639158

import socket
import json
import Profile
import part1_protocol

port = 3021
server = "168.235.86.101" #dsu server is hardcoded rn but it shouldnt be 

"""Handles the Direct message class for message objects."""
class DirectMessage:
  def __init__(self):
    self.recipient = None
    self.message = None
    self.timestamp = None

"""Handles the DirectMessenger class for sending and recieve messages across the server."""
class DirectMessenger:
  def __init__(self, dsuserver="168.235.86.101", username=None, password=None):
    self.dsuserver = dsuserver
    self.username = username
    self.password = password
    self.token = None


  def join(self) -> str:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client: # opening socket stream
      client.connect((server, port)) # connects to server and port passed to send function
    
      send = client.makefile('w') # to send
      recv = client.makefile('r') # to receive responses

      print('client connected to', server,'on', port) 

      json_msg = f'{{"join": {{"username": "{self.username}","password": "{self.password}", "token": ""}}}}'
              
      send.write(json_msg + '\r\n')
      send.flush() #cant leave anything behind 

      respo = recv.readline()
      
      return part1_protocol.extract_json(respo)[0]
  
  """"Sending the message to the recipient over the server."""
  def send(self, message:str, recipient:str) -> bool:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client: # opening socket stream
      client.connect((server, port)) # connects to server and port passed to send function
    
      send = client.makefile('w') # to send
      recv = client.makefile('r') # to receive responses

      print('client connected to', server,'on', port) 
    # returns true if message successfully sent, false if send failed.
      self.recipient = recipient
      self.message = message
      self.timestamp = Profile.time.time()
      
      try:
        direct_msg = '{"token": "' + self.token + '", "directmessage": {"entry":"' + self.message + '", "recipient": "' + self.recipient + '", "timestamp": "' + str(self.timestamp) + '"}}' # posts user's desired message
        response = True
        send.write(direct_msg + '\r\n')
        send.flush() #cant leave anything behind 
      except:
        response = False
      finally:
        respo = recv.readline()

      return response
    
  """Retrieving new messages from the server."""
  def retrieve_new(self) -> list:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client: # opening socket stream
      client.connect((server, port)) # connects to server and port passed to send function
    
      send = client.makefile('w') # to send
      recv = client.makefile('r') # to receive responses

      print('client connected to', server,'on', port) 
    # returns a list of DirectMessage objects containing all new messages
      new_msg = '{"token": "' + self.token + '", "directmessage": "new" }'
      send.write(new_msg + '\r\n')
      send.flush() #cant leave anything behind 
      respo = recv.readline()
      stringthing = part1_protocol.extract_json(respo)

      return stringthing

  """Retrieving ALL messages from the server."""
  def retrieve_all(self) -> list:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client: # opening socket stream
      client.connect((server, port)) # connects to server and port passed to send function
    
      send = client.makefile('w') # to send
      recv = client.makefile('r') # to receive responses

      print('client connected to', server,'on', port) 
    # returns a list of DirectMessage objects containing all messages
      all_msg = '{"token": "' + self.token + '", "directmessage": "all" }'
      send.write(all_msg + '\r\n')
      send.flush() #cant leave anything behind 
      respo = recv.readline()
      stringything = part1_protocol.extract_json(respo)
    
      return stringything[1]

#--------------------------- commands to call these functions -----------------------------------#

#dm = DirectMessenger(dsuserver=server, username="unittest123", password="passwrod1234")
#dm.token = DirectMessenger.join(DirectMessenger, server, dm.username, dm.password) 