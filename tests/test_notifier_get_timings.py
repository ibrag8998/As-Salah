from datetime import datetime

from as_salah.services.notifier import config
from as_salah.services.notifier.get_timings import (DataCollector,
                                                    ConfigDataProvider,
                                                    DataProvider)


def assert_response_ok(response):
    assert response['code'] == 200
    assert response['status'] == 'OK'


def test_ConfigDataProvider_updates():
    now = datetime.now()
    payload = ConfigDataProvider().payload
    assert payload['month'] == now.month
    assert payload['year'] == now.year


def test_DataCollector_response_ok():
    response_json = DataCollector().pull_json()
    assert_response_ok(response_json)


def test_DataCollector_custom_data_provider():
    class CustomDataProvider(DataProvider):
        url = config.API_URL
        payload = config.PAYLOAD
        payload.update({'year': 2001, 'latitude': 45})

    response_json = DataCollector(CustomDataProvider()).pull_json()
    assert_response_ok(response_json)
