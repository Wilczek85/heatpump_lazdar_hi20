from homeassistant.components.select import SelectEntity
from .const import DOMAIN

MODES = {
    0: "Grzanie",
    1: "Chłodzenie",
    2: "CWU"
}

async def async_setup_entry(hass, entry, async_add_entities):
    coordinator = hass.data[DOMAIN][entry.entry_id]
    async_add_entities([LazarModeSelect(coordinator)])

class LazarModeSelect(SelectEntity):
    _attr_name = "Lazar Tryb Pracy"
    _attr_unique_id = "lazar_hi20_mode"
    _attr_options = list(MODES.values())

    def __init__(self, coordinator):
        self.coordinator = coordinator

    @property
    def current_option(self):
        return MODES[self.coordinator.data["params"]["mode"]]

    async def async_select_option(self, option):
        for k, v in MODES.items():
            if v == option:
                await self.coordinator.api.set_param("mode", k)