import time
import WIFI_CONFIG
import network

from umqtt.simple import MQTTClient

from galactic import GalacticUnicorn
from picographics import PicoGraphics, DISPLAY_GALACTIC_UNICORN

from network_connection import connect
from secrets import SSID, PASSWORD # SSID, PASSWORD for network connection

MQTT_HOST = 'mqtt.cheerlights.com'
# MQTT_HOST = 'trewarva'

def hex_to_rgb(hex):
    return tuple(int(hex[i:i + 2], 16) for i in (1, 3, 5))


def display(topic, message):
    rgbs = message.decode('UTF8')
    rgb3 = hex_to_rgb(rgbs)
    global history
    history = history[1:] + [rgb3]
    show_block()
    galactic.update(graphics)


def show_block():
    for block in range(8):
        offset = 5 + block*6
        rgb3 = history[block]
        rgb = graphics.create_pen(*rgb3)
        graphics.set_pen(rgb)
        for x in range(6):
            for y in range(11):
                graphics.pixel(x + offset, y)


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

def run():
    connect(SSID, PASSWORD)
    mc = MQTTClient('ROM-GU', MQTT_HOST)
    mc.connect()
    print('connected to %s' % MQTT_HOST)
    mc.set_callback(display)
    mc.subscribe('cheerlightsRGB')
    while True:
        mc.wait_msg()
        time.sleep(0.001)


BLACK = (0,0,0)
history = []
for i in range(8):
    history.append(BLACK)
galactic = GalacticUnicorn()
graphics = PicoGraphics(DISPLAY_GALACTIC_UNICORN)
run()


