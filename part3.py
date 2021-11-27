print('part 3 - Hassan')

import time
from Profile import Profile


def get_data():
    # TODO: Rather than reading a file to get the data, use the Profile module to serialize new data (in form of JSON object)
    
    with open('part3_test_file.txt', 'r') as f:
        return f.read()

def store_data(contacts):
    # TODO: Rather than writing to a file to store data, use the Profile module to store the data somehow

       with open('part3_test_file.txt', 'a') as f:
           f.write(contacts)



class Message:
    def init(self, timestamp, is_sent, text=''):
        self.timestamp = timestamp
        self.is_from_main = is_sent
        self.text = text



class User:
    def init(self, username, password):
        self.username = username
        self.password = password

    def create_message(self, text):
        return Message(time=int(time.time()), is_sent=True, text=text)



class OtherUser:
    def init(self, username):
        self.username = username
    
    def get_message(self, text):
        return Message(time=int(time.time()), is_sent=False, text=text)



# This dictionary stores all the users contacts alongside their messages
new_contact_dict = {
    'user1': ['hello', 'hey!', 'whats up', 'nothing much'],
    'user2': ['hi', 'yo', 'howdy', 'nada'],
}

