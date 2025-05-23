"""Utils."""

from __future__ import annotations

import json
import uuid
from json import JSONDecodeError
from typing import Any


def is_number(string: str) -> bool:
    """String is a number."""
    try:
        float(string)
    except ValueError:
        return False

    return True


def find_dict_with_keyvalue_in_json(
    json_dict: list[dict[str, Any]], key_in_subdict: str, value_to_find: Any
) -> Any:
    """Searches a json_dict for the key key_in_subdict that matches value_to_find
    :param json_dict: dict
    :param key_in_subdict: str - the name of the key in the subdict to find
    :param value_to_find: str - the value of the key in the subdict to find
    :return: The subdict to find.
    """
    for data_group in json_dict:
        if data_group.get(key_in_subdict) == value_to_find:
            return data_group

    raise KeyError(f"`{key_in_subdict}` with value `{value_to_find}` not found in data")


def load_or_create_uuid(filename: str) -> uuid.UUID | None:
    """Load or create a uuid for the device."""
    try:
        with open(filename, encoding="utf-8") as fptr:
            jsonf = json.loads(fptr.read())
            return uuid.UUID(jsonf["nexia_uuid"], version=4)
    except (JSONDecodeError, FileNotFoundError):
        return _create_uuid(filename)
    except (ValueError, AttributeError):
        return None


def _create_uuid(filename):
    """Create a uuid for the device."""
    with open(filename, "w", encoding="utf-8") as fptr:
        new_uuid = uuid.uuid4()
        fptr.write(json.dumps({"nexia_uuid": str(new_uuid)}))
        return new_uuid


def find_humidity_setpoint(setpoint: float) -> float:
    """Find the closest humidity setpoint."""
    return round(0.05 * round(setpoint / 0.05), 2)
