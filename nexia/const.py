"""Top-level package for Nexia."""

__version__ = "0.1.0"

ROOT_URL = "https://www.mynexia.com"
MOBILE_URL = f"{ROOT_URL}/mobile"

DEFAULT_DEVICE_NAME = "Home Automation"

PUT_UPDATE_DELAY = 0.5

HOLD_PERMANENT = "permanent_hold"
HOLD_RESUME_SCHEDULE = "run_schedule"

FAN_MODE_AUTO = "auto"
FAN_MODE_ON = "on"
FAN_MODE_CIRCULATE = "circulate"
FAN_MODES = [FAN_MODE_AUTO, FAN_MODE_ON, FAN_MODE_CIRCULATE]

OPERATION_MODE_AUTO = "AUTO"
OPERATION_MODE_COOL = "COOL"
OPERATION_MODE_HEAT = "HEAT"
OPERATION_MODE_OFF = "OFF"
OPERATION_MODES = [
    OPERATION_MODE_AUTO,
    OPERATION_MODE_COOL,
    OPERATION_MODE_HEAT,
    OPERATION_MODE_OFF,
]

# The order of these is important as it maps to preset#
PRESET_MODE_HOME = "Home"
PRESET_MODE_AWAY = "Away"
PRESET_MODE_SLEEP = "Sleep"
PRESET_MODE_NONE = "None"

SYSTEM_STATUS_COOL = "Cooling"
SYSTEM_STATUS_HEAT = "Heating"
SYSTEM_STATUS_WAIT = "Waiting..."
SYSTEM_STATUS_IDLE = "System Idle"

AIR_CLEANER_MODE_AUTO = "auto"
AIR_CLEANER_MODE_QUICK = "quick"
AIR_CLEANER_MODE_ALLERGY = "allergy"
AIR_CLEANER_MODES = [
    AIR_CLEANER_MODE_AUTO,
    AIR_CLEANER_MODE_QUICK,
    AIR_CLEANER_MODE_ALLERGY,
]

HUMIDITY_MIN = 0.35
HUMIDITY_MAX = 0.65

UNIT_CELSIUS = "C"
UNIT_FAHRENHEIT = "F"

ALL_IDS = "all"
