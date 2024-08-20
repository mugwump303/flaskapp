import datetime
# TODO: Run some worker/process every so often.

f = open("scheduler_runs.txt", "a")
now = datetime.datetime.now()
text = f"<div>Scheduler Run: {now}</div>"

f.write(text)
f.close()
