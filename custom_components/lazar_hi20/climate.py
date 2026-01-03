from homeassistant.components.climate import ClimateEntity
from homeassistant.components.climate.const import HVACMode, ClimateEntityFeature
from .const import DOMAIN

async def async_setup_entry(hass, entry, async_add_entities):
    coordinator = hass.data[DOMAIN][entry.entry_id]
    async_add_entities([LazarClimate(coordinator)])

class LazarClimate(ClimateEntity):
    _attr_name = "Lazar HI20"
    _attr_unique_id = "lazar_hi20_climate"
    _attr_supported_features = ClimateEntityFeature.TARGET_TEMPERATURE
    _attr_temperature_unit = "°C"
    _attr_min_temp = 15
    _attr_max_temp = 55

    def __init__(self, coordinator):
        self.coordinator = coordinator

    @property
    def current_temperature(self):
        return self.coordinator.data["stat"]["temps"]["out"] / 10

    @property
    def target_temperature(self):
        return self.coordinator.data["params"]["cwu"]["tsetcomf"] / 10

    async def async_set_temperature(self, **kwargs):
        temp = int(kwargs["temperature"] * 10)
        await self.coordinator.api.set_param("tsetcomf", temp)

    @property
    def hvac_modes(self):
        return [HVACMode.HEAT, HVACMode.COOL, HVACMode.OFF]

    @property
    def hvac_mode(self):
        return HVACMode.HEAT if self.coordinator.data["params"]["onoff"] else HVACMode.OFF

    async def async_set_hvac_mode(self, hvac_mode):
        await self.coordinator.api.set_param("onoff", "on" if hvac_mode != HVACMode.OFF else "off")