import ds_messenger
import unittest
import socket
import getting_token


class TestDS_Messenger(unittest.TestCase):
    def test_is_true(self):
        getting_token
        ds_messenger.DirectMessenger.token = "31292afb-8505-4421-b112-e18bc0938642"
        self.assertTrue(ds_messenger.DirectMessenger.send(ds_messenger.DirectMessenger, "Hello World", "Sped"))

if __name__ == "__main__":
    unittest.main()
    print("Everything passed")