import pytest

from algoapi import AlgoAPI


@pytest.fixture(scope='session', autouse=True)
def client():
    return AlgoAPI()