from gpiozero import MCP3008
import time

# Threshold voltage to consider a channel "active"
voltage_threshold = 0.5  # 0.5V threshold, adjust as needed

# Create MCP3008 objects for each channel
adc_channels = [MCP3008(channel=i) for i in range(8)]

while True:
    for i, adc in enumerate(adc_channels):
        voltage = adc.value * 3.3  # Convert the 0-1 value to 0-3.3V
        if voltage > voltage_threshold:
            print(f"Channel {i} is active with {voltage:.2f} V")
        else:
            print(f"Channel {i} is not active.")
    time.sleep(1)