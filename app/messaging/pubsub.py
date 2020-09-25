from pubsub import pub
from app.messaging import PriceInfoMessenger

class PyPubSubPriceMessenger(PriceInfoMessenger):
    def publish_all_info(self):
        for fetcher in self.fetchers:
            data = fetcher.fetch_prices()
            pub.sendMessage(fetcher.symbol, data)