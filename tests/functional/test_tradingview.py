import datetime as dt

import pytest

from algoapi import AlgoAPI


@pytest.fixture(scope='module', autouse=True)
def client():
    return AlgoAPI()


def test_history(client):
    r = client.get_history(
        symbol='VNINDEX',
        resolution='30',
        from_ts=dt.datetime(2023, 10, 16, 7, 0),
        to_ts=dt.datetime(2023, 10, 16, 16, 0),
    )
    r['nextTime'] = convert_to_dt(r['nextTime'])
    r['t'] = [convert_to_dt(ts) for ts in r['t']]

    print('\n', r)
    assert type(r) == dict
    assert r.keys()


def convert_to_dt(dt_obj: dt.datetime):
    if isinstance(dt_obj, int):
        return dt.datetime.fromtimestamp(dt_obj)
    return dt_obj
