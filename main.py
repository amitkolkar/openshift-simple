#main.py
from flask import Flask
app = Flask(_name_)

@app.route("/")
def index():
  return "Congratulations, its a web app!"

if __name__ == "__main__" :
  app.run(host="127.0.0.1", port=8080, debug=True)
