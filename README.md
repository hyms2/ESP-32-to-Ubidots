## **ESP32 IoT Sensor with Ubidots Integration**  

### 📌 **Project Overview**  
This project integrates an **ESP32 microcontroller** with **Ubidots** to send real-time sensor data over Wi-Fi. The system collects:  
- 📏 **Distance measurements** using an **ultrasonic sensor (HC-SR04)**  
- 🌡 **Temperature & Humidity** using a **DHT11 sensor**  
- 📡 **Wireless data transmission** to **Ubidots** via **REST API**  

The collected data is displayed in the **Ubidots dashboard** for real-time monitoring.  

---

## 🚀 **Features**
- 📡 **Wi-Fi Connectivity**: Connects the ESP32 to a Wi-Fi network.  
- 📊 **Data Logging**: Sends distance, temperature, and humidity to Ubidots.  
- 🔄 **Real-time Updates**: Sensor values update automatically.  
- 📉 **Ubidots Dashboard Integration**: Visualize data with graphs & widgets.  

---

## ⚙️ **Hardware Requirements**
- ✅ **ESP32** (NodeMCU / DevKit V1)  
- ✅ **Ultrasonic Sensor (HC-SR04)**  
- ✅ **DHT11 Temperature & Humidity Sensor**  
- ✅ **Jumper Wires**  
- ✅ **Micro-USB Cable**  

---

## 🛠 **Software Requirements**
- **MicroPython** (Firmware for ESP32)  
- **Thonny IDE** (For programming ESP32)  
- **Ubidots** (IoT platform for data visualization)  

---

## 🔌 **Wiring Diagram**
| Component  | ESP32 Pin  |
|------------|-----------|
| HC-SR04 Trig | GPIO 22 (D22) |
| HC-SR04 Echo | GPIO 23 (D23) |
| DHT11 Data | GPIO 13 (D13) |
| VCC (Both) | 3.3V or 5V |
| GND (Both) | GND |

---

---

## 🚀 **How It Works**
1. **ESP32 reads sensor data** from HC-SR04 and DHT11.  
2. **Sends the data** to Ubidots via **REST API (HTTP POST request)**.  
3. **Ubidots stores the values**, and you can **view them on the Ubidots dashboard**.  

---

---

## 📊 **Ubidots Dashboard Setup**
1. **Go to Ubidots** → Create a new **Device** (`esp-32`).  
2. **Add Variables**: `distance`, `temperature`, `humidity`.  
3. **Create Widgets**: Select **Gauge, Line Chart, or Table** to visualize data.  

---

---

## ✨ **Contributors**
👤 [Your Name] – Developer  

---

## 📜 **License**
This project is **open-source** under the **MIT License**.  

---
