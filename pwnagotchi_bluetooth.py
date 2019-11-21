#!/usr/bin/env python3

# This is a quick daemon that interfaces a Pwnagotchi with a mobile device
# running the Bluedot (https://github.com/martinohanlon/BlueDot) Python
# module.  The reason I wrote this is so that I can cleanly shut down my
# Pwnagotchi without having to yank the power.

# This utility has to be run as the root user.

# Incidentally, here's how to pair a RasPi with an Android phone.
# RasPi:
# * `sudo bluetoothctl`
# * Type the following commands one at a time:
# ** discoverable on
# ** pairable on
# ** agent on
# ** default-agent
# Phone:
# * Settings -> Connections
# * Make sure Bluetooth is turned on.
# * Bluetooth (tap on the word not the switch)
# * Tap on your RasPi in the list.
# RasPi:
# * Type "yes"
# * `quit`

# source: https://bluedot.readthedocs.io/en/latest/pairpiandroid.html

# by: The Doctor [412/724/301/703/415/510] <drwho at virtadpt dot net>
# license: GPLv3

import os
import platform
import subprocess
import sys

from bluedot import BlueDot

# Localhost name.
hostname = ""

# Handle to a Bluedot interface.
bd = None

# Make sure we're running as the root user.  We have to be to access the
# Bluetooth interface.  ABEND if we're not.
if os.getuid() != 0:
    print("ERROR: We're not running as root.  ABENDing.")
    sys.exit(1)

# Save the hostname.
hostname = platform.node()

# Command we want to run.  In this case, shutting down the RasPi.
command = ["/sbin/shutdown", "-h", "now"]

# Message that we're going to display to the user.
message = "Shutting down {} now."

# Instantiate a Bluedot object and connect to my phone.
try:
    bd = BlueDot()
    print("Successfully associated {} with mobile device.".format(hostname))
except:
    print("Unable to associate with mobile device.  ABENDing.")
    sys.exit(1)

# Wait for the user to press the big blue button on the phone.
bd.wait_for_press()

# Do the thing.
print(message.format(hostname))
subprocess.run(command)

# Clean up after ourselves.
sys.exit(0)

