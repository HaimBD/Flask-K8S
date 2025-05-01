from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "This is the original message. The next step is to change it via CI/CD..."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
