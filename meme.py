from flask import Flask

app = Flask(__name__)

#this is the place it goes
@app.route("/")
def index():
    return "Drink more coffee right now!"

app.run(host="127.0.0.1", port=80)
# using this to create a server 