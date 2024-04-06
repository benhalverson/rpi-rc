import sys
import time
from datetime import datetime
import pigpio
import csv

last = [None]*32
cb = []

csv_file = open('frequency_data.csv', mode='w', newline='')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Timestamp', 'Frequency (Hz)'])

def calculate_frequency(diff: float):
    if diff > 0:  
        frequency = 1_000_000 / diff 
        return round(frequency, 2)
    else:
        return None 

def cbf(GPIO, level, tick):
   global csv_writer
   if last[GPIO] is not None:
      diff = pigpio.tickDiff(last[GPIO], tick)
      freqency = calculate_frequency(diff)
      if freqency:
         print(freqency, 'Hz')
         timestamp = datetime.now().strftime("%H:%M:%S")
         csv_writer.writerow([timestamp, freqency])
   last[GPIO] = tick


pi = pigpio.pi()

if not pi.connected:
   exit()

if len(sys.argv) == 1:
   # G = range(0, 32)
   G = [18]
else:
   G = []
   for a in sys.argv[1:]:
      G.append(int(a))
   
for g in G:
   cb.append(pi.callback(g, pigpio.EITHER_EDGE, cbf))

try:
   while True:
      time.sleep(600)
except KeyboardInterrupt:
   print("\nTidying up")
   for c in cb:
      c.cancel()

pi.stop()
csv_file.close()

