# galactic-unicorn

Experiments with the pre-production galactic unicorn.

This includes a [cheerlights](https://cheerlights.com/) client.
This version shows cheerlights history: up to 8 recent colours in blocks 6x11.

The flyer game is a work in progress, and not yet usable.

# Installation

You'll need to

1. Connect your unicorn to the internet
2. Import upip, which is built-in to recent picow #micropython images
3. Run `upip.install('umqtt.simple')`.
1. Copy this repository to a directory of your choice by cloning or downloading/unzipping it.
2. Copy`cheerlights.py` and `WIFI_CONFIG.py` from `src/galactic_unicorn` to your Unicorn, 
3. Edit and save `WIFI_CONFIG.py` to contain your network id and password.
5. Run `cheerlights.py` using Thonny, mpremote or any other tool of your choice.

Here's the sort of thing you'll see:

![Cheerlights History Display](docs/img/cheerlight-blocks.jpg)



