## **ESP32 IoT Sensor with Ubidots and MongoDB Integration**  

## 📌 Project Overview
This project uses an **ESP32** to collect sensor data from a **DHT11 temperature & humidity sensor** and an **HC-SR04 ultrasonic sensor**, sending it to **Ubidots** (for visualization) and **MongoDB** (for storage). The ESP32 connects to Wi-Fi, reads sensor values, and transmits the data via REST API.

## 🚀 Features
- Collects temperature and humidity using **DHT11**
- Measures distance using **HC-SR04 Ultrasonic Sensor**
- Sends data to **Ubidots** for real-time visualization
- Stores data in **MongoDB** via a Flask API

## 🛠️ Hardware Requirements
- **ESP32**
- **DHT11 Sensor**
- **HC-SR04 Sensor**
- **Jumper Wires**
- **Breadboard (Optional)**

## 🖥️ Software Requirements
- **MicroPython** (Firmware for ESP32)
- **Thonny** (MicroPython IDE)
- **Flask** (Python backend for MongoDB API)
- **MongoDB Atlas** (Cloud database)
- **Ubidots** (Data visualization)

## 🔌 Wiring Diagram
| Component  | ESP32 Pin  |
|------------|-----------|
| HC-SR04 Trig | D22 |
| HC-SR04 Echo | D23 |
| DHT11 Data | D13 |
| VCC (Both) | 3.3V |
| GND (Both) | GND |
