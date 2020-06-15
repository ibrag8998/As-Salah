from typing import Dict, Optional, Union, Any

import requests

from . import config
from .utils import get_month, get_year


class DataProvider:
    url: str
    payload: Dict[str, Union[int, float]]


class ConfigDataProvider(DataProvider):
    url: str = config.API_URL
    payload: Dict[str, Union[str, float]] = config.PAYLOAD

    def __init__(self) -> None:
        # Update month and year on each `__init__` call to current, if their
        # value is `None` in config (it is a special value)
        self.payload['month'] = self.payload['month'] or get_month()
        self.payload['year'] = self.payload['year'] or get_year()


class DataCollector:
    def __init__(self, data_provider: Optional[DataProvider] = None) -> None:
        self.data_provider = data_provider or ConfigDataProvider()

    def pull_json(self) -> Dict[str, Any]:
        """ Make request to API and return response json """
        response = requests.get(self.data_provider.url,
                                params=self.data_provider.payload)
        if response.ok:
            return response.json()
        raise ValueError(f"Response status code: {response.status_code}")
