from homeassistant.components.sensor import SensorEntity
from homeassistant.helpers.update_coordinator import CoordinatorEntity
from homeassistant.const import UnitOfEnergy
from .const import DOMAIN

async def async_setup_entry(hass, entry, async_add_entities):
    coordinator = hass.data[DOMAIN][entry.entry_id]
    async_add_entities([LazarEnergySensor(coordinator)])


class LazarEnergySensor(CoordinatorEntity, SensorEntity):
    _attr_name = "Lazar HI20 Energia"
    _attr_native_unit_of_measurement = UnitOfEnergy.KILO_WATT_HOUR
    _attr_state_class = "total_increasing"
    _attr_device_class = "energy"

    def __init__(self, coordinator):
        super().__init__(coordinator)
        self._attr_unique_id = f"{coordinator.data['boxid']}_energy"
        self._energy = 0

    @property
    def native_value(self):
        power = self.coordinator.data["stat"]["unit"]["powerneed"]
        self._energy += power / 1000 / 3600 * 30
        return round(self._energy, 3)
