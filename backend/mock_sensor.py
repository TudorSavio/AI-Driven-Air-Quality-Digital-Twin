import time
import random
import requests
import json

# This points to your local FastAPI backend
BACKEND_URL = "http://localhost:8000/api/sensor-data" 

def generate_mock_data():
    """Generates realistic-looking urban air quality data."""
    return {
        "temperature": round(random.uniform(28.0, 34.0), 2), # Typical Chennai heat
        "humidity": round(random.uniform(50.0, 75.0), 2),
        "co2": random.randint(400, 800),
        "tvoc": random.randint(10, 300),
        "pm25": round(random.uniform(15.0, 60.0), 2),
        "dust": round(random.uniform(10.0, 50.0), 2)
    }

print("🚀 Starting Virtual ESP32 Sensor System...")

while True:
    sensor_data = generate_mock_data()
    
    try:
        # Send the data to your AI Backend
        response = requests.post(BACKEND_URL, json=sensor_data)
        print(f"📡 Transmitted to Brain: {sensor_data}")
    except requests.exceptions.ConnectionError:
        print("⚠️ Backend offline. Waiting for FastAPI server...")
        
    # Wait 5 seconds before the next reading
    time.sleep(5)
