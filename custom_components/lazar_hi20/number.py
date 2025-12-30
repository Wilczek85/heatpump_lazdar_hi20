from __future__ import annotations

from homeassistant.components.number import NumberEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant

from .const import DOMAIN


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities,
) -> None:
    """Set up number entities (placeholder)."""

    # Na razie pusta lista – docelowo tu będą:
    # - tseteco
    # - tsetcomf
    # - krzywe grzewcze
    async_add_entities([])
