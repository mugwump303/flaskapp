# Tells system which file is our application file.
export FLASK_APP=src/app.py
export FLASK_DEBUG=1
flask run


docker rm -v $(docker ps --filter status=exited -q)
docker compose up -d prometheus
