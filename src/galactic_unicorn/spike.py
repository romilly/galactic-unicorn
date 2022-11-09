from galactic import GalacticUnicorn
from picographics import PicoGraphics, DISPLAY_GALACTIC_UNICORN

from umqtt.simple import MQTTClient
from network_connection import connect
from secrets import SSID, PASSWORD

def hex_to_rgb(hex):
    return tuple(int(hex[i:i + 2], 16) for i in (1, 3, 5))

def display_level(topic, message):
    print(message)
    rgbs = message.decode('UTF8')
    rgb3 = hex_to_rgb(rgbs)
    # graphics.set_pen(graphics.create_pen(*rgb3))
    # for x in range(11):
    #    for y in range(4):
    #        graphics.pixel(x,y)
    #galactic.update(graphics)

def run():
    print('starting')
    connect(SSID, PASSWORD)
    print('connected to network')
    mc = MQTTClient('ROM-GU', MQTT_HOST)
    mc.connect()
    print('connected to %s' % MQTT_HOST)
    galactic = GalacticUnicorn()
    print('gu created')
    mc.set_callback(display_level)
    print('callback set')
    mc.subscribe('cheerlightsRGB')
    print('subscribed')
    while True:
        print('waiting for summat')
        mc.wait_msg()
MQTT_HOST = 'mqtt.cheerlights.com'
# galactic = GalacticUnicorn()
# graphics = PicoGraphics(DISPLAY_GALACTIC_UNICORN)
# graphics.set_pen(graphics.create_pen(0, 255, 0))

run()
