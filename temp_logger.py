import RPi.GPIO as GPIO
from datetime import datetime
import time
import csv
import os

GPIO.setmode(GPIO.BCM)

GPIO.setup(4, GPIO.IN)

def read_temp():
    with open("/sys/class/thermal/thermal_zone0/temp", "r") as f:
        return float(f.read().strip()) / 1000

def c_to_f(c: str): 
    return c * 9.0 / 5.0 + 32.0

def save_temp_to_csv(temp: float, time: float):
    data_dir = "data"
    os.makedirs(data_dir, exist_ok=True)
    with open(os.path.join(data_dir, "temp_log.csv"), "a") as f:
        writer = csv.writer(f)
        writer.writerow([time, temp])

def get_voltage_value():
    try:
        if GPIO.input(4):
            print("Pin is HIGH")    
        else:
            print("Pin is LOW")
    except Exception as e:
        print("Error", e)
        


if __name__ == "__main__":

    while True:
        current_time = datetime.now().strftime("%H:%M:%S")
        temp = read_temp()
        fahrenheit = c_to_f(temp)
        write_to_csv = f"{current_time}, {fahrenheit}"
        save_temp_to_csv(temp, current_time)
        print("Current Time =", current_time, "Temp ", fahrenheit, "F", "Temp ",  temp, "C")
        time.sleep(10)
        get_voltage_value()
