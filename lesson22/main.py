from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return '''<h1>python哇塞!</h1>
            <p>實在是太猛了</p>
            '''