import logging
from app.data import PriceInfoFetcher
from app.models import PriceInfo
from app.models.apca_utils.apca_converters import apca_bar_to_candle
import alpaca_trade_api as tradeapi

# fetcher that uses Alpaca's API to get a set of bars. To be used until streaming is available for  account
class ScheduledAlpacaRestStockInfoFetcher(PriceInfoFetcher):
    def __init__(self, symbol: str, range: int):
        PriceInfoFetcher.__init__(self, symbol, range)
        self.client = tradeapi.REST()

    def fetch_prices(self) -> PriceInfo:
        try:
            apca_bar = self.client.get_barset(symbols=self.symbol, timeframe="minute", limit=1)[self.symbol][0]
            candle = apca_bar_to_candle(apca_bar)
            self._add_price(candle)
            return PriceInfo(list(self.price_buffer), list(self.indicator_buffer))
        # TODO: update this error handling
        except Exception:
            logging.exception("Error while fetching stock data from Alpaca REST API")
