Probably not. Apple shifts the IDs on these so that they can't be recognized. Might be able to figure out how many are nearby, but not which is which.

[ESPresense](https://espresense.com/beacons) comes the closest: "We can only count how many are currently not connected to a phone" It's not clear to me if "connected to a phone" means set up for Find My, or just that a phone is nearby and interacting.

It would actually probably be useful to know when AirTags (cats) move from zone to zone, so maybe it's worth looking into anyway?

But maybe it won't work because the AirTags are no longer advertising? https://learn.adafruit.com/introduction-to-bluetooth-low-energy/gap

https://adamcatley.com/AirTag#advertising-data

https://github.com/seemoo-lab/openhaystack
#### Advertising data

This section describes the Bluetooth activity when the AirTag is registered to the FindMy network.

- Address type: Random Static (changes daily, first 6 bytes of public key)
- Advertising PDU type: Connectable undirected (ADV_IND)
- Advertising period: 2000ms
- Advertising transmit time: 4ms (including wake up)

|Byte #|Value|Description|
|---|---|---|
|0|0x1E|Advertising data length: 31 (the maximum allowed)|
|1|0xFF|Advertising data type: Manufacturer Specific Data|
|2-3|0x004C|Apple’s [company identifier](https://www.bluetooth.com/specifications/assigned-numbers/company-identifiers/)|
|4|0x12|Apple payload type to indicate a FindMy network broadcast|
|5|0x19|Apple payload length (31 - 6 = 25 = 0x19)|
|6|0x10|Status byte|
|7-29|Varies|EC P-224 public key used by FindMy network. Changes daily|
|30|0-3|Upper 2 bits of first byte of ECC public key|
|31|Varies|Crypto counter value? Changes every 15 minutes to a random value|

According to Apple’s [documentation](https://support.apple.com/en-gb/guide/security/sece994d0126/1/web/1#:~:text=P-224%20public%20key%20Pi%20obtained%20from%20the%20Bluetooth%20payload), the BLE advertising data contains a NIST EC P-224 public key. This key would be at least 28+1 bytes long but only 23+1 bytes in the advertising data ever change. The other 6 bytes are cleverly used as the device’s Bluetooth address. This is how Apple fits a public key in a single BLE packet. As demonstrated [here](https://github.com/seemoo-lab/openhaystack/blob/ffc5170ea4b4ceb1ad84e4f89324d6e666ffc7c3/Firmware/ESP32/main/openhaystack_main.c#L107).

There also seems to be a way to predict part of the future Bluetooth address, but this needs more investigation.

Apple presumably uses authentication to stop non-Apple devices connecting to the AirTag, as connections are terminated by the AirTag shortly after connecting.

### Navigation
* [README](README.md)
* [2023-09-24 AirTag tracking?](2023-09-24%20AirTag%20tracking%3F.md)

