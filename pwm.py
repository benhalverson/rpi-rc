from gpiozero import Servo
from time import sleep, time
import csv

servo = Servo(18)

data_dir = "data"
log_file = "pwm_log.csv"

with open(log_file, "a") as f:
    writer = csv.writer(f)
    writer.writerow(["time", "pwm"])

    for position in range(0, 10):
        servo.value = position
        writer.writerow([time(), position])

        print(f"Position: {position}")
        sleep(0.5)

print("Logging complete.")