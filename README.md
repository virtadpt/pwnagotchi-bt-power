# pwnagotchi-bt-power
A very simple, silly utility which monitors the Bluetooth interface of a Pwnagotchi and cleanly shuts it down on receiving a command from a mobile phone.

Relies upon the [Bluedot Python module](https://bluedot.readthedocs.io/en/latest/) and [Android app](https://play.google.com/store/apps/details?id=com.stuffaboutcode.bluedot&hl=en_US) to function.

What I was trying to do is shut my [Pwnagotchi](https://pwnagotchi.ai/) off without just yanking the power and gambling with corrupting the microSD card every time.  Rather than shoehorn in a button to connect to the GPIO pins and figure out which ones weren't being used by [the display I have](https://www.waveshare.com/wiki/2.13inch_e-Paper_HAT) I decided to make use of the Bluetooth interface on my mobile.

The instructions are simple:

* Install the Python 3 virtualenv utility.
  * `sudo apt-get update`
  * `sudo apt-get install python-virtualenv`
* Install the utility.
  * Clone this repo onto your Pwnagotchi.
  * `cd pwnagotchi-bt-power'`
  * `python3 -mvenv env`
  * `. env/bin/activate`
  * `pip install bluedot`
* Set the utility to start up on boot.
  * [I use GNU Screen for this.](https://drwho.virtadpt.net/archive/2017-06-11/restarting-a-screen-session-without-manual-intervention)  I've included the `bluetooth-power.sh` script to make life easier for you.
  * Be sure that the startup script runs as the root user!
* [Pair your phone with your Pwnagotchi.](https://bluedot.readthedocs.io/en/latest/pairpiandroid.html)
  * RasPi
    * `sudo bluetoothctl`
    * Type the following commands one at a time:
      * `discoverable on`
      * `pairable on`
      * `agent on`
      * `default-agent`
  * Phone
    * Settings -> Connections
    * Make sure Bluetooth is turned on.
    * Bluetooth (tap on the word not the switch)
    * Tap on your RasPi in the list.
  * RasPi:
    * 'yes'
    * `quit`
* Reboot your Pwnagotchi.

To shut down your Pwnagotchi:

* Open the Bluedot app on your phone.
* Tap on your Pwnagotchi in the list.
* Tap the big blue button.

