let imageData = null;

// تشغيل الكاميرا
navigator.mediaDevices.getUserMedia({ video: true })
.then(stream => {
    document.getElementById('video').srcObject = stream;
})
.catch(err => {
    alert("❌ فشل الوصول للكاميرا");
});

// التقاط صورة
function capture(){
    const video = document.getElementById('video');
    const canvas = document.getElementById('canvas');

    canvas.width = video.videoWidth;
    canvas.height = video.videoHeight;

    const ctx = canvas.getContext('2d');
    ctx.drawImage(video, 0, 0);

    imageData = canvas.toDataURL('image/jpeg');

    alert("📸 تم التقاط الصورة");
}

// إرسال الصورة للسيرفر
async function send(){
    if(!imageData){
        alert("⚠️ التقط صورة أولاً");
        return;
    }

    try {
        const res = await fetch('/send_photo', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                image: imageData
            })
        });

        const data = await res.json();

        if(data.success){
            alert("✅ تم إرسال الصورة بنجاح");
        } else {
            alert("❌ فشل الإرسال:\n" + (data.telegram_response || data.message));
        }

    } catch (error) {
        alert("🔥 خطأ في الاتصال بالسيرفر:\n" + error.message);
    }
                }
