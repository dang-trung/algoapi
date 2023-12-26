import datetime as dt

from tests.functional.utils import ts_to_dt


def test_get_time(client):
    now = dt.datetime.now().replace(microsecond=0)
    sv_time = ts_to_dt(client.get_time())
    assert sv_time == now


def test_get_config(client):
    resp = client.get_config()
    for k in [
        'supports_search', 'supports_group_request', 'supports_marks',
        'supports_timescale_marks', 'supports_time', 'exchanges',
        'symbols_types', 'supported_resolutions'
    ]:
        assert k in resp.keys()


def test_get_symbol(client):
    resp = client.get_symbol(symbol='VN30F1M')
    for k in [
        'name', 'exchange_traded', 'exchange_listed', 'timezone', 'minmov',
        'minmov2', 'pointvalue', 'session', 'has_intraday', 'has_no_volume',
        'description', 'type', 'intraday_multipliers', 'supported_resolutions',
        'pricescale', 'ticker'
    ]:
        assert k in resp.keys()


def test_search_symbols(client):
    resp = client.search_symbols(limit=30, query='VN', type='FUT')
    assert len(resp) == 4
    for k in ['symbol', 'full_name', 'description', 'exchange', 'type']:
        assert k in resp[0].keys()


def test_get_history(client):
    resp = client.get_history(
        symbol='VNINDEX',
        resolution='30',
        from_ts=dt.datetime(2023, 10, 16, 7, 0),
        to_ts=dt.datetime(2023, 10, 16, 16, 0),
    )
    resp['nextTime'] = ts_to_dt(resp['nextTime'])
    resp['t'] = [ts_to_dt(ts) for ts in resp['t']]
    print(resp)

    assert type(resp) == dict
    for k in ['nextTime', 't', 'o', 'h', 'l', 'c', 'v', 's']:
        assert k in resp.keys()


def test_user_chart(client):
    # Original charts
    resp = client.get_user_charts(client='test', user=1)
    for chart in resp['data']:
        chart['timestamp'] = ts_to_dt(chart['timestamp'])

    print('Original charts:', resp)

    if len(resp['data']) == 0:
        next_id = 1
    else:
        next_id = resp['data'][-1]['id'] + 1

    # Add a chart
    client.add_user_chart(
        client='test',
        user=1,
        name=f'bscalgo{next_id}',
        content='1',
        symbol='HPG',
        resolution='D',
    )

    resp = client.get_user_charts(client='test', user=1)
    for chart in resp['data']:
        chart['timestamp'] = ts_to_dt(chart['timestamp'])
    print('Charts after adding:', resp)

    # Remove chart by ID
    client.delete_user_chart(client='test', user=1, chart=next_id)
    resp = client.get_user_charts(client='test', user=1)
    for chart in resp['data']:
        chart['timestamp'] = ts_to_dt(chart['timestamp'])
    print('Charts left after removing:', resp)
