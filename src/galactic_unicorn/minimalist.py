import network
import time
from umqtt.simple import MQTTClient
from secrets import SSID, PASSWORD # SSID, PASSWORD for network connection

from galactic import GalacticUnicorn

MQTT_HOST = 'mqtt.cheerlights.com'


def connect(ssid, password, max_wait=10):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    while max_wait > 0:
        if wlan.status() < 0 or wlan.status() >= 3:
            break
        max_wait -= 1
        time.sleep(1)
    if wlan.status() != 3:
        raise RuntimeError('network connection failed')
    return wlan

def display_level(topic, message):
    print(message)

def run():
    print('starting')
    connect(SSID, PASSWORD)
    print('connected to network')
    mc = MQTTClient('ROM-GU', MQTT_HOST)
    mc.connect()
    print('connected to %s' % MQTT_HOST)
    galactic = GalacticUnicorn() # if this is commented out, everything works
    mc.set_callback(display_level)
    print('callback set')
    mc.subscribe('cheerlightsRGB')
    print('subscribed')
    while True:
        print('waiting for summat')
        mc.wait_msg()
        time.sleep(0.001)


OUTPUT_WHEN_WORKING = """
MicroPython 9dfabcd on 2022-10-19; Raspberry Pi Pico W with RP2040
Type "help()" for more information.
>>> %Run -c $EDITOR_CONTENT
starting
connected to network
connected to mqtt.cheerlights.com
callback set
subscribed
waiting for summat
b'#ffa500'
waiting for summat
"""

OUTPUT_WHEN_NOT_WORKING = """
MicroPython 9dfabcd on 2022-10-19; Raspberry Pi Pico W with RP2040
Type "help()" for more information.
>>> %Run -c $EDITOR_CONTENT
starting
connected to network
connected to mqtt.cheerlights.com
callback set
"""

run()
