import pytest


@pytest.fixture(scope='session', autouse=True)
def add_user_id(client):
    client.set_user_id('130192')


def test_get_filter_range(client):
    print('\n', client.get_filter_range())


def test_get_all_filters(client):
    print('\n', client.get_all_filters())


def test_create_update_delete_filter(client):
    print('\n')
    # get all filter_id pre-add
    ori_filter_ids = [
        str(f['FilterId']) for f in client.get_all_filters()['data']
    ]
    print('Original filter_ids:', ori_filter_ids)

    # run and save a filter to initiate
    client.create_filter(
        filter=[
            {
                'code': 'MC',
                'low': 100,
                'high': 496311
            }, {
                'code': 'P_PER_MAX_52W',
                'low': 99,
                'high': 100
            }
        ],
        exchange='',
        industry='',
        name='TEST'
    )

    # get all filter_id pre-delete
    filter_ids = [str(f['FilterId']) for f in client.get_all_filters()['data']]
    print('Post-adding new filter:', filter_ids)

    # check if a new filter is added
    assert len(filter_ids) == len(ori_filter_ids) + 1

    # try update filter params
    selected_id = filter_ids[-1]
    print(
        f'Pre-update filter w/ id {selected_id}:',
        client.get_filter_by_id(filter_id=selected_id)
    )

    client.update_filter(
        filter_id=selected_id,
        name='RENAMED TEST',
        exchange='HOSE',
        industry='',
        filter=[
            {
                'code': 'MC',
                'low': 100,
                'high': 1000
            }, {
                'code': 'P_PER_MAX_52W',
                'low': 95,
                'high': 100
            }
        ],
    )
    filter = client.get_filter_by_id(filter_id=selected_id)
    print(f'Post-update filter w/ id {selected_id}:', filter)

    # check if the filter's exchange got updated or not
    assert filter['exchange'] == 'HOSE'

    # delete filter_id just added for testing
    client.delete_filter(filter_id=selected_id)

    # get all filter_id post-delete
    filter_ids = [str(f['FilterId']) for f in client.get_all_filters()['data']]
    print(f'Post-deleting filter w/ id {selected_id}:', filter_ids)

    # check if the selected filter_id got deleted or not
    assert not selected_id in filter_ids
    assert filter_ids == ori_filter_ids


def test_get_filter_by_id(client):
    filter = client.get_filter_by_id('2353')
    assert isinstance(filter, dict)
    for k in ['filter_id', 'name', 'exchange', 'industry', 'filter']:
        assert k in filter.keys()


def test_run_filter_by_id(client):
    print(client.run_filter_by_id('2353'))
