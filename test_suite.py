import time
import RPi.GPIO as GPIO
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008

#using physical pin 11 to blink an LED
GPIO.setmode(GPIO.BCM)
chan_list = [11]
GPIO.setup(chan_list, GPIO.OUT)

# Hardware SPI configuration:
SPI_PORT   = 0
SPI_DEVICE = 0
LED_PIN = 11
mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))

# # Hardware SPI Setup
# GPIO.setup(LED_PIN, GPIO.OUT)

# by taking readings and printing them out, find
# appropriate threshold levels and set them 
# accordingly. Then, use them to determine
# when it is light or dark, quiet or loud.
lux_treshold=0  # change this value
sound_treshold=0 # change this value

while True: 
  #Following commands control the state of the output
  #GPIO.output(pin, GPIO.HIGH)
  #GPIO.output(pin, GPIO.LOW)
  for i in range(5):
    GPIO.output(LED_PIN, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(LED_PIN, GPIO.LOW)
    time.sleep(0.5)

  # get reading from adc 
  # mcp.read_adc(adc_channel)