import pandas as pd
import pytest

from tests.functional.utils import Envs, check_identical


@pytest.fixture(scope='session', autouse=True)
def add_user_id(clients):
    [client.set_user_id('230992') for client in clients]


def test_get_filter_range(clients):
    resps = Envs._make(
        [pd.DataFrame(client.get_filter_range()['data']) for client in clients]
    )

    check_identical(resps)


def test_run_filter(clients):
    resps = Envs._make(
        [
            pd.DataFrame(
                client.run_filter(
                    filter=[{
                        'code': 'MC',
                        'low': 9000,
                        'high': 10000
                    }],
                    exchange='HOSE',
                    industry='',
                )['data']['items']
            )[['SECURITY_CODE', 'EXCHANGE_CODE', 'MC']] for client in clients
        ]
    )

    check_identical(resps)


def test_get_all_filters(clients):
    resps = Envs._make([client.get_all_filters() for client in clients])
    [print(f'[{env.upper()}]\n{resp}') for env, resp in resps._asdict().items()]
