#!/usr/bin/env python

import os
import random
from flask import Flask, jsonify

length = os.getenv('LENGTH', 4)
blocks = os.getenv('BLOCKS', 4)
port = os.getenv('PORT', 3000)
debug = os.getenv('DEBUG', True)

app = Flask(__name__)
chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

def get_block():
  block=''
  for i in range(length):
    next_index = random.randrange(len(chars))
    block = block + chars[next_index]
  return block

def get_password():
  password=[]
  for i in range(blocks):
    password.append(get_block())
  return '-'.join(password)

@app.route('/', methods=['GET'])
def index():
    return get_password()

@app.route('/json', methods=['GET'])
def get_json():
    return jsonify(
        password=get_password()
    )

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=port, debug=debug)
