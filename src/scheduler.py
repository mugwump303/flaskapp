import datetime
# NOTE: This runs using a heroku scheduler, but, locally, it does nothing.

f = open("scheduler.txt", "a")
now = datetime.datetime.now()
text = f"<div>Scheduler Run: {now}</div>"

f.write(text)
f.close()
