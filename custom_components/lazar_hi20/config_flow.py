from homeassistant import config_entries
import voluptuous as vol
from .const import DOMAIN
from .api import LazarHi20API

class LazarConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION = 1

    async def async_step_user(self, user_input=None):
        errors = {}

        if user_input:
            api = LazarHi20API(
                user_input["login"],
                user_input["password"]
            )
            try:
                await self.hass.async_add_executor_job(api.login_api)
                return self.async_create_entry(
                    title="Lazar Hi20",
                    data=user_input
                )
            except Exception:
                errors["base"] = "auth"

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema({
                vol.Required("login"): str,
                vol.Required("password"): str
            }),
            errors=errors
        )
