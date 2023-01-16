import ds1621
import network
import ustruct
import utime
import ubinascii
from umqtt.simple import MQTTClient


# Connect to Wi-Fi
wlan = network.WLAN(network.STA_IF)
if not wlan.isconnected():
    print("Not connected to Wi-Fi. Exiting...")
    # utilisez sys.exit() pour quitter le programme
    sys.exit()

# Initialisation du capteur DS1621
sensor = ds1621.DS1621(scl=(22), sda=(21))

# Get the ESP32's MAC address
mac = ubinascii.hexlify(wlan.config('mac'),':').decode()

# Configuration du client MQTT
client = MQTTClient("ESP32_"+ mac, "ip_raspi", user_MQTT, password_MQTT)
client.connect()

while True:
    # Lire la température
    temperature = sensor.read_temperature()
    #publier la temperature to MQTT broker
    print(temperature)
    client.publish("temp/ds1621", str(temperature))
    utime.sleep(5)
