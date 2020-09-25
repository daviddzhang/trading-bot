from abc import ABC, abstractmethod
from typing import Deque
from collections import deque
from app.models import Candlestick, IndicatorInfo, PriceInfo

# abstract class for any type of stock info
DEFAULT_UPDATE_INTERVAL = 60

class PriceInfoFetcher(ABC):
    def __init__(self, symbol: str, range: int):
        self.symbol = symbol
        # ring buffer-type data structure via queue
        self.price_buffer: Deque[Candlestick] = deque(maxlen=range)
        self.indicator_buffer: Deque[IndicatorInfo] = deque(maxlen=range)

    # method to retrieve updated price info for the interval
    @abstractmethod
    def fetch_prices(self) -> PriceInfo:
        pass

    @abstractmethod
    def _add_price(self, candle: Candlestick) -> None:
        self.price_buffer.append(candle)

    def _add_indicator(self, indicator: IndicatorInfo) -> None:
        self.indicator_buffer.append(indicator)
