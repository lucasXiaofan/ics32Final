print('part 3 - Hassan')

from json.decoder import JSONDecodeError
import time
#from Profile import Profile
import json

file = 'part3_test_file.json'

def get_data():
    # TODO: Rather than reading a file to get the data, use the Profile module to serialize new data (in form of JSON object)
    
    with open(file, 'r') as f:
        return json.load(f)

def init_json():
    with open(file, 'w') as f:
        json.dump({}, f)

def store_data(contacts):
    # TODO: Rather than writing to a file to store data, use the Profile module to store the data somehow
       with open(file, 'w') as f:
           json.dump(contacts, f)

def display_text(contacts):
    for k, v in contacts.items():
        print(k)
        for message in v:
            print(message)
    # Make it so it displays all contacts



class Message:
    def __init__(self, timestamp, is_sent, text=''):
        self.timestamp = timestamp
        self.is_sent = is_sent
        self.text = text




class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def create_message(self, text):
        return Message(timestamp=int(time.time()), is_sent=True, text=text)



class OtherUser:
    def __init__(self, username):
        self.username = username
    
    def get_message(self, text):
        return Message(timestamp=int(time.time()), is_sent=False, text=text)


if __name__ == '__main__':
    try:
        data = get_data()

    except JSONDecodeError:  # the JSON file is empty
        init_json()
        data = get_data()

    print(f'\ndata: {data}\n')

    username = "hassan"
    password = "1234"
    
    other_username = "test_user"
    user_1 = User(username, password)
    user_2 = OtherUser(other_username)
    message = user_1.create_message("hello")
    message = user_2.get_message("hello")



    # This dictionary stores all the users contacts alongside their messages
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
                new_contact_messages.append(user_1.create_message(inp).__dict__)
            else:
                new_contact_messages.append(user_2.get_message(inp).__dict__)


    contacts = data
    print(contacts)
    if user_2.username in contacts:
        contacts[user_2.username].extend(new_contact_messages)
    else:
        contacts[user_2.username] = new_contact_messages
    store_data(contacts)
    #display_text(contacts)



#Make it so that when you get the data from the file, you add it to the contacts dict and then when you store the data, you 
#write the entire contacts dict without appending
