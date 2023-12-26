import pytest


@pytest.fixture(scope='session', autouse=True)
def add_user_id(client):
    client.set_user_id('230992')


def test_get_formula_signal(client):
    client.get_formula_signal()


def test_get_signals(client):
    client.get_signals()


def test_modify_signal(client):
    active_signals = client.get_signals_by_status(active=True)
    num_signals_pre_add = len(active_signals)

    # Register formula
    client.register_signal(formula_id=1133)
    active_signals = client.get_signals_by_status(active=True)
    num_signals_post_add = len(active_signals)

    # Unsub formula
    client.unsubcribe_signal(formula_id=1133)
    active_signals = client.get_signals_by_status(active=True)
    num_signals_post_delete = len(active_signals)

    assert num_signals_post_add == num_signals_pre_add + 1
    assert num_signals_post_delete == num_signals_pre_add


def test_get_signal_histories(client):
    signal = client.get_signal_histories(formula_id=1133)['data'][0]
    for k in [
        'currentDate', 'realTimeFormulaID', 'name', 'nameCN', 'nameEN',
        'nameKR', 'nameJP', 'tradeDate', 'exchangeCode', 'securityCode',
        'closePrice', 'levelName', 'marketCapital', 'secBtPerf', 'buySellInd',
        'priceColor', 'shortNameCN', 'shortNameKR', 'shortNameJP', 'shortName',
        'shortNameEN', 'levelNameEN', 'levelNameCN', 'levelNameKR',
        'levelNameJP', 'avgVlol5d', 'priceChange'
    ]:
        assert k in signal
