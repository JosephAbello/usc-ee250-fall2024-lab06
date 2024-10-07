import time
import RPi.GPIO as GPIO
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008

# using physical pin 11 to blink an LED
LED_PIN = [11]
GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED_PIN, GPIO.OUT)

# Channel setup for MCP3008
LIGHT_SENSOR_CHANNEL = 0
SOUND_SENSOR_CHANNEL = 1

# Hardware SPI configuration:
SPI_PORT   = 0
SPI_DEVICE = 0
mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))

# by taking readings and printing them out, find
# appropriate threshold levels and set them 
# accordingly. Then, use them to determine
# when it is light or dark, quiet or loud.
lux_threshold = 300  # change this value
sound_threshold = 500 # change this value

while True:
  time.sleep(0.5)

  # Blink the LED 5 times with on/off intervals of 500ms.
  for i in range(5):
    #Following commands control the state of the output
    #GPIO.output(pin, GPIO.HIGH)
    #GPIO.output(pin, GPIO.LOW)
    GPIO.output(LED_PIN, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(LED_PIN, GPIO.LOW)
    time.sleep(0.5)

  # read the output of the Grove light sensor with intervals of 100 ms and print the raw value along with the text “bright” or “dark”
  print("Reading light sensor...")
  start_time = time.time()
  # Read for 5 seconds
  while time.time() - start_time < 5:
    # get reading from adc 
    # mcp.read_adc(adc_channel)
    light_value = mcp.read_adc(LIGHT_SENSOR_CHANNEL)
    if light_value > lux_threshold:
      print(f"Light value: {light_value} - Bright")
    else:
      print(f"Light value: {light_value} - Dark")
    # 100ms intervals
    time.sleep(0.1)
  
  # Blink the LED 4 times with on/off intervals of 200ms.
  for i in range(4):
    GPIO.output(LED_PIN, GPIO.HIGH)
    time.sleep(0.2)
    GPIO.output(LED_PIN, GPIO.LOW)
    time.sleep(0.2)
  
  # read the output of the Grove sound sensor with intervals of 100 ms and print the raw value. If the sound sensor is tapped, the LED should turn on for 100 ms.
  print("Reading sound sensor...")
  start_time = time.time()
  # Read for 5 seconds
  while time.time() - start_time < 5:
    # get reading from adc 
    # mcp.read_adc(adc_channel)
    sound_value = mcp.read_adc(SOUND_SENSOR_CHANNEL)
    print(f"Sound value: {sound_value}")
    if sound_value > sound_threshold:
      print("Sound exceeded treshold")
      GPIO.output(LED_PIN, GPIO.HIGH)
      time.sleep(0.1)  # LED on for 100ms
      GPIO.output(LED_PIN, GPIO.LOW)
    time.sleep(0.1)  # 100ms intervals