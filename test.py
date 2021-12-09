'''import Profile
x= Profile.Profile()
x.load_profile('profiles/xiaof.dsu')
x.contacts =  {"professor": [{"timestamp": 1638578507, "is_sent": True, "text": "hey"}, {"timestamp": 1638578511, "is_sent": False, "text": "hey "}, {"timestamp": 1638578642, "is_sent": True, "text": "hey professor"}, {"timestamp": 1638578644, "is_sent": False, "text": "whats up"}], "new_contact": [{"timestamp": 1638578602, "is_sent": True, "text": "hey"}, {"timestamp": 1638578604, "is_sent": False, "text": "hello"}, {"timestamp": 1638578607, "is_sent": True, "text": "whats up"}, {"timestamp": 1638578613, "is_sent": True, "text": ""}, {"timestamp": 1638578614, "is_sent": True, "text": "a"}, {"timestamp": 1638578614, "is_sent": True, "text": "a"}], "hello": [{"timestamp": 1638838474, "is_sent": True, "text": "hey"}, {"timestamp": 1638838482, "is_sent": False, "text": "whats up"}, {"timestamp": 1638838509, "is_sent": True, "text": "a"}, {"timestamp": 1638838510, "is_sent": True, "text": "b"}]}
x.save_profile('profiles/xiaof.dsu')
'''
'''
from ds_messenger import DirectMessenger
server = "168.235.86.101" #dsu server is hardcoded rn but it shouldnt be 

dm = DirectMessenger(dsuserver=server, username="xiaof", password="1234")
print(dm.token)
dm.token = dm.join() 
msg = dm.retrieve_all()
key_name = []
contacts = {}
message_list = []
def make_list(msg_dictionary,name):
    message_list = []
    for msg_dic2 in msg_dictionary:
        if name == msg_dic2['from']:
            message_list.append(msg_dic2)
    return message_list

for msg_dic in msg:
    if msg_dic['from'] not in key_name:
        key_name.append(msg_dic['from'])

for name in key_name:
    
    list = make_list(msg,name)
    contacts['{}'.format(name)] = list

print(msg)
'''
"""print(contacts)
print(len(contacts['brandonliu']))
print(len(contacts['xiaof']))
print(len(contacts['unittestwork']))"""

Time = '123'
username = 'xiaofan'
body = 'hhhh'
New_message = '{'+'"timestamp": '+Time+', '+'"from": '+'"'+username+'", '+'"message": '+'"'+body+'"'+'}'
print(New_message)

