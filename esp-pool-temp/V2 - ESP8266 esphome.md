The ESP32-S2 and the TFT seemed like overkill for this project, and I had a bunch of 
[Older ESP8266 boards around](https://learn.adafruit.com/adafruit-feather-huzzah-esp8266), so I figured I'd try one of them out.

I also wanted to play with [esphome](https://esphome.io/). I was already pushing the data from the sensor to Home Assistant via MQTT. Why not integrate directly?

### Installing esphome

I blundered around with this a bit. It turns out the Feather Huzzah 8266 board I was using needed a [serial driver](https://www.silabs.com/developers/usb-to-uart-bridge-vcp-drivers) (which [Adafruit's excellent guide mentions](https://learn.adafruit.com/adafruit-feather-huzzah-esp8266/using-nodemcu-lua)). Even with that, I found the esphome docs confusing. Their site is organized around each integration, and doesn't have a lot of big-picture information. I spent the longest time wondering "why would I actually want to use esphome?"

What I ended up doing that worked well: 
1. Make a directory/repo for esphome configs 
2. `python3 -m pip install virtualenv`
3. `python3 -m virtualenv venv`
4. `source venv/bin/activate`
5. `pip install wheel esphome`
6. `esphome dashboard .`
Use the web interface at http://localhost:6052 to add a new device. Note: wants to be done in Chrome for WASM access to the serial port.

> Lesson Learned: That conveniently short USB micro cable that you have lying around? Might be power only because it came with a knockoff camera battery charger. When you plug the board into the Mac, it should prompt you whether to allow the accessory to connect. If it doesn't, try a different cable.

2023-07-23

Put my esphome build on a Huzzah, went to plug it in... realized that the fact that I used the _reverse_ TFT feather for V1 means that the headers need to go on the _other_ side of the board. Luckily, I have a bunch of Huzzahs, so I soldered one up reversed.

Got it all set up. The Dallas 1-wire support finds the sensors with no problem. Reports data to Home Assistant nicely. Great?

![Graph showing data intermittently gathered](intermittent.png)

Not great. I suspect that V2 is chewing through the whole battery. I've been going out there and resetting it daily, and have tried moving the solar panel into sunnier spots, but it hasn't really helped.

Hypotheses:
1. The ESP8266 is just more power hungry than the ESP32-S2
2. The esphome code is keeping it more active than the circuit python code did
3. Something in the circuit python code is triggering a sleep mode (maybe the `time.sleep`?)

2023-07-29

The ESP8266 needs RST connected to GPIO 16 to support deep sleep mode, and, unlike the S2 Feather, the Huzzah doesn't have a battery monitor. Happily, Adafruit [has a suggestion for that](https://learn.adafruit.com/using-ifttt-with-adafruit-io/wiring#battery-tracking). It means giving up the only Analog to Digital converter on the Huzzah, but we weren't using it for anything here anyway. Setting up the esphome config for this was pretty straightforward. I measured the actual voltage and the fraction returned by the voltage divider, and set up a filter to scale the values. Hopefully this will let me confirm if the power is indeed the problem.

The protoboard is getting increasingly crowded, but I cleaned up some of the badly-clipped leads with a new pair of flush cutters.

If the power is the problem, maybe we can...
- Use the deep sleep mode
- Use MQTT to push the values rather than the home assistant API pulling them ([see](https://ncrmnt.org/2021/12/06/optimizing-esp8266-esphome-for-battery-power-and-making-an-ice-bath-thermometer-as-well/))