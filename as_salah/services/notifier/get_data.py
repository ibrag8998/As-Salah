from typing import Dict, Union, Any

import requests

from . import config
from .utils import get_month, get_year


class ConfigDataProvider:
    url: str = config.API_URL
    params: Dict[str, Union[str, float]] = config.PAYLOAD

    def __init__(self) -> None:
        # Update month and year on each `__init__` call to current, if their
        # value is `None` in config (it is a special value)
        self.params['month'] = self.params['month'] or get_month()
        self.params['year'] = self.params['year'] or get_year()


class DataCollector(ConfigDataProvider):
    def pull_json(self) -> Dict[str, Any]:
        """ Make request to API and return response json """
        response = requests.get(self.url, params=self.params)
        if response.ok:
            return response.json()
        raise ValueError(f"Response status code: {response.status_code}")
