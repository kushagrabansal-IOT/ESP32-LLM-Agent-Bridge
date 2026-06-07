import requests
import random
import os
from datetime import datetime

TOKEN = os.environ.get("GH_TOKEN", "")
USERNAME = "kushagrabansal-IOT"
headers = {
    "Authorization": f"token {TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}

ts = datetime.now().strftime("%m%d-%H%M")
slot = "morning" if datetime.now().hour < 12 else "evening"

TRENDING_POOL = [
    {
        "name": f"ESP32-TinyML-Classifier-{ts}",
        "desc": "Real-time TinyML image/audio classifier on ESP32 — offline, ultra low power, <50ms inference",
        "topics": ["esp32","tinyml","edge-ai","tensorflow-lite","embedded","machine-learning","arduino"]
    },
    {
        "name": f"IoT-Kalman-Sensor-Fusion-{ts}",
        "desc": "Multi-sensor fusion using Kalman filter on ESP32 for precision tracking and environmental monitoring",
        "topics": ["esp32","sensor-fusion","kalman-filter","iot","embedded","mpu6050","precision"]
    },
    {
        "name": f"ESP32-Offline-Voice-AI-{ts}",
        "desc": "Fully offline voice assistant on ESP32-S3 — wake word detection, local NLP, zero cloud dependency",
        "topics": ["esp32","voice-assistant","offline-ai","wake-word","tinyml","nlp","embedded"]
    },
    {
        "name": f"AI-Security-System-ESP32-{ts}",
        "desc": "Edge AI security system with face detection, intruder alert, GSM notification — runs on ESP32-CAM",
        "topics": ["esp32","security-system","face-detection","gsm","edge-ai","camera","iot"]
    },
    {
        "name": f"BLE-Mesh-IoT-Network-{ts}",
        "desc": "Scalable BLE mesh network for IoT deployments — auto device discovery, self-healing routing on ESP32",
        "topics": ["bluetooth","ble-mesh","iot","esp32","embedded","mesh-network","wireless"]
    },
    {
        "name": f"MQTT-AI-IoT-Hub-{ts}",
        "desc": "Central IoT hub with MQTT broker, real-time anomaly detection, dashboard and mobile push alerts",
        "topics": ["mqtt","iot","esp32","dashboard","anomaly-detection","smart-home","automation"]
    },
    {
        "name": f"Wearable-ECG-Monitor-ESP32-{ts}",
        "desc": "Wearable ECG monitor on ESP32 with real-time heart rate, arrhythmia detection and BLE data streaming",
        "topics": ["ecg","wearable","esp32","health","ble","biomedical","embedded"]
    },
    {
        "name": f"ESP32-LLM-Device-Control-{ts}",
        "desc": "Control physical ESP32 devices via LLM natural language commands — Claude/GPT to hardware bridge",
        "topics": ["esp32","llm","agent","mcp","edge-ai","device-control","iot","embedded"]
    },
    {
        "name": f"Robot-Gesture-Control-MPU6050-{ts}",
        "desc": "Gesture-controlled robot using ESP32 + MPU6050 with AI gesture recognition and real-time response",
        "topics": ["robot","gesture-control","esp32","mpu6050","robotics","embedded","ai"]
    },
    {
        "name": f"Smart-Energy-Monitor-ESP32-{ts}",
        "desc": "AI-powered energy monitor — real-time power consumption, anomaly detection, cost prediction on ESP32",
        "topics": ["energy-monitoring","esp32","iot","smart-meter","ai","power","automation"]
    }
]

project = random.choice(TRENDING_POOL)

print(f"[{slot.upper()}] Creating repo: {project['name']}")

# Create repo
resp = requests.post(
    "https://api.github.com/user/repos",
    headers=headers,
    json={
        "name": project["name"],
        "description": project["desc"],
        "private": False,
        "auto_init": True
    }
)

if resp.status_code == 201:
    data = resp.json()
    html_url = data["html_url"]
    print(f"✅ CREATED: {html_url}")

    # Add topics
    topic_resp = requests.put(
        f"https://api.github.com/repos/{USERNAME}/{project['name']}/topics",
        headers={**headers, "Accept": "application/vnd.github.mercy-preview+json"},
        json={"names": project["topics"]}
    )
    print(f"🏷️  Topics: {project['topics']}")

    # Write daily log
    with open("daily_log.txt", "a") as f:
        f.write(f"[{datetime.now().isoformat()}] [{slot}] CREATED: {html_url}\n")

    print(f"\n📦 SUMMARY")
    print(f"   Repo  : {project['name']}")
    print(f"   URL   : {html_url}")
    print(f"   Slot  : {slot}")
    print(f"   Time  : {datetime.now().strftime('%Y-%m-%d %H:%M IST')}")
else:
    print(f"❌ Error {resp.status_code}: {resp.text}")
