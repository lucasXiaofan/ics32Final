#part 3 - Hassan'

import time
import Profile

# Global variable that stores the current profile in use
_current_profile = Profile.Profile()


def create_path(filename):
    with open(filename, 'x') as f:
        pass


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


def display_profile():
    for key, value in _current_profile.contacts.items():
        print(key, value)

def check_password(p) -> bool:
    '''Returns True if the given password is equal to the profile's password.'''
    return p == _current_profile.password


def main():
    print('Configure account:')
    username = 'username1'  # CHANGE VALUE
    password = 'password'  # CHANGE VALUE

    logged_in = False
    

    file_path = f'profiles/{username}.dsu'
    try:
        load_profile(file_path)
    except Profile.DsuFileError:  # Path doesn't exist (new user)
        create_path(file_path)
        _current_profile.username = username
        _current_profile.password = password
        _current_profile.save_profile(file_path)

    if check_password(password):
        print('ACCESS GRANTED')
        logged_in = True
        display_profile()
    else:
        print('ACCESS DENIED')
    
    if logged_in:
        other_user = 'otheruser'  # CHANGE VALUE
        messages = [{'text': 'hello',}, {'text': 'whats up',}]  # Arbitrary configuration of the message format
        
        if other_user not in _current_profile.contacts:
            # If the username isn't in contacts
            _current_profile.contacts[other_user] = messages
        else:
            # If there already are messages for an existing user, then do 
            _current_profile.contacts[other_user].extend(messages)

        _current_profile.save_profile(file_path)
        display_profile()
    

if __name__ == '__main__':
    main()


# TODO: Test if there are any errors when there is nothing in the 
# messaging text editor but still send the message
