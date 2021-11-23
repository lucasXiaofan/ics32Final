# ds_protocol.py

# Starter code for assignment 3 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Sona Keshishyan
# sonak1@uci.edu
# 94639158

import json
from collections import namedtuple
import ds_messenger

DataTuple = namedtuple('DataTuple', ['token', 'message']) # stored for easy access for client module to utilize

def extract_json(json_msg:str) -> DataTuple: # helps get important information from response
  '''
  Call the json.loads function on a json string and convert it to a DataTuple object
  
  '''
  try:
    json_obj = json.loads(json_msg)
    if json_obj["response"]["type"] == "ok":
      if "token" in json_obj["response"]:
        token = json_obj["response"]["token"] # takes token and uses it
        message = json_obj["response"]["message"] # prints message for user 
        print(message)
      else:
        token = None # if response with no token then would still work with namedtuple
        message = json_obj["response"]["message"] # prints message for user to know 
        print(message)
    else:
      print(json_obj)
      
  except json.JSONDecodeError:
    print("Json cannot be decoded.")

  return DataTuple(token, message) # easy to use in client module, if i need just message or just token 

  




