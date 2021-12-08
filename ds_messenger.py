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

class DirectMessage:
  def __init__(self):
    self.recipient = None
    self.message = None
    self.timestamp = None

class DirectMessenger:
  def __init__(self, dsuserver=None, username=None, password=None):
    self.dsuserver = dsuserver
    self.username = username
    self.password = password
    self.token = None


  def join(self, dsuserver, username, password) -> str:
     with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client: # opening socket stream
      client.connect((server, port)) # connects to server and port passed to send function
    
      send = client.makefile('w') # to send
      recv = client.makefile('r') # to receive responses

      print('client connected to', server,'on', port) 

      json_msg = '{"join": {"username": "unittestwork" ,"password": "hellowrodl1223", "token": ""}}'
              
      send.write(json_msg + '\r\n')
      send.flush() #cant leave anything behind 

      respo = recv.readline()
      
      dm = DirectMessenger()
      dm.token = part1_protocol.extract_json(respo)[0]

      return dm.token
  

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
        direct_msg = '{"token": "' + dm.token + '", "directmessage": {"entry":"' + self.message + '", "recipient": "' + self.recipient + '", "timestamp": "' + str(self.timestamp) + '"}}' # posts user's desired message
        response = True
        send.write(direct_msg + '\r\n')
        send.flush() #cant leave anything behind 
      except:
        response = False
      finally:
        respo = recv.readline()

      return response
    
		
  def retrieve_new(self) -> list:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client: # opening socket stream
      client.connect((server, port)) # connects to server and port passed to send function
    
      send = client.makefile('w') # to send
      recv = client.makefile('r') # to receive responses

      print('client connected to', server,'on', port) 
    # returns a list of DirectMessage objects containing all new messages
      new_msg = '{"token": "' + dm.token + '", "directmessage": "new" }'
      send.write(new_msg + '\r\n')
      send.flush() #cant leave anything behind 
      respo = recv.readline()
      stringthing = part1_protocol.extract_json(respo)

      return stringthing

  def retrieve_all(self) -> list:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client: # opening socket stream
      client.connect((server, port)) # connects to server and port passed to send function
    
      send = client.makefile('w') # to send
      recv = client.makefile('r') # to receive responses

      print('client connected to', server,'on', port) 
    # returns a list of DirectMessage objects containing all messages
      all_msg = '{"token": "' + dm.token + '", "directmessage": "all" }'
      send.write(all_msg + '\r\n')
      send.flush() #cant leave anything behind 
      respo = recv.readline()
      stringything = part1_protocol.extract_json(respo)
    
      return stringything[1]

#--------------------------- commands to call these functions -----------------------------------#

dm = DirectMessenger(dsuserver=server, username="unittest123", password="passwrod1234")
dm.token = DirectMessenger.join(DirectMessenger, server, dm.username, dm.password) 
#DirectMessenger.send(DirectMessenger, "Whats up man", dm.username)
#DirectMessenger.retrieve_all(DirectMessenger)
# DirectMessenger.retrieve_new(DirectMessenger)

# To do:
# First populate DirectMessenger class with username, dsuserver, and password
# Call join function to collect token and populate DirectMessenger token attribute
# Now you have access to using the send, retrieve_all, and retrieve_new functions
# I recommend retrieving all messages to display on the GUI and to add new messages to the user's dsu file
# To call send function you need a message and the username of the person you're sending to 