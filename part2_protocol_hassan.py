# Hassan Al-Najjar
# hhalnajj@uci.edu
# 67882437

import json
from collections import namedtuple

# Namedtuple to hold the values retrieved from json messages.
DataTuple = namedtuple('DataTuple', ['response', 'response_type'])


def extract_json(json_msg:str): #-> DataTuple:
  '''
  Call the json.loads function on a json string and convert it to a DataTuple object'''
  json_obj = json.loads(json_msg)

  try:
    response = json_obj['response']
    response_type = response['type']
  except json.JSONDecodeError:
    print("Json cannot be decoded.")
  return DataTuple(response, response_type)


def make_json(token, post=None, bio=None):
  ''' Serializes a post or bio into a json string.'''
  if post:
    json_string  = json.dumps({'token': token, 'post': post})
  elif bio:
    json_string  = json.dumps({'token': token, 'bio': bio})
  return json_string


def join_server_json(username, password):
  ''' Serializes username or password into a json string.'''
  json_dict = {'username': username, 'password': password, 'token': ''}
  return json.dumps({'join' :json_dict})
