from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'
萨法
史蒂夫
if __name__ == '__main__':
    app.run()
所发生的