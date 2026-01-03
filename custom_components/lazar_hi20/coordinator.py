from datetime import timedelta
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed
from .api import LazarAPI
from .const import DOMAIN

class LazarCoordinator(DataUpdateCoordinator):
    def __init__(self, hass, api):
        super().__init__(
            hass,
            logger=hass.logger,
            name=DOMAIN,
            update_interval=timedelta(seconds=30),
        )
        self.api = api

    async def _async_update_data(self):
        try:
            return await self.api.get_status()
        except Exception as err:
            raise UpdateFailed(f"API error: {err}")