import RPi.GPIO as GPIO
import time

# Use Broadcom SOC channel numbering
GPIO.setmode(GPIO.BOARD)

# Pin number (according to BCM numbering) to read PWM from
PWM_PIN = 18

# Set up the GPIO pin as an input
GPIO.setup(PWM_PIN, GPIO.IN)
# GPIO.setup(PWM_PIN, GPIO.OUT)
# GPIO.output(PWM_PIN, GPIO.IN)

# Variables to measure PWM
last_edge_time = None
frequency = None
duty_cycle = None

def edge_detected(channel):
    global last_edge_time, frequency, duty_cycle
    
    # Capture the current time
    now = time.time()
    
    if last_edge_time is not None:
        # Calculate the period and frequency
        period = now - last_edge_time
        frequency = 1.0 / period
        
        # Wait for a short time to measure the high phase
        # This is a crude way and might not work well for very high frequencies or precision measurements
        time.sleep(0.001)  # Sleep for 1 ms
        high_time_start = time.time()
        
        # Wait for the pin to go low (marking the end of the high phase)
        while GPIO.input(PWM_PIN) == GPIO.HIGH:
            print("Waiting for the pin to go low...")
            print("PWM_PIN", GPIO.input(PWM_PIN))
        
        # Calculate the high time and duty cycle
        high_time = time.time() - high_time_start
        duty_cycle = (high_time / period) * 100
        
        # Print the results
        print(f"Frequency: {frequency:.2f} Hz, Duty Cycle: {duty_cycle:.2f}%")
    
    # Update the last edge time
    last_edge_time = now

# Add a rising edge detect event
GPIO.add_event_detect(PWM_PIN, GPIO.RISING, callback=edge_detected)

try:
    # Keep the script running to detect edges
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    # Clean up GPIO on CTRL+C exit
    GPIO.cleanup()
GPIO.cleanup()  # Clean up GPIO on normal exit