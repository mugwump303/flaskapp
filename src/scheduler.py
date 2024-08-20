import requests

# NOTE: This runs using a heroku scheduler, but, locally, it does nothing.

# import datetime
# f = open("scheduler.txt", "a")
# now = datetime.datetime.now()
# text = f"<div>Scheduler Run: {now}</div>"
# f.write(text)
# f.close()

url='https://mugwump303-flaskapp-a986c05f07c3.herokuapp.com/log_scheduler/'
response = requests.get(url)
print(response.status_code)
print(response.text)

