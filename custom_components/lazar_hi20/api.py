import requests
from .const import BASE_URL, LOGIN_ENDPOINT, DATA_ENDPOINT

class LazarHi20API:
    def __init__(self, login, password):
        self.session = requests.Session()
        self.login = login
        self.password = password

    def login_api(self):
        r = self.session.post(
            BASE_URL + LOGIN_ENDPOINT,
            data={"login": self.login, "haslo": self.password},
            timeout=10
        )
        r.raise_for_status()

    def get_data(self):
        r = self.session.get(
            BASE_URL + DATA_ENDPOINT,
            params={"what": "bcst"},
            timeout=10
        )
        r.raise_for_status()
        return r.json()

    def set_param(self, param, value):
        r = self.session.get(
            BASE_URL + DATA_ENDPOINT,
            params={
                "what": "setparam",
                "param": param,
                "value": value
            },
            timeout=10
        )
        r.raise_for_status()
