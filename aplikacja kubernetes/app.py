from flask import Flask, render_template, request
import socket

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
        return render_template('index.html', ip_address=ip_address, updated=True)
    else:
        return render_template('index.html', updated=False)

if __name__ == '__main__':
    app.run(debug=True)
