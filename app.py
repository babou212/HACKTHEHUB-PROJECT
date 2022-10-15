from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "welcome"

@app.route("/hi")
def who():
    return "who are you?"

@app.route("/hi/<userName>")
def greeting(userName):
    return f"hi there, {userName}"

if __name__ == '__main__':
    app.run(debug=True)