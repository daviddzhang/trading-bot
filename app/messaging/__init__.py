from abc import ABC, abstractmethod
from typing import List
from app.data import PriceInfoFetcher

# abstract class for any intermediate class that handles messaging/pubsub for price info. should take in list of fetchers
# indicating where to get data from. inheriting classes must implement publishing/messaging method
class PriceInfoMessenger(ABC):
    def __init__(self, fetchers: List[PriceInfoFetcher], interval: int = 60):
        self.fetchers = fetchers
        self.interval = interval

    @abstractmethod
    def publish_all_info(self):
        pass

    def add_producer(self, fetcher: PriceInfoFetcher) -> None:
        self.info_list.append(fetcher)
