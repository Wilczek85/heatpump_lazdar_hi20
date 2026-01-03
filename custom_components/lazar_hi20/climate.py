from homeassistant.components.climate import ClimateEntity
from homeassistant.components.climate.const import HVACMode
from .const import DOMAIN

async def async_setup_entry(hass, entry, async_add_entities):
    coordinator = hass.data[DOMAIN][entry.entry_id]
    async_add_entities([LazarClimate(coordinator)])

class LazarClimate(ClimateEntity):
    _attr_name = "Lazar HI20 Climate"
    _attr_unique_id = "lazar_hi20_climate"

    def __init__(self, coordinator):
        self.coordinator = coordinator

    @property
    def temperature_unit(self):
        return "°C"

    @property
    def current_temperature(self):
        return self.coordinator.data["stat"]["temps"]["out"] / 10

    @property
    def hvac_mode(self):
        mode = self.coordinator.data["params"]["mode"]
        return {0: HVACMode.HEAT, 1: HVACMode.COOL, 2: HVACMode.HEAT}.get(mode)

    @property
    def hvac_modes(self):
        return [HVACMode.HEAT, HVACMode.COOL]