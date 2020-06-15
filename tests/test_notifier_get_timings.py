from datetime import datetime

from as_salah.services.notifier.get_timings import (DataCollector,
                                                    ConfigDataProvider)


def test_ConfigDataProvider_updates():
    now = datetime.now()
    params = ConfigDataProvider().params
    assert params['month'] == now.month
    assert params['year'] == now.year


def test_DataCollector_response_ok():
    response = DataCollector().pull_json()
    assert response['code'] == 200
    assert response['status'] == 'OK'
