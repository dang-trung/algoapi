import datetime as dt
from collections import namedtuple

import pandas as pd

# Multiple Envs Testing
Envs = namedtuple('Envs', ['prod', 'uat'])


# Check Identical Response Data
def check_identical(resps):
    for resp in resps:
        resp.columns = resp.columns.str.lower()

    if not resps.prod.equals(resps.uat):
        print('[NOT IDENTICAL]')
        print('[PROD]')
        print(resps.prod)
        print('[UAT]')
        print(resps.uat)

        merged = pd.concat(resps)
        dup_rows = merged[merged.duplicated(keep=False)]
        num_dup_rows = len(dup_rows)
        print(
            f'[DUPLICATE] {num_dup_rows} ROWS '
            f'({num_dup_rows / len(resps.prod):.0%} PROD)'
        )
        if num_dup_rows <= len(resps.prod):
            print('[DIFF]')
            for env, resp in resps._asdict().items():
                resp['env'] = env
            print(
                pd.concat(
                    [
                        resp.loc[~resp.index.isin(dup_rows.index)]
                        for resp in resps
                    ]
                ).sort_index()
            )
    else:
        print('[IDENTICAL]')


def check_identical_dict(resps):
    if not resps.prod == resps.uat:
        print('[NOT IDENTICAL]')
        print('[PROD]')
        print(resps.prod)
        print('[UAT]')
        print(resps.uat)
    else:
        print('[IDENTICAL]')


# Convert timestamp to datetime
def ts_to_dt(timestamp: int):
    if isinstance(timestamp, int):
        return dt.datetime.fromtimestamp(timestamp)
    return timestamp
