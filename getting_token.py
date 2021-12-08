import socket
import ds_messenger
import part1_protocol


port = 3021
server = "168.235.86.101"

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client: # opening socket stream
    client.connect((server, port)) # connects to server and port passed to send function
    
    send = client.makefile('w') # to send
    recv = client.makefile('r') # to receive responses

    print('client connected to', server,'on', port) # confirmation to user

    json_msg = '{"join": {"username": "unittestwork" ,"password": "hellowrodl1223", "token": ""}}' 
        
    send.write(json_msg + '\r\n')
    send.flush() #cant leave anything behind 

    respo = recv.readline()

    new_token = part1_protocol.extract_json(respo)[0] # grabs token from join response

    ds_messenger.DirectMessenger(dsuserver=server, username="unittestwork", password="hellowrodl1233")
    ds_messenger.DirectMessenger.token = new_token

    ds_messenger.DirectMessenger.send(ds_messenger.DirectMessenger, "Hello Bob", "unittestwork")



