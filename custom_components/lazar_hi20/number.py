from homeassistant.components.number import NumberEntity
from homeassistant.helpers.update_coordinator import CoordinatorEntity
from .const import DOMAIN

CURVES = {
    "tsetcrvTp15": ("Krzywa +15°C", 0, 400),
    "tsetcrvT0": ("Krzywa 0°C", 0, 400),
    "tsetcrvTm10": ("Krzywa -10°C", 0, 400),
    "tsetcrvTm20": ("Krzywa -20°C", 0, 400),
}

async def async_setup_entry(hass, entry, async_add_entities):
    coordinator = hass.data[DOMAIN][entry.entry_id]

    entities = [
        LazarCurveNumber(coordinator, key, name)
        for key, (name, _, _) in CURVES.items()
    ]

    async_add_entities(entities)


class LazarCurveNumber(CoordinatorEntity, NumberEntity):
    def __init__(self, coordinator, key, name):
        super().__init__(coordinator)
        self.key = key
        self._attr_name = name
        self._attr_unique_id = f"{coordinator.data['boxid']}_{key}"
        self._attr_native_min_value = 0
        self._attr_native_max_value = 400
        self._attr_native_step = 1

    @property
    def native_value(self):
        return self.coordinator.data["params"]["cricuits"][0][self.key]

    async def async_set_native_value(self, value):
        data = self.coordinator.data["params"]["cricuits"][0]

        # WALIDACJA
        if self.key == "tsetcrvTp15" and value > data["tsetcrvT0"]:
            raise ValueError("+15°C nie może być większe niż 0°C")
        if self.key == "tsetcrvT0" and value > data["tsetcrvTm10"]:
            raise ValueError("0°C nie może być większe niż -10°C")
        if self.key == "tsetcrvTm10" and value > data["tsetcrvTm20"]:
            raise ValueError("-10°C nie może być większe niż -20°C")

        await self.hass.async_add_executor_job(
            self.coordinator.api.set_param,
            self.key,
            int(value),
        )
        await self.coordinator.async_request_refresh()
