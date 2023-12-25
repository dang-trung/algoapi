import pytest

from algoapi import AlgoAPI
from tests.functional.utils import Envs


@pytest.fixture(scope='session', autouse=True)
def client():
    return AlgoAPI()


@pytest.fixture(autouse=True)
def print_new_line():
    print()


@pytest.fixture(scope='session')
def clients():
    return Envs(
        prod=AlgoAPI(base_url='http://10.21.186.94:80'),
        uat=AlgoAPI(base_url='http://10.21.170.66:8083', verbose=True)
    )
