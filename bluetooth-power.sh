#!/usr/bin/env bash

# Wrapper script that starts up the Pwnagotchi Bluetooth utility, suitable for
# starting inside of a Screen session or something.  Must be run as the root
# user with sudo or something because Bluetooth interaction on the Pwnagotchi
# is a privileged operation.

# by: The Doctor [412/724/301/703/415/510] <drwho at virtadpt dot net>
# license: GPLv3

# Make sure we are where we think we are.
cd /home/pi/pwnagotchi-bt-power

# Fire up the virtualenv.
. env/bin/activate

# Start the daemon.
./pwnagotchi_bluetooth.py

