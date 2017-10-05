#!/usr/bin/env python

import random
from flask import Flask, jsonify

app = Flask(__name__)
chars = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def gen_pass(password='',length=16):
  for i in range(length):
    next_index = random.randrange(len(chars))
    if i > 0 and i % 4 == 0:
      password += "-"
    password = password + chars[next_index]
  return password

@app.route('/', methods=['GET'])
def index():
    return gen_pass()

@app.route('/json', methods=['GET'])
def get_json():
    return jsonify(
        password=gen_pass()
    )

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
