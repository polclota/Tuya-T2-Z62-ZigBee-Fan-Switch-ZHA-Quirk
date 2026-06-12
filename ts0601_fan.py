import zigpy.types as t
from zhaquirks.tuya.builder import TuyaQuirkBuilder
from zigpy.quirks.v2 import EntityType
from zigpy.quirks.v2.homeassistant import UnitOfTime


class PowerOnState(t.enum8):
    """Tuya power on state enum."""

    Off = 0x00
    On = 0x01


class FanSpeed(t.enum8):
    """Fan speed enum."""

    Speed_1 = 0x00
    Speed_2 = 0x01
    Speed_3 = 0x02
    Speed_4 = 0x03
    Speed_5 = 0x04


(
    TuyaQuirkBuilder("_TZE28C1000000_z5jz7wpo", "TS0601")
    # Switch
    .tuya_switch(
        dp_id=1,
        attribute_name="on_off",
        entity_type=EntityType.STANDARD,
        translation_key="on_off",
        fallback_name="switch",
    )
    # Countdown timer (seconds)
    .tuya_number(
        dp_id=2,
        attribute_name="countdown_timer",
        type=t.uint16_t,
        entity_type=EntityType.STANDARD,
        unit=UnitOfTime.SECONDS,
        min_value=0,
        max_value=43200,
        step=1,
        translation_key="countdown_timer",
        fallback_name="countdown",
    )
    # Fan speed
    .tuya_enum(
        dp_id=3,
        attribute_name="fan_speed",
        enum_class=FanSpeed,
        translation_key="fan_speed",
        fallback_name="Fan Speed",
    )
    # Power-on state
    .tuya_enum(
        dp_id=11,
        attribute_name="power_on_state",
        enum_class=PowerOnState,
        translation_key="power_on_state",
        fallback_name="Power On State",
    )
    .skip_configuration()
    .add_to_registry()
)
