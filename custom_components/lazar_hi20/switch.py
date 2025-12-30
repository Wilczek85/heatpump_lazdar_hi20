from homeassistant.components.switch import SwitchEntity
from .const import DOMAIN

async def async_setup_entry(hass, entry, async_add_entities):
    coordinator = hass.data[DOMAIN][entry.entry_id]
    api = coordinator.api
    async_add_entities([LazarPowerSwitch(api, coordinator)])

class LazarPowerSwitch(SwitchEntity):
    _attr_name = "Lazar Hi20 Power"

    def __init__(self, api, coordinator):
        self.api = api
        self.coordinator = coordinator

    @property
    def is_on(self):
        return self.coordinator.data["params"]["onoff"] == 1

    async def async_turn_on(self, **kwargs):
        await self.hass.async_add_executor_job(self.api.set_param, "onoff", 1)

    async def async_turn_off(self, **kwargs):
        await self.hass.async_add_executor_job(self.api.set_param, "onoff", "off")
