# esphome Bluetooth LE relay

There are some sensors in my [trailer](https://tourtoise.quest) that Home Assistant can't talk to, for some reason. I'm trying a [Adafruit ESP32 Feather V2](https://www.adafruit.com/product/5400) to talk to them.

### [Power Watchdog](https://hughesautoformers.com/power-watchdog-smart-surge-protectors/)
The setup for this is a little fiddly, but it works a charm:
https://github.com/tango2590/Hughes-Power-Watchdog

### Mopeka Propane Sensor
In theory, the support for this is in [esphome](https://esphome.io/components/sensor/mopeka_std_check.html), but I haven't gotten it working. It's possible that I have a Mopeka sensor that is neither the Standard Check or the Pro Check, but I'll have to uninstall the propane cylinder to figure that out.

### Enclosure
Does nobody make a minimal enclosure for a Feather? I can't find one. Maybe everyone but me has a 3D printer and just makes a new one for each project?

The [Polycase KT-35](https://www.polycase.com/kt-35) is pretty close to the right size. Using an end-mill style bit with my Dremel produced a slot that the USB-C connector fits in, and the fit is tight enough against the screw bosses that the Feather is held in place.

<a data-flickr-embed="true" href="https://www.flickr.com/photos/aneel/53080477009/in/album-72177720310129468/" title="Untitled"><img src="https://live.staticflickr.com/65535/53080477009_5df4fae783_w.jpg" width="300" height="400" alt="Untitled"/></a> <a data-flickr-embed="true" href="https://www.flickr.com/photos/aneel/53079713437/in/album-72177720310129468/" title="Untitled"><img src="https://live.staticflickr.com/65535/53079713437_3cda248bba_w.jpg" width="300" height="400" alt="Untitled"/></a> 