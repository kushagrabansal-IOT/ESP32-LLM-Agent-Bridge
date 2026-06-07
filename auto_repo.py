import requests
import random
import os
from datetime import datetime

TOKEN = os.environ.get("GH_TOKEN", "")
headers = {
    "Authorization": f"token {TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}

ts = datetime.now().strftime("%m%d%H%M")

pool = [
    {"name": f"ESP32-TinyML-Edge-{ts}", "desc": "TinyML inference on ESP32 for real-time edge AI classification - ultra low power, offline capable", "topics": ["esp32","tinyml","edge-ai","tensorflow-lite","embedded"]},
    {"name": f"IoT-Sensor-Fusion-{ts}", "desc": "Multi-sensor fusion with Kalman filter on ESP32 for precision IoT positioning and monitoring", "topics": ["esp32","sensor-fusion","kalman-filter","iot","embedded"]},
    {"name": f"ESP32-Voice-AI-{ts}", "desc": "Offline voice assistant on ESP32-S3 with wake word detection and local command execution", "topics": ["esp32","voice-assistant","offline-ai","tinyml","embedded"]},
    {"name": f"Smart-Security-System-{ts}", "desc": "AI-powered security system with face detection, intruder alert and GSM notification on ESP32", "topics": ["esp32","security","ai","gsm","face-detection","iot"]},
    {"name": f"MQTT-Smart-Hub-{ts}", "desc": "Central IoT hub with MQTT broker, anomaly detection, real-time dashboard and mobile alerts", "topics": ["mqtt","iot","esp32","dashboard","smart-home","automation"]},
    {"name": f"ESP32-CAM-AI-Vision-{ts}", "desc": "Computer vision system on ESP32-CAM with object detection, counting and cloud sync", "topics": ["esp32-cam","computer-vision","object-detection","iot","embedded"]},
    {"name": f"BLE-Mesh-IoT-{ts}", "desc": "BLE mesh network for scalable IoT deployments with automatic device discovery and routing", "topics": ["bluetooth","ble","mesh","iot","esp32","embedded"]},
]

project = random.choice(pool)

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
    print(f"CREATED: {data['html_url']}")
    # Add topics
    username = data['owner']['login']
    requests.put(
        f"https://api.github.com/repos/{username}/{project['name']}/topics",
        headers={**headers, "Accept": "application/vnd.github.mercy-preview+json"},
        json={"names": project["topics"]}
    )
    print(f"Topics set: {project['topics']}")
else:
    print(f"Error {resp.status_code}: {resp.text}")
