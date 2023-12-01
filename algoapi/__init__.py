from algoapi.filter import FilterClient


class AlgoAPI(FilterClient):

    def __init__(self, base_url: str = 'http://10.21.186.94:80') -> None:
        super().__init__()
        self.base_url = base_url
