import ds_messenger
import unittest
import socket
import json

port = 3021
server = "168.235.86.101"

class TestDS_Messenger(unittest.TestCase):
    def setUp(self):
        print("In setUp()")
        self.token1 = "31292afb-8505-4421-b112-e18bc0938642"
        self.token2 = "23433ber-3434-6454-g343-y34rb4230453"

    def test_join(self):
        print("In test_join()")
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client: # opening socket stream
            client.connect((server, port)) # connects to server and port passed to send function
    
            send = client.makefile('w') # to send
            recv = client.makefile('r') # to receive responses


            json_msg = '{"join": {"username": "unittestwork" ,"password": "hellowrodl1223", "token": ""}}' 
        
            send.write(json_msg + '\r\n')
            send.flush() #cant leave anything behind 

            respo = recv.readline()
            json_obj = json.loads(respo)
            if json_obj["response"]["type"] == "ok": 
                    join_msg = True
            else:
                    join_msg = False
        self.assertTrue(join_msg)
        dm = ds_messenger.DirectMessenger(dsuserver=server, username="whatsupman", password="weoweowoe")
        token = dm.join()
        self.assertIsInstance(token, str)

    def test_DS_class(self):
        print("In test_DS_class()")
        ds_messenger.DirectMessenger.token = self.token1
        self.assertTrue(ds_messenger.DirectMessenger.send(ds_messenger.DirectMessenger, "Hello World", "unittestwork"))
        self.assertIsNotNone(ds_messenger.DirectMessenger.retrieve_all)
        self.assertIsNotNone(ds_messenger.DirectMessenger.retrieve_new)
        ds_messenger.DirectMessenger.token = self.token2
        self.assertTrue(ds_messenger.DirectMessenger.send(ds_messenger.DirectMessenger, "Hello World", "unittestwork"))
        self.assertIsNotNone(ds_messenger.DirectMessenger.retrieve_all)
        self.assertIsNotNone(ds_messenger.DirectMessenger.retrieve_new)

    def test_Message_class(self):
        print("In test_message_class()")
        dm1 = ds_messenger.DirectMessage()
        dm1.recipient = "unittestwork"
        dm1.message = "hello unit tester"
        self.assertIs(dm1.recipient, "unittestwork")
        self.assertIs(dm1.message, "hello unit tester")
        self.assertTrue(ds_messenger.DirectMessenger.send(ds_messenger.DirectMessenger, dm1.message, dm1.recipient))

    def tearDown(self):
        print("In tearDown()")
        del self.token1
        del self.token2
    

if __name__ == "__main__":
    unittest.main()
    print("Everything passed")