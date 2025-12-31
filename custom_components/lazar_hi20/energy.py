from homeassistant.components.sensor import SensorEntity, SensorDeviceClass
from homeassistant.helpers.update_coordinator import CoordinatorEntity
from homeassistant.const import UnitOfPower, UnitOfEnergy
from .const import DOMAIN

async def async_setup_entry(hass, entry, async_add_entities):
    coordinator = hass.data[DOMAIN][entry.entry_id]

    async_add_entities([
        LazarPowerSensor(coordinator),
        LazarEnergySensor(coordinator),
    ])


class LazarPowerSensor(CoordinatorEntity, SensorEntity):
    _attr_name = "Lazar HI20 Pobór mocy"
    _attr_native_unit_of_measurement = UnitOfPower.WATT
    _attr_device_class = SensorDeviceClass.POWER
    _attr_state_class = "measurement"

    def __init__(self, coordinator):
        super().__init__(coordinator)
        self._attr_unique_id = f"{coordinator.config_entry.entry_id}_power"

    @property
    def native_value(self):
        return self.coordinator.data["stat"]["unit"]["powerneed"]


class LazarEnergySensor(CoordinatorEntity, SensorEntity):
    _attr_name = "Lazar HI20 Energia"
    _attr_native_unit_of_measurement = UnitOfEnergy.KILO_WATT_HOUR
    _attr_device_class = SensorDeviceClass.ENERGY
    _attr_state_class = "total_increasing"

    def __init__(self, coordinator):
        super().__init__(coordinator)
        self._attr_unique_id = f"{coordinator.config_entry.entry_id}_energy"
        self._energy = 0.0

    @property
    def native_value(self):
        power_w = self.coordinator.data["stat"]["unit"]["powerneed"]
        # 30s update → kWh
        self._energy += (power_w / 1000) * (30 / 3600)
        return round(self._energy, 4)
