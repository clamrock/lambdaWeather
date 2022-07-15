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
<<<<<<< HEAD

import asyncio
import aiohttp
import pynws
=======
from .nws import *
>>>>>>> 750a6007f8ec01a37e55a81614bee0a958ceb52e

def setup_platform( hass: HomeAssistant, config: ConfigType, add_entities: AddEntitiesCallback, discovery_info: DiscoveryInfoType | None = None) -> None:
    """Set up the sensor platform."""
    sensors=[]
    
    sensors.append(lambdaWeatherSensor("SensorOne"))
    sensors.append(lambdaWeatherSensor("SensorTwo"))
    
    add_entities(sensors)


def ctof(temp):
    return ((temp * (9 / 5)) + 32)


def calculateApparent(temp, heat, wind):
    if ctof(temp) > 80:
        return ctof(heat)
    if ctof(temp) < 51:
        return ctof(wind)
    return ctof(temp)


async def example():
    async with aiohttp.ClientSession() as session:
        nws = pynws.SimpleNWS(*DETROIT, USERID, session)
        await
        nws.set_station()
        await
        nws.update_observation()
        # await nws.update_forecast()
        # await nws.update_alerts_forecast_zone()
        # await nws.update_detailed_forecast()

        current_temp = nws.observation['temperature']
        current_heatIndex = nws.observation['heatIndex']
        current_windChill = nws.observation['windChill']

        # print("{}, {}, {}".format(current_temp, current_heatIndex, current_windChill))

        apparentTemp = calculateApparent(current_temp, current_heatIndex, current_windChill)

        # print("Apparent temp = {}".format(apparentTemp))
        return apparentTemp

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
