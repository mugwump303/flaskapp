#!/usr/bin/env python3
from flask import Flask, Response, request, render_template
import datetime
from prometheus_client import Counter, generate_latest

COUNTER = Counter(
    'Hits',
    'Visits to Homepage',
)

LOGS = Counter(
    'Logs',
    'Jobs Logged to App ',
)

app = Flask(__name__)

@app.route("/")
def main():
    COUNTER.inc(1)

    f = open("home.txt", "a")
    now = datetime.datetime.now()
    text = f"<div>Page Hit: {now}</div>"
    f.write(text)
    f.close()

    home = open("home.txt", "r").read()
    scheduler = open("scheduler.txt").read()

    runs = {
        "home": home,
        "scheduler": scheduler,
    }
    
    return render_template('index.html', runs=runs)


@app.route("/log_scheduler/", methods=["GET"])
def log_scheduler():
    LOGS.inc(1)
    f = open("scheduler.txt", "a")
    now = datetime.datetime.now()
    text = f"<div>Scheduler Run: {now}</div>"
    f.write(text)
    f.close()

    return 'Log Recevied'

@app.route("/echo_user_input", methods=["POST"])
def echo_input():
    input_text = request.form.get("user_input", "")
    return "You entered: " + input_text

@app.get('/metrics')
def get_metrics():
    # https://stackoverflow.com/questions/25860304/how-do-i-set-response-headers-in-flask
    return Response(generate_latest(), content_type='text/plain')
