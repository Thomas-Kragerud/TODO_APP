from flask import Flask
import models

# Application layer
app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    models.Schema()
    app.run()
