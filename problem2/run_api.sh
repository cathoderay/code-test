# Please, install requirements.txt before running it.

# Starts the server
gunicorn api:api

# In order to test the api, you can do something like:
# curl -d '{"expression":"(42*1)"}' -H "Content-Type: application/json" -X POST http://localhost:8000/calc
