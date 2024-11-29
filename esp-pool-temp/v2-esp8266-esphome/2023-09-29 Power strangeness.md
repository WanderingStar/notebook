| Date             | Event                                                                |
| ---------------- | -------------------------------------------------------------------- |
| 2023-09-26 22:54 | Battery hits 3.51 V, stops sending data                              |
| 2023-09-27 13:20 | Another data point at 3.51 V. No charging or discharging in between? |
| 2023-09-28 20:30 | Brought the unit inside                                              |

Inside:
1. Unplugged the solar DC cable
2. Plugged in USB-C (Adrienne's laptop charger) to the charging board. Charge light did not come on
3. Unplugged Feather. Charge light came on
4. Plugged Feather back in. Charge light went off
5. Unplugged Feather. Charge light came on
6. Plugged Feather into laptop. LEDs came on
7. `esphome logs pool-8266.yaml` found the device on serial, spat out some logs
8. Plugged Feather back into board. Charge light stayed on
9. Unplugged USB-C. Feather reported 3.58 V, kept running.

So maybe the Feather is getting into a bad state if the battery is low enough and something about that interferes with the charging circuit?

### Navigation
* [README](README.md)
* [2023-07-23 ESP8266 esphome](2023-07-23%20ESP8266%20esphome.md)
* [2023-07-29 Power Problems](2023-07-29%20Power%20Problems.md)
* [2023-07-30 Deep Sleep](2023-07-30%20Deep%20Sleep.md)
* [2023-07-31 MQTT](2023-07-31%20MQTT.md)
* [2023-08-01 Tweaks](2023-08-01%20Tweaks.md)
* [2023-09-29 Power strangeness](2023-09-29%20Power%20strangeness.md)

