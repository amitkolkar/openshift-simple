#main.py
from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
  return "Congratulations, its a web app! Update 1"

if __name__ == "__main__" :
  app.run(host="0.0.0.0", port=8080)
