# ESP32 LLM Agent Bridge 🤖⚡

[![ESP32](https://img.shields.io/badge/Hardware-ESP32-blue)](https://www.espressif.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Stars](https://img.shields.io/github/stars/kushagrabansal-IOT/ESP32-LLM-Agent-Bridge?style=social)](https://github.com/kushagrabansal-IOT/ESP32-LLM-Agent-Bridge)

> **Bridge between LLM AI Agents and physical ESP32 IoT devices using a lightweight UART protocol. Inspired by the Device Context Protocol (DCP) trend.**

Built by [Kushagra Bansal](https://github.com/kushagrabansal-IOT) | Founder @ [Project Lab India](https://projectlabindia.in)

---

## 🚀 What This Does

Allows LLM agents (Claude, GPT, Gemini) to **directly control and communicate** with ESP32 hardware through:
- Sub-50-byte UART frames
- Capability-scoped device commands
- Real-time sensor data streaming to AI agents
- Offline fallback with local rule engine

---

## 🔧 Hardware Required

| Component | Specification |
|-----------|--------------|
| Microcontroller | ESP32 / ESP32-S3 |
| Communication | UART (115200 baud) |
| Sensors | DHT22, MPU6050, Ultrasonic (optional) |
| Actuators | Relay Module, Servo, LEDs |
| Power | 5V USB / LiPo Battery |

---

## 📁 Project Structure

```
ESP32-LLM-Agent-Bridge/
├── firmware/
│   ├── main.ino          # ESP32 Arduino firmware
│   ├── protocol.h        # DCP-inspired frame structure
│   └── sensors.h         # Sensor abstraction layer
├── agent/
│   ├── bridge.py         # Python LLM ↔ ESP32 bridge
│   └── tools.py          # LLM tool definitions
├── examples/
│   ├── led_control/      # Simple LED agent control
│   ├── sensor_stream/    # Real-time sensor to LLM
│   └── voice_command/    # Voice → ESP32 pipeline
├── docs/
│   └── protocol.md       # Frame specification
└── README.md
```

---

## ⚡ Quick Start

```bash
# Clone the repo
git clone https://github.com/kushagrabansal-IOT/ESP32-LLM-Agent-Bridge.git

# Install Python dependencies
pip install pyserial anthropic

# Flash ESP32 firmware
# Open firmware/main.ino in Arduino IDE → Upload

# Run the bridge
python agent/bridge.py --port /dev/ttyUSB0 --model claude-sonnet
```

---

## 📡 Protocol Frame Format

```
[START_BYTE][CMD_TYPE][PAYLOAD_LEN][PAYLOAD...][CHECKSUM]
     0xAA      1 byte    1 byte     N bytes      1 byte
```

**Commands:**
- `0x01` → Read sensor
- `0x02` → Set actuator
- `0x03` → Stream mode ON
- `0x04` → Emergency stop

---

## 🧠 Use Cases

- ✅ AI-controlled home automation
- ✅ Voice command → hardware action
- ✅ Real-time sensor monitoring via LLM
- ✅ Autonomous robot decision making
- ✅ IoT + TinyML edge inference

---

## 👨‍💻 Author

**Kushagra Bansal**
- 🏢 Founder @ Project Lab India, Jaipur
- 🔬 ESP32 | Edge AI | Robotics | Embedded Systems
- 🏆 Innovation Award Recipient | IEEE Member
- 🌐 [radiomarket.in](https://radiomarket.in)

---

## 📄 License

MIT License — Free to use, modify, and distribute.

> ⭐ Star this repo if you found it useful!
