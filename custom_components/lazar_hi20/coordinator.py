from datetime import timedelta
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed
from .const import UPDATE_INTERVAL

class LazarCoordinator(DataUpdateCoordinator):
    def __init__(self, hass, api):
        self.api = api
        super().__init__(
            hass,
            logger=None,
            name="Lazar HI20",
            update_interval=timedelta(seconds=UPDATE_INTERVAL),
        )

    async def _async_update_data(self):
        try:
            return await self.hass.async_add_executor_job(self.api.get_data)
        except Exception as err:
            raise UpdateFailed(err) from err
