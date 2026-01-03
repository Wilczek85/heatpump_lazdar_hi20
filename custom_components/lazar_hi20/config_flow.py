from homeassistant import config_entries
from homeassistant.core import callback
from .const import DOMAIN

class LazarConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION = 1

    async def async_step_user(self, user_input=None):
        if user_input:
            return self.async_create_entry(title="Lazar HI20", data=user_input)
        return self.async_show_form(
            step_id="user",
            data_schema=self.schema({})
        )