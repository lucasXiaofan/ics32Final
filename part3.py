print('part 3 - Hassan')

from json.decoder import JSONDecodeError
import time
#from Profile import Profile
import json

FILE = 'part3_test_file.json'


def init_json():
    #  This function is called whenever the JSON file is completely empty, it will put a "{}" 
    # inside which will then able to be read as an empty JSON file
    
    with open(FILE, 'w') as f:
        json.dump({}, f)


def get_data():
    # TODO: Rather than reading a file to get the data, use the Profile module to serialize new data (in form of JSON object)
    
    with open(FILE, 'r') as f:
        return json.load(f)

def texting_interface(user_1, user_2) -> list:
    #  TEST INTERFACE (Not using this code)
    # This list stores all the messages sent by a contact
    new_contact_messages = []

    user_1_bool = True
    while True:
        if user_1_bool:
            inp = input('Enter text, User 1: (type \'c\' to change users)\n')
        else:
            inp = input('Enter text, User 2: (type \'c\' to change users)\n')

        if inp == 'q':
            print('quit')
            break

        # 'c' doesnt work for some reason?
        if inp == 'c' and user_1_bool == True:
            user_1_bool = False
        elif inp == 'c' and user_1_bool == False:
            user_1_bool = True

        else:
            if user_1_bool:
                new_contact_messages.append(user_1.send_message(inp))
            else:
                new_contact_messages.append(user_2.get_message(inp))
    return new_contact_messages

def store_data(contacts):
    # TODO: Rather than writing to a file to store data, use the Profile module to store the data somehow
       with open(FILE, 'w') as f:
           json.dump(contacts, f)

def display_text(contacts):
    for k, v in contacts.items():
        print(f'\n{k}:')
        for message in v:
            print(message)
    # Make it so it displays all contacts


def create_message(timestamp, is_sent, text='') -> dict:
    return {'timestamp': timestamp, 'is_sent': is_sent, 'text': text}



class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def send_message(self, text) -> dict:
        return create_message(timestamp=int(time.time()), is_sent=True, text=text)



class OtherUser:
    def __init__(self, username):
        self.username = username
    
    def get_message(self, text) -> dict:
        return create_message(timestamp=int(time.time()), is_sent=False, text=text)


def main():
    try:
        data = get_data()
    except JSONDecodeError:  # the JSON file is empty
        init_json()
        data = get_data()
    display_text(data)
    
    username = 'hassan'
    password = '1234'
    other_username = input('Enter the contact username:\n')
    user_1 = User(username, password)
    user_2 = OtherUser(other_username)

    new_contact_messages = texting_interface(user_1, user_2)
    contacts = data

    if user_2.username in contacts:
        contacts[user_2.username].extend(new_contact_messages)
    else:
        contacts[user_2.username] = new_contact_messages

    store_data(contacts)
    display_text(contacts)


if __name__ == '__main__':
    main()
