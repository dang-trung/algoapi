import datetime as dt

from algoapi.base import BaseClient


class TradingViewClient(BaseClient):

    def get_history(
        self,
        symbol: str,
        resolution: int | str,
        from_ts: int | dt.datetime,
        to_ts: int | dt.datetime,
    ):
        endpoint = '/tradingview/api/1.1/history'

        return self._get(
            endpoint=endpoint,
            params=self._params(self.get_history, locals()),
        )
