# Starter code for assignment 3 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Sona Keshishyan
# sonak1@uci.edu
# 94639158

import socket
import part1_protocol
import json
import Profile



def send(server:str, port:int, username:str, password:str, message:str, bio:str=None):
  '''
  The send function joins a ds server and sends a message, bio, or both

  :param server: The ip address for the ICS 32 DS server.
  :param port: The port where the ICS 32 DS server is accepting connections.
  :param username: The user name to be assigned to the message.
  :param password: The password associated with the username.
  :param message: The message to be sent to the server.
  :param bio: Optional, a bio for the user.
  '''
  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client: # opening socket stream
    client.connect((server, port)) # connects to server and port passed to send function
    
    send = client.makefile('w') # to send
    recv = client.makefile('r') # to receive responses

    print('client connected to', server,'on', port) # confirmation to user

    # for json to use variables instead of actual hard-coded values, do this format: "' + str(variable) + '"

    while True:
      json_msg = '{"join": {"username": "' + username + '" ,"password": "' + password + '", "token": ""}}' # join message must always join before posting
      
      send.write(json_msg + '\r\n')
      send.flush() #cant leave anything behind 

      respo = recv.readline()

      new_token = part1_protocol.extract_json(respo).token # grabs token from join response

      if bio != None: # posts bio to post if user has bio
        bio_1 = bio_function(bio, new_token)

        send.write(bio_1 + '\r\n')
        send.flush() 

        response = recv.readline() 
        
      else:
        pass

      msg = '{"token": "' + str(new_token) + '", "post": {"entry":"' + str(message) + '", "timestamp": "' + str(Profile.time.time()) + '"}}' # posts user's desired message

      send.write(msg + '\r\n')
      send.flush()
      srv_msg = recv.readline()
      part1_protocol.extract_json(srv_msg).message # prints confirmation message 
      
      break

  
  pass


def bio_function(bio, new_token):
  bio_post = '{"token":"' + str(new_token) + '", "bio": {"entry": "' + str(bio) + '","timestamp": "' + str(Profile.time.time()) + '"}}' #to post a bio with a post

  return bio_post
