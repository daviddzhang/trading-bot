from app.data import StockInfo
from app.models import PriceInfo
from app.models.apca_utils.apca_converters import apca_bar_to_candle
import alpaca_trade_api as tradeapi

class ScheduledStockInfo(StockInfo):
    def __init__(self, symbol: str, client: tradeapi.REST, range: int):
        StockInfo.__init__(self, symbol, range)
        self.client = client

    def fetch_prices(self) -> PriceInfo:
        try:
            apca_bar = self.client.get_barset(self.symbol, "minute", 1)[self.symbol][0]
            candle = apca_bar_to_candle(apca_bar)
            self._add_price(candle)
            return PriceInfo(list(self.price_buffer), list(self.indicator_buffer))

        except Exception as e:
            # TODO: update this error handling
            print(e)

