#electronics #feather #esp8266 #esphome

Interesting... the temperature sensors stopped providing data long before the battery voltage was critically low. They stop providing values when the battery hits 3.5V, though their [datasheet](https://cdn-shop.adafruit.com/datasheets/DS18B20.pdf) says they'll run down to 3.0V.

![[battery-curve.png]]

Maybe the 3.3V regulated output from the Feather is significantly lower than the battery voltage? At 2.5V, the Feather stopped sending data.

I'm surprised that it's not getting some sun at nearly 10 am.

Sources on the net say that these batteries _really_ don't like being drained past 2.9 V, so we should probably fix that...

---

Figured out how to use the LEDs on the Feather Huzzah:
```
output:
  - id: red_led
    platform: esp8266_pwm
    pin: GPIO0
    inverted: True

  - id: blue_led
    platform: esp8266_pwm
    pin: GPIO2
    inverted: True
```

Figured out how to set up a toggle in HA that gets reflected on the esphome:
```
binary_sensor:
  - platform: homeassistant
    id: prevent_deep_sleep
    name: Prevent Deep Sleep
    entity_id: input_boolean.prevent_deep_sleep
    on_state:
      then:
        - if:
            condition:
              binary_sensor.is_on: prevent_deep_sleep
            then:
              - output.turn_on: blue_led
            else:
              - output.turn_off: blue_led
```

> Lesson Learned: if you put the Feather into a loop where it keeps triggering deep sleep, it's hard to reprogram it. Break the connection between GPIO16 and RST, and it should stop sleeping

Spent a bunch of time trying to figure out how to effectively use deep sleep. The framework is tantalizingly close to supporting a nice event-driven pattern, but I ended up needing to write a linear script instead.

Challenges:
1. First value read from HA for "Prevent Deep Sleep" toggle (or anything) doesn't trigger the `on_value` or `on_value_range` handlers. They seem to only fire when a value changes while the esphome device is paying attention to it.
2.  There seems to be a missing check for a state being undefined because it hasn't been received from the API yet.

Here's what I ended up with...
```
esphome:
  name: pool-8266
  # Make sure we don't immediately go back into deep sleep after waking
  on_boot:
    - deep_sleep.prevent: nap

# Configure the duty cycle, when it's OK to sleep. I want a wakeup every minute
# And 15s seems like enough for things to all settle. Maybe it can be reduced
deep_sleep:
  id: nap
  run_duration: 15s
  sleep_duration: 45s

# This is a Helper configured in HA so that I have a way to make sure I can
# deliver an OTA update
binary_sensor:
  - platform: homeassistant
    id: prevent_deep_sleep
    name: Prevent Deep Sleep
    entity_id: input_boolean.prevent_deep_sleep

# The guts of it...
interval:
  - interval: 5s
    then:
      # Status blink
      - output.turn_on: blue_led
      - delay: .5s
      - output.turn_off: blue_led
      - logger.log: "Considering nap"
      # This 'if' could be much more compact using 'and', but I broke it out
      # For logging purposes 
      - if:
          condition:
            api.connected:
          else:
            # Since we can't check if prevent_deep_sleep is 'unknown'...
            - logger.log: "No Nap: Not connected to API"
            - deep_sleep.prevent: nap
          then:
            if:
              condition:
                binary_sensor.is_off: prevent_deep_sleep
              else:
                - logger.log: "No Nap: Prevent Deep Sleep is on"
                - deep_sleep.prevent: nap
              then:
                if:
                  condition:
                    sensor.in_range:
                      id: battery_voltage
                      below: 4.0
                  else:
                    # Don't bother sleeping if we're charging
                    - logger.log: "No Nap: Battery Charging"
                    - deep_sleep.prevent: nap
                  then:
                    - logger.log: "Nap Allowed"
                    - deep_sleep.allow: nap
```