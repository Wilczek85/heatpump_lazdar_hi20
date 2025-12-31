from homeassistant.components.number import NumberEntity
from homeassistant.helpers.update_coordinator import CoordinatorEntity
from .const import DOMAIN

CURVES = {
    "tsetcrvTp15": "Krzywa grzewcza +15°C",
    "tsetcrvT0": "Krzywa grzewcza 0°C",
    "tsetcrvTm10": "Krzywa grzewcza -10°C",
    "tsetcrvTm20": "Krzywa grzewcza -20°C",
}


async def async_setup_entry(hass, entry, async_add_entities):
    coordinator = hass.data[DOMAIN][entry.entry_id]

    entities = [
        LazarCurveNumber(coordinator, key, name, entry.entry_id)
        for key, name in CURVES.items()
    ]

    async_add_entities(entities)


class LazarCurveNumber(CoordinatorEntity, NumberEntity):
    def __init__(self, coordinator, key, name, entry_id):
        super().__init__(coordinator)
        self._key = key
        self._entry_id = entry_id

        self._attr_name = name
        self._attr_unique_id = f"{entry_id}_{key}"

        self._attr_native_min_value = 0
        self._attr_native_max_value = 400
        self._attr_native_step = 1

    @property
    def native_value(self):
        data = self.coordinator.data
        if not data:
            return None

        try:
            return data["params"]["cricuits"][0][self._key]
        except Exception:
            return None

    async def async_set_native_value(self, value):
        data = self.coordinator.data
        if not data:
            return

        curves = data["params"]["cricuits"][0]

        # 🔒 WALIDACJA ZALEŻNOŚCI
        if self._key == "tsetcrvTp15" and value > curves["tsetcrvT0"]:
            raise ValueError("+15°C nie może być większe niż 0°C")
        if self._key == "tsetcrvT0" and value > curves["tsetcrvTm10"]:
            raise ValueError("0°C nie może być większe niż -10°C")
        if self._key == "tsetcrvTm10" and value > curves["tsetcrvTm20"]:
            raise ValueError("-10°C nie może być większe niż -20°C")

        await self.hass.async_add_executor_job(
            self.coordinator.api.set_param,
            self._key,
            int(value),
        )
        await self.coordinator.async_request_refresh()
