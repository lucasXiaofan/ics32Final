# ds_protocol.py

# Starter code for assignment 3 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Sona Keshishyan
# sonak1@uci.edu
# 94639158

import json
from collections import namedtuple
import part2_client
import ds_messenger

response_list = []

def extract_json(json_msg:str): # helps get important information from response
  '''
  Call the json.loads function on a json string and convert it to a DataTuple object
  
  '''
  try:
    json_obj = json.loads(json_msg)
    if json_obj["response"]["type"] == "ok": 
      if "token" in json_obj["response"]:
        user_token = json_obj["response"]["token"] # takes token and uses it
        message = json_obj["response"]["message"] # prints message for user 
        print(message)    
      elif "messages" in json_obj["response"]:
        user_token = None
        messages = json_obj["response"]["messages"] # user messages
        for i in messages:
          response_list.append(i)
        print(response_list)
      else:
        user_token = None
        message = json_obj["response"]["message"] # prints message for user to know 
        print(message)
    else:
      print(json_obj)
      
  except json.JSONDecodeError:
    print("Json cannot be decoded.")

  return user_token, response_list # easy to use in client module, if i need just message or just token 

  




