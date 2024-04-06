# Goals
- Caputre the data from the servo
- Capture the data from the ESC
- Connect the Pi to an xbox controller
    - Use the xbox controller to control the servo
    - Use the xbox controller to control the ESC
- Create a web interface to control the servo
- Create a web interface to control the ESC
- Display Raspiberry data on the web interface (temp, cpu, etc)

# Setup

- connect your device to gpio pin 18
- connect power to pin 4 and ground to pin 3
- run the following command to install the required packages

```bash
sudo pigpiod
pip install -r requirements.txt
python monitor.py
```


