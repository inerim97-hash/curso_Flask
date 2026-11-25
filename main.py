from flask import Flask, request

app = Flask(__name__)

@app.route("/")

def index():
    user_ip_information = request.remote_addr
    return f"Keubule prro, tu direccion ip es la siguiente {user_ip_information}" 

app.run(host='0.0.0.0', port=81, debug=True)

