from flask import Flask, request, make_response, redirect

app = Flask(__name__)

@app.route("/index")

def index():
    user_ip_information = request.remote_addr
    response = make_response( redirect("/show_information_address"))
    response.set_cookie("user_ip_information", user_ip_information)
    return response

 

app.run(host='0.0.0.0', port=81, debug=False)