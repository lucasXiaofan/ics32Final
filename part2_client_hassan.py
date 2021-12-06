import socket
import ds_protocol
import time

def send_message(client, message):
  client.sendall(message.encode('utf-8'))  # SEND


def recieve_message(client):
  return client.recv(4096).decode('utf-8')  #  RECIEVE


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

  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect((server, port))

    msg = ds_protocol.join_server_json(username=username, password=password)
    send_message(client, msg) # SEND

    print('\n\n')
    
    recv_msg = recieve_message(client)  #  RECIEVE

    DataTuple = ds_protocol.extract_json(recv_msg)
    if DataTuple.response_type == 'ok':
      # If there isn't any errors with the data given, the client will use the token given to it by the server in order to authenticate it
      token = DataTuple.response['token']

      if bio:
        # If the bio isn't empty, the client will send the bio to the server
        bio = {'entry': bio, 'timestamp': str(time.time())}
        msg_bio = ds_protocol.make_json(token, bio=bio)
        send_message(client, msg_bio) # SEND

        recv_msg = recieve_message(client)  #  RECIEVE

      # Sends the post to the server
      post = {'entry': message, 'timestamp': str(time.time())}
      msg_post = ds_protocol.make_json(token=token, post=post)
      send_message(client, msg_post) # SEND

      recv_msg = recieve_message(client)  # RECIEVE
      print('Post Uploaded!')

    elif DataTuple.response_type == 'error':
      # Tells the user what the issue is if there was an error
      message = DataTuple.response['message']
      print('Error:', message)



