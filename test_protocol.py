import json
from json.decoder import JSONDecodeError
from logging import ERROR
import part1_protocol
import unittest
import socket
import json

json_msg = '{"join": {"username": "unittesrddefeftwork" ,"password": "whatsupppp1234", "token": ""}}'
response_msg = '{"response": {"type": "ok", "message": "Direct message sent"}}'
response_messages = '{"response": {"type": "ok", "messages": [{"message":"Hello User 1!", "from":"markb", "timestamp":"1603167689.3928561"},{"message":"Bzzzzz", "from":"thebeemoviescript", "timestamp":"1603167689.3928561"}]}}'
server_response = '{"response": {"type": "ok", "messages": [{"message": "Hello World", "from": "unittestwork", "timestamp": "1638918547.8141189"}]}}'
token_response = '{"response": {"type": "ok", "message": "Welcome back, unittestwork", "token": "31292afb-8505-4421-b112-e18bc0938642"}}'


class TestProtocol(unittest.TestCase):
    def test_is_list(self):
        response_list = part1_protocol.extract_json(response_msg)[1]
        self.assertIsInstance(response_list, list)
        response_list1 = part1_protocol.extract_json(response_messages)[1]
        self.assertIsInstance(response_list1, list)
        self.assertIsInstance(json_msg, str)

    def test_works(self):
        message = [{'message': 'Hello User 1!', 'from': 'markb', 'timestamp': '1603167689.3928561'}, {'message': 'Bzzzzz', 'from': 'thebeemoviescript', 'timestamp': '1603167689.3928561'}, {'message': 'Hello World', 'from': 'unittestwork', 'timestamp': '1638918547.8141189'}]
        self.assertEqual(part1_protocol.extract_json(server_response)[1], message)
        token = "31292afb-8505-4421-b112-e18bc0938642"
        self.assertEqual(part1_protocol.extract_json(token_response)[0], token)

    

if __name__ == "__main__":
    unittest.main()