import aiohttp
import async_timeout

class LazarAPI:
    def __init__(self, session, username, password):
        self._session = session
        self._username = username
        self._password = password

    async def login(self):
        async with async_timeout.timeout(10):
            resp = await self._session.post(
                "https://hkslazar.net/sollogin",
                data={"login": self._username, "haslo": self._password}
            )
            resp.raise_for_status()

    async def get_status(self):
        async with async_timeout.timeout(10):
            resp = await self._session.get(
                "https://hkslazar.net/oemSerwis?what=bcst"
            )
            resp.raise_for_status()
            return await resp.json()

    async def set_param(self, param, value):
        async with async_timeout.timeout(10):
            resp = await self._session.get(
                f"https://hkslazar.net/oemSerwis?what=setparam&param={param}&value={value}"
            )
            resp.raise_for_status()
            return await resp.json()