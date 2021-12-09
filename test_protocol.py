import json
from json.decoder import JSONDecodeError
from logging import ERROR
import part1_protocol
import unittest
import socket
import json

#  Source: ttps://docs.python.org/3/library/unittest.html

class TestProtocol(unittest.TestCase):
    def setUp(self):
        print("In setUp()")
        self.json_msg = '{"join": {"username": "unittesrddefeftwork" ,"password": "whatsupppp1234", "token": ""}}'
        self.response_msg = '{"response": {"type": "ok", "message": "Direct message sent"}}'
        self.response_messages = '{"response": {"type": "ok", "messages": [{"message":"Hello User 1!", "from":"markb", "timestamp":"1603167689.3928561"},{"message":"Bzzzzz", "from":"thebeemoviescript", "timestamp":"1603167689.3928561"}, {"message": "Hello World", "from": "unittestwork", "timestamp": "1638918547.8141189"}]}}'
        self.server_response = '{"response": {"type": "ok", "messages": [{"message": "Hello World", "from": "unittestwork", "timestamp": "1638918547.8141189"}]}}'
        self.token_response = '{"response": {"type": "ok", "message": "Welcome back, unittestwork", "token": "31292afb-8505-4421-b112-e18bc0938642"}}'
        self.response_message1 = '{"response": {"type": "ok", "messages": [{"message":"Hello User 2!", "from":"markb", "timestamp":"1603167689.3928561"}]}}'
        self.response_message2 = '{"response": {"type": "ok", "messages": [{"message":"Hello User 1!", "from":"markb", "timestamp":"1604167689.3928561"}, {"message":"Hello User 2!", "from":"markb", "timestamp":"1605137689.3928561"}, {"message":"Hello User 3!", "from":"markb", "timestamp":"1606167689.3928561"}, {"message":"Hello User 4!", "from":"markb", "timestamp":"1607167689.3928561"}]}}'
   
    def test_is_type(self):
        print("In test_is_type()")
        response_list = part1_protocol.extract_json(self.response_msg)[1]
        self.assertIsInstance(response_list, list)
        response_list1 = part1_protocol.extract_json(self.response_messages)[1]
        self.assertIsInstance(response_list1, list)
        self.assertIsInstance(self.json_msg, str)

    def test_works(self):
        print("In test_works()")
        message = [{'message': 'Hello User 1!', 'from': 'markb', 'timestamp': '1603167689.3928561'}, {'message': 'Bzzzzz', 'from': 'thebeemoviescript', 'timestamp': '1603167689.3928561'}, {'message': 'Hello World', 'from': 'unittestwork', 'timestamp': '1638918547.8141189'}]
        self.assertEqual(part1_protocol.extract_json(self.response_messages)[1], message)
        token = "31292afb-8505-4421-b112-e18bc0938642"
        self.assertEqual(part1_protocol.extract_json(self.token_response)[0], token)
        message2 = [{'message': 'Hello User 2!', 'from': 'markb', 'timestamp': '1603167689.3928561'}]
        self.assertEqual(part1_protocol.extract_json(self.response_message1)[1], message2)
        message3 = [{'message': 'Hello User 1!', 'from': 'markb', 'timestamp': '1604167689.3928561'}, {'message': 'Hello User 2!', 'from': 'markb', 'timestamp': '1605137689.3928561'}, {'message': 'Hello User 3!', 'from': 'markb', 'timestamp': '1606167689.3928561'}, {'message': 'Hello User 4!', 'from': 'markb', 'timestamp': '1607167689.3928561'}]
        self.assertEqual(part1_protocol.extract_json(self.response_message2)[1], message3)


    def tearDown(self):
        print("In tearDown()")
        del self.json_msg
        del self.response_messages
        del self.response_msg
        del self.server_response
        del self.token_response
        del self.response_message2


if __name__ == "__main__":
     unittest.main()