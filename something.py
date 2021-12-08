import socket
import part1_protocol
import ds_messenger

port = 3021
server = "168.235.86.101"


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client: # opening socket stream
  client.connect((server, port)) # connects to server and port passed to send function
    
  send = client.makefile('w') # to send
  recv = client.makefile('r') # to receive responses

  print('client connected to', server,'on', port) # confirmation to user

    # for json to use variables instead of actual hard-coded values, do this format: "' + str(variable) + '"

  while True:
    json_msg = '{"join": {"username": "unittesrddefeftwork" ,"password": "whatsupppp1234", "token": ""}}' # join message must always join before posting
    send.write(json_msg + '\r\n')
    send.flush() #cant leave anything behind 
    respo = recv.readline()
    print(respo)

    user_token = part1_protocol.extract_json(respo)[0]
    print(user_token)
    # pass token to populate ds_messenger 
    ds_messenger.DirectMessenger
    dmr = ds_messenger.DirectMessenger()
    ds_messenger.DirectMessenger(dsuserver=server, username="unittesrddefeftwork", password="whatsupppp1234")
    dmr.token = user_token

    break