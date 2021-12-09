'''import Profile
x= Profile.Profile()
x.load_profile('profiles/xiaof.dsu')
x.contacts =  {"professor": [{"timestamp": 1638578507, "is_sent": True, "text": "hey"}, {"timestamp": 1638578511, "is_sent": False, "text": "hey "}, {"timestamp": 1638578642, "is_sent": True, "text": "hey professor"}, {"timestamp": 1638578644, "is_sent": False, "text": "whats up"}], "new_contact": [{"timestamp": 1638578602, "is_sent": True, "text": "hey"}, {"timestamp": 1638578604, "is_sent": False, "text": "hello"}, {"timestamp": 1638578607, "is_sent": True, "text": "whats up"}, {"timestamp": 1638578613, "is_sent": True, "text": ""}, {"timestamp": 1638578614, "is_sent": True, "text": "a"}, {"timestamp": 1638578614, "is_sent": True, "text": "a"}], "hello": [{"timestamp": 1638838474, "is_sent": True, "text": "hey"}, {"timestamp": 1638838482, "is_sent": False, "text": "whats up"}, {"timestamp": 1638838509, "is_sent": True, "text": "a"}, {"timestamp": 1638838510, "is_sent": True, "text": "b"}]}
x.save_profile('profiles/xiaof.dsu')
'''

from ds_messenger import DirectMessenger
server = "168.235.86.101" #dsu server is hardcoded rn but it shouldnt be 

dm = DirectMessenger(dsuserver=server, username="unittest123", password="passwrod1234")
print(dm.token)
dm.token = dm.join() 
print(dm.token)