import datetime as dt

from tests.functional.utils import Envs, check_identical_dict, ts_to_dt


def test_get_time(clients):
    sv_time = Envs._make([ts_to_dt(client.get_time()) for client in clients])
    assert sv_time.prod == sv_time.uat


def test_get_config(clients):
    resps = Envs._make([client.get_config() for client in clients])
    check_identical_dict(resps)


def test_get_symbol(clients):
    resps = Envs._make(
        [client.get_symbol(symbol='VN30F1M') for client in clients]
    )
    check_identical_dict(resps)


def test_search_symbols(clients):
    resps = Envs._make(
        [
            client.search_symbols(limit=30, query='VN', type='FUT')
            for client in clients
        ]
    )
    check_identical_dict(resps)


def test_get_history(clients):
    resps = Envs._make(
        [
            client.get_history(
                symbol='AAA',
                resolution='30',
                from_ts=dt.datetime(2023, 7, 7, 7, 0),
                to_ts=dt.datetime(2023, 7, 7, 16, 0),
            ) for client in clients
        ]
    )
    for resp in resps:
        resp['nextTime'] = ts_to_dt(resp['nextTime'])
        resp['t'] = [ts_to_dt(ts) for ts in resp['t']]

    check_identical_dict(resps)


def test_user_charts(clients):
    resps = Envs._make(
        [client.get_user_charts(client='test', user=1) for client in clients]
    )
    for resp in resps:
        for chart in resp['data']:
            chart['timestamp'] = ts_to_dt(chart['timestamp'])

    check_identical_dict(resps)
