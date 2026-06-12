Device: Tuya T2-Z62
Model: TS0601
Manufacturer: _TZE28C1000000_z5jz7wpo

Features:
- On/Off switch
- 5-speed fan control
- Countdown timer
- Power-on state

Tested and working with ZHA.
Fan speed requires enum mapping (Speed_1 ... Speed_5).

Known limitation:

Changing fan speed (DP3) powers on the fan, but the DP1 switch state is not updated by the device firmware.

Example:
- Switch OFF
- Select Speed_1
- Fan starts
- Switch entity still shows OFF

This appears to be a device firmware behavior rather than a quirk issue.

Additional observation:

Commands work correctly (switch, countdown and fan speed), however state synchronization appears incomplete.

When changing fan speed, the physical device responds correctly, but the corresponding entities in ZHA are not always updated to reflect the actual device state.

Likewise, changes occurring on the device itself are not consistently reflected back to ZHA.

This suggests that some datapoints may not be reported by the device, or that additional datapoints are required to correctly track the running state.
