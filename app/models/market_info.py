from typing import List, Dict

class Candlestick:
    def __init__(self, high: float, low: float, open: float, close: float, volume: int, time: int):
        self.high = high
        self.low = low
        self.open = open
        self.close = close
        self.volume = volume
        self.time = time


class IndicatorInfo:
    def __init__(self, info: Dict[str, float]):
        self.info = info

class PriceInfo:
    def __init__(self, price_list: List[Candlestick], indicator_list: List[IndicatorInfo]):
        self.price_list = price_list
        self.indicator_list = indicator_list


