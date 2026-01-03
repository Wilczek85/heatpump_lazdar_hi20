import logging
from homeassistant.helpers.aiohttp_client import async_get_clientsession
from .api import LazarAPI
from .coordinator import LazarCoordinator
from .const import DOMAIN, PLATFORMS

_LOGGER = logging.getLogger(__name__)

async def async_setup_entry(hass, entry):
    session = async_get_clientsession(hass)
    api = LazarAPI(session, entry.data["username"], entry.data["password"])
    await api.login()

    coordinator = LazarCoordinator(hass, api)
    await coordinator.async_config_entry_first_refresh()

    hass.data.setdefault(DOMAIN, {})[entry.entry_id] = coordinator
    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)
    return True