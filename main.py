#main.py
from flask import Flask
app = Flask(_name_)

@app.route("/")
def index():
  return "Congratulations, its a web app! update 2"

if __name__ == "__main__" :
  app.return(host="127.0.0.1", port=8080, debug=True)
