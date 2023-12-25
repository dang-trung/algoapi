from algoapi import AlgoAPI


def test_snake_to_camel():
    assert AlgoAPI._snake_to_camel('camel_case') == 'camelCase'
    assert AlgoAPI._snake_to_camel('camel_Case') == 'camelCase'
    assert AlgoAPI._snake_to_camel('Camel_Case') == 'camelCase'
    assert AlgoAPI._snake_to_camel('user_id') == 'userID'
