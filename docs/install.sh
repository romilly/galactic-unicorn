#! /bin/bash
cd /home/romilly/git/active/pico-code/src/pico_code/picow
mpremote cp network_connection.py :
mpremote cp blinker.py :
mpremote cp secrets.py :
cd mqtt
mpremote cp mqtt_installer.py :
mpremote exec 'import mqtt_installer'