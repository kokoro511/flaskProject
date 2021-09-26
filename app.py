from flask import Flask
app = Flask(__name__)

@app.route('/f/<num>')
def greet(num=""):
    a = (num * 1.8) + 32
    return "{}".format(a)

if __name__ == '__main__':
    app.run()

