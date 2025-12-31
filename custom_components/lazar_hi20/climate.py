from homeassistant.components.climate import ClimateEntity
from homeassistant.components.climate.const import (
    HVACMode,
    ClimateEntityFeature,
)
from homeassistant.helpers.update_coordinator import CoordinatorEntity
from homeassistant.const import UnitOfTemperature
from .const import DOMAIN

async def async_setup_entry(hass, entry, async_add_entities):
    coordinator = hass.data[DOMAIN][entry.entry_id]

    entities = [
        LazarCWUClimate(coordinator),
        LazarCOClimate(coordinator, 0),
        LazarCOClimate(coordinator, 1),
    ]

    async_add_entities(entities)


class LazarCWUClimate(CoordinatorEntity, ClimateEntity):
    _attr_name = "CWU"
    _attr_hvac_modes = [HVACMode.HEAT, HVACMode.OFF]
    _attr_supported_features = ClimateEntityFeature.TARGET_TEMPERATURE
    _attr_temperature_unit = UnitOfTemperature.CELSIUS

    def __init__(self, coordinator):
        super().__init__(coordinator)
        self._attr_unique_id = f"{coordinator.data['boxid']}_cwu"

    @property
    def current_temperature(self):
        v = self.coordinator.data["stat"]["temps"]["cwu"]
        return None if v == -9999 else v / 10

    @property
    def target_temperature(self):
        return self.coordinator.data["params"]["cwu"]["tsetcomf"] / 10

    async def async_set_temperature(self, **kwargs):
        value = int(kwargs["temperature"] * 10)
        await self.hass.async_add_executor_job(
            self.coordinator.api.set_param,
            "tsetcomf",
            value,
        )
        await self.coordinator.async_request_refresh()

    @property
    def hvac_mode(self):
        return HVACMode.HEAT if self.coordinator.data["params"]["onoff"] == 1 else HVACMode.OFF
