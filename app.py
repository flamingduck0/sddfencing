from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    output = render_template('base.html')
    return output


if __name__ == '__main__':
    app.run()
