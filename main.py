import time
import network
import urequests
import dht
from machine import Pin

# Ubidots API Information
UBIDOTS_URL = "https://industrial.api.ubidots.com/api/v1.6/devices/[device_name]/"
UBIDOTS_TOKEN = "x"

# Flask API URL (Change to your PC's IP)
FLASK_SERVER_URL = "http://[ip_address]:5000/add_data"

# Wi-Fi Credentials
SSID = "x"
PASSWORD = "x"

# Define Ultrasonic Sensor Pins
TRIG = Pin(22, Pin.OUT)
ECHO = Pin(23, Pin.IN)

# DHT11 Sensor
dht_sensor = dht.DHT11(Pin(13))

# Function to Connect to Wi-Fi
def connect_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print("Connecting to Wi-Fi...")
        wlan.connect(SSID, PASSWORD)
        while not wlan.isconnected():
            time.sleep(1)
    print("Connected to Wi-Fi")

# Measure Distance from Ultrasonic Sensor
def measure_distance():
    TRIG.value(0)
    time.sleep_us(2)
    TRIG.value(1)
    time.sleep_us(10)
    TRIG.value(0)

    pulse_start = time.ticks_us()
    while ECHO.value() == 0:
        pulse_start = time.ticks_us()

    while ECHO.value() == 1:
        pulse_end = time.ticks_us()

    pulse_duration = time.ticks_diff(pulse_end, pulse_start)
    distance = (pulse_duration * 0.0343) / 2

    return distance

# Read DHT11 Sensor Data
def read_dht11():
    try:
        dht_sensor.measure()
        temp = dht_sensor.temperature()
        humid = dht_sensor.humidity()
        return temp, humid
    except Exception as e:
        print("DHT11 Error:", e)
        return None, None

# Send Data to Ubidots
def send_to_ubidots(distance, temperature, humidity):
    headers = {
        "X-Auth-Token": UBIDOTS_TOKEN,
        "Content-Type": "application/json"
    }

    data = {
        "distance": distance,
        "temperature": temperature,
        "humidity": humidity
    }

    try:
        response = urequests.post(UBIDOTS_URL, json=data, headers=headers)
        print("Ubidots Response:", response.text)
        response.close()
    except Exception as e:
        print("Error sending data to Ubidots:", e)

# Send Data to MongoDB via Flask API
def send_to_mongodb(distance, temperature, humidity):
    headers = {
        "Content-Type": "application/json"
    }

    data = {
        "distance": distance,
        "temperature": temperature,
        "humidity": humidity
    }

    try:
        response = urequests.post(FLASK_SERVER_URL, json=data, headers=headers)
        print("MongoDB Response:", response.text)
        response.close()
    except Exception as e:
        print("Error sending data to MongoDB:", e)


connect_wifi()

while True:
    distance = measure_distance()
    temp, humid = read_dht11()
    
    if temp is not None and humid is not None:
        print(f"Distance: {distance:.2f} cm, Temp: {temp}°C, Humidity: {humid}%")
        
        send_to_ubidots(distance, temp, humid)
        send_to_mongodb(distance, temp, humid)

    time.sleep(10)
