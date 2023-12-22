import pandas as pd


def check_identical(resps):
    for resp in resps:
        resp.columns = resp.columns.str.lower()

    if not resps.prod.equals(resps.uat):
        print('[NOT IDENTICAL]')

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

    print()
