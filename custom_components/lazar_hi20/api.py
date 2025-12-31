import requests

class LazarHi20API:
    def __init__(self, username, password):
        self._session = requests.Session()
        self._username = username
        self._password = password

    def login(self):
        r = self._session.post(
            "https://hkslazar.net/sollogin",
            data={"login": self._username, "haslo": self._password},
            timeout=10,
        )
        r.raise_for_status()

    def get_data(self):
        r = self._session.get(
            "https://hkslazar.net/oemSerwis?what=bcst",
            timeout=10,
        )
        r.raise_for_status()
        return r.json()

    def set_param(self, param, value):
        r = self._session.get(
            f"https://hkslazar.net/oemSerwis?what=setparam&param={param}&value={value}",
            timeout=10,
        )
        r.raise_for_status()
