let imageData = null;

navigator.mediaDevices.getUserMedia({video:true})
.then(stream => {
    document.getElementById('video').srcObject = stream;
})
.catch(err => {
    alert("فشل الوصول للكاميرا");
});

function capture(){
    const video = document.getElementById('video');
    const canvas = document.getElementById('canvas');

    canvas.width = video.videoWidth;
    canvas.height = video.videoHeight;

    const ctx = canvas.getContext('2d');
    ctx.drawImage(video, 0, 0);

    imageData = canvas.toDataURL('image/jpeg');
    alert("تم التقاط الصورة");
}

async function send(){
    if(!imageData){
        alert("التقط صورة أولاً");
        return;
    }

    const res = await fetch('/send_photo', {
        method:'POST',
        headers:{'Content-Type':'application/json'},
        body: JSON.stringify({image:imageData})
    });

    const data = await res.json();

    alert(data.success ? "تم الإرسال" : "فشل الإرسال");
      }
