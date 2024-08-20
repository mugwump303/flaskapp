#!/usr/bin/env python3
from flask import Flask, request, render_template
import datetime

app = Flask(__name__)

# TODO: Add rabbitmq. Use it to send messages.

@app.route("/")
def main():
    f = open("home.txt", "a")
    now = datetime.datetime.now()
    text = f"<div>Page Hit: {now}</div>"
    f.write(text)
    f.close()

    render_template('index.html')

@app.route("/echo_user_input", methods=["POST"])
def echo_input():
    input_text = request.form.get("user_input", "")
    return "You entered: " + input_text