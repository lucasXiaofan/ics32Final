import json
import part1_protocol
import unittest
import socket

json_msg = '{"join": {"username": "unittesrddefeftwork" ,"password": "whatsupppp1234", "token": ""}}'
response_msg = '{"response": {"type": "ok", "message": "Direct message sent"}}'
response_messages = '{"response": {"type": "ok", "messages": [{"message":"Hello User 1!", "from":"markb", "timestamp":"1603167689.3928561"},{"message":"Bzzzzz", "from":"thebeemoviescript", "timestamp":"1603167689.3928561"}]}}'

class TestProtocol(unittest.TestCase):
    def test_is_list(self):
        self.assertIsInstance(part1_protocol.extract_json(response_msg), list)
        self.assertIsInstance(part1_protocol.extract_json(response_messages), list)

if __name__ == "__main__":
    unittest.main()
    print("Everything passed")