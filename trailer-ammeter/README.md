I have a Beelink minicomputer, which runs off of 12V power. But if I plug it in to the 12V, the 7.5A fuse blows. There's other stuff on that circuit, but I want to figure out how much the computer actually draws.

This isn't super urgent because the minicomputer is powered off of the 120V, while the trailer is on shore power, and there's a 12V battery backup for when it's moving. An interesting fact: the computer will get through the bios checks and _start_ booting on the 12V adapter for the battery backup, but won't fully boot. However, it boots fine when plugged in the the battery backup. I think this means that the backup batteries are able to source more amperage that the adapter, and the minicomputer only has extravagant power needs at boot time.

It would be nice to know what those extravagant needs are and whether the circuit is close to having enough or just not.

I've thought about getting a panel ammeter:
https://www.adafruit.com/product/574

But I actually want to capture a pulse, so maybe the solution is something like:
https://www.homemade-circuits.com/arduino-dc-digital-ammeter/

[Comparison table for ESP8266/ESP32/ESP32-S2/ESP32-S3/ESP32-C3/ESP32-C6](https://gist.github.com/sekcompsci/2bf39e715d5fe47579fa184fa819f421#comparison-table-for-esp8266esp32esp32-s2esp32-s3esp32-c3esp32-c6)

