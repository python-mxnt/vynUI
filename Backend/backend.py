from flask import Flask, send_from_directory
from getOllamaModeldata import ollamalist
from collectHostData import boot_time, cpu_info, system_info, memory_info, get_size, disk_info, network_info, get_host_data

vynUI = Flask(__name__, static_folder='Frontend/static')

# Serve index.html
@vynUI.route('/')
def index():
    return send_from_directory('Frontend', 'index.html')

# Serve other frontend files (like CSS)
@vynUI.route('/<path:path>')
def serve_file(path):
    return send_from_directory('Frontend', path)

if __name__ == "__main__":
    vynUI.run(debug=True)