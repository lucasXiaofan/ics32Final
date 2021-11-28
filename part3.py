print('part 3 - Hassan')

import time
import Profile

# Global variable that stores the current profile in use
_current_profile = Profile.Profile()
_current_path = ''



def create_profile(file_path, username=None, password=None, bio='', dsuserver=None):
    """Creates a profile using the Profile class."""
    global _current_profile  # Global variable
    _current_profile = Profile.Profile(dsuserver, username, password)
    _current_profile.bio = bio

    global _current_path
    _current_path = file_path  # This stores the file path into the global variable to be used in other functions


def clear_profile():
    """Clears the previous profile when loading in a new one."""
    global _current_profile
    _current_profile = Profile.Profile(dsuserver=None, username=None, password=None)
    _current_profile.bio = ''
    _current_profile._posts = []
    _current_profile.contacts = {}


def load_profile(file_path):
    """Loads a profile from a DSU file using the Profile class."""
    clear_profile()  # Clears the current profile so that the new profile could be loaded
    _current_profile.load_profile(file_path)

    global _current_path
    _current_path = file_path


def save_profile():
    """Saves a profile into a DSU file using the Profile class."""
    global _current_profile
    _current_profile.save_profile(_current_path)






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
    file_path = '/Users/mac/Desktop/profiles/test.dsu'

    load_profile(file_path)

    print(_current_profile.contacts)

    contacts = _current_profile.contacts
    display_text(contacts)
    

    other_username = input('Enter the contact username:\n')
    username = 'hassan'
    password = 'password'
    user_1 = User(username, password)
    user_2 = OtherUser(other_username)

    new_contact_messages = texting_interface(user_1, user_2)

    if user_2.username in contacts:
        contacts[user_2.username].extend(new_contact_messages)
    else:
        contacts[user_2.username] = new_contact_messages

    _current_profile.contacts = contacts
    save_profile()

    display_text(contacts)


if __name__ == '__main__':
    main()
