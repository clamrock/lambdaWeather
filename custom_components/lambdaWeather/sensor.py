"""Platform for sensor integration."""
from __future__ import annotations

from homeassistant.components.sensor import (
    SensorDeviceClass,
    SensorEntity,
    SensorStateClass,
)
from homeassistant.const import TEMP_CELSIUS
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType, DiscoveryInfoType
import random
from nws import *

def setup_platform( hass: HomeAssistant, config: ConfigType, add_entities: AddEntitiesCallback, discovery_info: DiscoveryInfoType | None = None) -> None:
    """Set up the sensor platform."""
    sensors=[]
    
    sensors.append(lambdaWeatherSensor("SensorOne"))
    sensors.append(lambdaWeatherSensor("SensorTwo"))
    
    add_entities(sensors)


class lambdaWeatherSensor(SensorEntity):
    """Representation of a Sensor."""
    def __init__(self, _name):

        self._attr_name = _name
        self._attr_native_unit_of_measurement = TEMP_CELSIUS
        self._attr_device_class = SensorDeviceClass.TEMPERATURE
        self._attr_state_class = SensorStateClass.MEASUREMENT

    def update(self) -> None:
        """Fetch new state data for the sensor.
        This is the only method that should fetch new data for Home Assistant.
        """
        loop = asyncio.get_event_loop()
        apparentTemp = loop.run_until_complete(example())

        self._attr_native_value = apparentTemp
