from flask import Flask, send_from_directory

app = Flask(__name__, static_url_path='')

@app.route('/')
def home():
    return app.send_static_file('index.html')

@app.route('/<path:path>')
def static_file(path):
    return app.send_static_file(path)

if __name__ == "__main__":
app.run()
