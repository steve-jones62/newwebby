from flask import Flask, jsonify
import socket

app = Flask(__name__)

@app.route('/get_info', methods=['GET'])
def get_info():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return jsonify({"hostname": hostname, "ip_address": ip_address})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)